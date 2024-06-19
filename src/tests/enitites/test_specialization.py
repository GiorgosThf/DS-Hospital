import unittest

from src.entities.Specialization import Specialization


class TestSpecialization(unittest.TestCase):

    def test_specialization_enum_values(self):
        assert Specialization.RADIOLOGIST.value == 'Radiologist'
        assert Specialization.HEMATOLOGIST.value == 'Hematologist'
        assert Specialization.ALLERGIST.value == 'Allergist'
        assert Specialization.PATHOLOGIST.value == 'Pathologist'
        assert Specialization.CARDIOLOGIST.value == 'Cardiologist'


if __name__ == '__main__':
    unittest.main()
