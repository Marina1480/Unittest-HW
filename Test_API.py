import unittest
from Create_Yandexfolder import folder_create


class TestSomething(unittest.TestCase):

    def test_API(self):
        self.assertEqual(folder_create().status_code, 200)

    @unittest.expectedFailure
    def test_API_error(self):
        self.assertEqual(folder_create().status_code, 404)