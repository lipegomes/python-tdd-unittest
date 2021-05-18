import unittest

from unittest.mock import patch

from src.base.Person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("Nikola", "Tesla")

    def test_person_attr_name_correct_name_value(self):
        self.assertEqual(self.p1.name, "Nikola")

    def test_person_attr_surname_correct_surname_value(self):
        self.assertEqual(self.p1.surname, "Tesla")

    def test_person_attr_obtained_data_start_false(self):
        self.assertFalse(self.p1.obtained_data)

    def test_person_attr_name_correct_name_is_str(self):
        self.assertIsInstance(self.p1.name, str)

    def test_person_attr_surname_correct_surname_is_str(self):
        self.assertIsInstance(self.p1.surname, str)

    def test_response_obtained_data_success_ok(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.response_obtained_data_success_ok(), "Connected")
            self.assertTrue(self.p1.obtained_data)

    def test_response_obtained_data_client_error_404(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.response_obtained_data_success_ok(), "Bad Request (400)")
            self.assertFalse(self.p1.obtained_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
