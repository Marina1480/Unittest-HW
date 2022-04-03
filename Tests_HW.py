import unittest
from Documents_copy import get_doc_owner_name, delete_doc, get_doc_shelf, add_new_doc

class TestSomething(unittest.TestCase):
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), "Василий Гупкин")

    def test_delete_doc(self):
        self.assertEqual(delete_doc(), ("2207 876234", True))

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), '1')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc(), '3')





