from datetime import datetime


class DateTimeUtils:
    @staticmethod
    def parse_date(date, date_format):
        return datetime.strptime(date, date_format).date()

    @staticmethod
    def parse_time(time, time_format):
        return datetime.strptime(time, time_format).time()

    @staticmethod
    def date_to_string(date, date_format):
        return date.strftime(date_format)

    @staticmethod
    def time_to_string(time, time_format):
        return time.strftime(time_format)
