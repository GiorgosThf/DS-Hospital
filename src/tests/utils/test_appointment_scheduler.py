import unittest
from datetime import datetime, time, timedelta

from src.utils.AppointmentScheduler import AppointmentScheduler


class TestAppointmentScheduler(unittest.TestCase):

    def test_is_within_working_hours(self):
        # Test within working hours
        valid_time = datetime.strptime('10:00', '%H:%M').time()
        self.assertTrue(AppointmentScheduler.is_within_working_hours(valid_time))

        # Test outside working hours
        invalid_time = datetime.strptime('18:00', '%H:%M').time()
        self.assertFalse(AppointmentScheduler.is_within_working_hours(invalid_time))

        # Test edge case exactly at the end of working hours
        edge_time = datetime.strptime('17:00', '%H:%M').time()
        self.assertFalse(AppointmentScheduler.is_within_working_hours(edge_time))

        # Test edge case exactly at the start of working hours
        start_time = datetime.strptime('09:00', '%H:%M').time()
        self.assertTrue(AppointmentScheduler.is_within_working_hours(start_time))

    def test_is_date_within_range(self):
        # Test future date
        future_date = datetime.now().date() + timedelta(days=1)
        future_date_str = future_date.strftime('%Y-%m-%d')
        self.assertTrue(AppointmentScheduler.is_date_within_rang(future_date_str))

        # Test current date
        current_date = datetime.now().date()
        current_date_str = current_date.strftime('%Y-%m-%d')
        self.assertFalse(AppointmentScheduler.is_date_within_rang(current_date_str))

        # Test past date
        past_date = datetime.now().date() - timedelta(days=1)
        past_date_str = past_date.strftime('%Y-%m-%d')
        self.assertFalse(AppointmentScheduler.is_date_within_rang(past_date_str))

    def test_create_appointment_slots(self):
        slots = AppointmentScheduler.create_appointment_slots()

        # Check the number of slots generated
        self.assertEqual(len(slots), 8)  # Since 9:00 to 17:00 with 1 hour slots gives 8 slots

        # Check the start and end times of generated slots
        expected_slots = [time(hour=9, minute=0),
                          time(hour=10, minute=0),
                          time(hour=11, minute=0),
                          time(hour=12, minute=0),
                          time(hour=13, minute=0),
                          time(hour=14, minute=0),
                          time(hour=15, minute=0),
                          time(hour=16, minute=0)]

        self.assertEqual(slots, expected_slots)


if __name__ == '__main__':
    unittest.main()
