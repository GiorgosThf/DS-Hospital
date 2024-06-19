import unittest
from datetime import datetime

from src.utils.DateUtils import DateTimeUtils


class TestDateTimeUtils(unittest.TestCase):
    def test_parse_date(self):
        date_str = '2024-07-01'
        date_format = '%Y-%m-%d'
        parsed_date = DateTimeUtils.parse_date(date_str, date_format)

        self.assertEqual(parsed_date.year, 2024)
        self.assertEqual(parsed_date.month, 7)
        self.assertEqual(parsed_date.day, 1)

    def test_parse_time(self):
        time_str = '14:30:00'
        time_format = '%H:%M:%S'
        parsed_time = DateTimeUtils.parse_time(time_str, time_format)

        self.assertEqual(parsed_time.hour, 14)
        self.assertEqual(parsed_time.minute, 30)
        self.assertEqual(parsed_time.second, 0)

    def test_date_to_string(self):
        date = datetime(year=2024, month=7, day=1)
        date_format = '%Y-%m-%d'
        date_str = DateTimeUtils.date_to_string(date, date_format)

        self.assertEqual(date_str, '2024-07-01')

    def test_time_to_string(self):
        time = datetime.strptime('14:30:00', '%H:%M:%S').time()
        time_format = '%H:%M:%S'
        time_str = DateTimeUtils.time_to_string(time, time_format)

        self.assertEqual(time_str, '14:30:00')


if __name__ == '__main__':
    unittest.main()
