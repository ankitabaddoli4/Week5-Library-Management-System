import unittest
from library_system.member import Member


class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Ankita", "MEM001")

    def test_member_creation(self):
        self.assertEqual(self.member.name, "Ankita")
        self.assertEqual(self.member.member_id, "MEM001")

    def test_borrow_book(self):
        success, message = self.member.borrow_book("12345")
        self.assertTrue(success)
        self.assertIn("12345", self.member.borrowed_books)

    def test_return_book(self):
        self.member.borrow_book("12345")
        success, message = self.member.return_book("12345")
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()