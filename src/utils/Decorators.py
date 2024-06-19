from functools import wraps

import jwt
from flask import request

from src.entities.ResponseEntity import ResponseEntity
from src.utils.Http import HTTP
from src.utils.ResponseData import ResponseData
from src.utils.ServiceException import ServiceException
from src.utils.TokenFactory import JWT


def token_required(secret_key):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):

            token = request.headers.get('Authorization')

            if JWT.is_missing(token):
                return error_as_response('Token is missing! Please provide authorization token', HTTP.FORBIDDEN)
            if JWT.is_blacklisted(token):
                return error_as_response('Token is invalid! Please verify token', HTTP.UNAUTHORIZED)
            try:
                data = JWT.decode_token(token, secret_key)
                current_user = data.get('username')

            except jwt.ExpiredSignatureError:
                return error_as_response('Token is expired! Please login', HTTP.UNAUTHORIZED)
            except jwt.InvalidTokenError:
                return error_as_response('Token is invalid! Please verify token', HTTP.UNAUTHORIZED)

            return f(current_user, *args, **kwargs)

        return decorated

    return decorator


def remove_token(secret_key):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if JWT.is_missing(token):
                return error_as_response('Token is missing! Please provide authorization token', HTTP.FORBIDDEN)
            if JWT.is_blacklisted(token):
                return error_as_response('Token is expired! User is already logged out!', HTTP.BAD_REQUEST)
            try:

                JWT.decode_token(token, secret_key)

            except jwt.ExpiredSignatureError:
                return error_as_response('Token is expired! User is already logged out', HTTP.BAD_REQUEST)
            except jwt.InvalidTokenError:
                return error_as_response('Token is invalid!', HTTP.UNAUTHORIZED)

            JWT.set_blacklisted_token(token)

            return f(token, *args, **kwargs)

        return decorated

    return decorator


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ServiceException as e:
            return (ResponseEntity.builder()
                    .with_status(e.status_code)
                    .with_data(ResponseData.builder()
                               .error(e.message)
                               .resp_status(ResponseData.ERROR).build())
                    .build())
        except Exception as e:
            return (ResponseEntity.builder()
                    .with_status(500)
                    .with_data(ResponseData.builder()
                               .error({str(e), str(e.args)})
                               .resp_status(ResponseData.ERROR).build())
                    .build())

    return wrapper


def error_as_response(error, status):
    return (ResponseEntity.builder()
            .with_status(status)
            .with_data(ResponseData.builder()
                       .error(error)
                       .resp_status(ResponseData.ERROR).build()).build())

