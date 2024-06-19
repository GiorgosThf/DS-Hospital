from cerberus import schema_registry
from flask import Flask, Blueprint


from src.controllers import AdminController, PatientController, DoctorController
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


app.register_blueprint(AdminController.admin, url_prefix='/api/admin')
app.register_blueprint(DoctorController.doctor, url_prefix='/api/doctor')
app.register_blueprint(PatientController.patient, url_prefix='/api/patient')


swagger_ui_blueprint = get_swaggerui_blueprint(
    '/api/swagger',
    '/static/swagger.json',
    config={
        'app_name': 'DS Hospital API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix='/api/swagger')


schema_registry.add('is_specialization', {'type': 'boolean'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
