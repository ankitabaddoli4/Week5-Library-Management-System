import unittest
from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


class TestLibrary(unittest.TestCase):

    def setUp(self):

        self.library = Library()

        self.book = Book("Python Basics", "John Doe", "12345")
        self.member = Member("Ankita", "MEM001")

        self.library.add_book(self.book)
        self.library.register_member(self.member)

    def test_add_book(self):
        self.assertIn("12345", self.library.books)

    def test_register_member(self):
        self.assertIn("MEM001", self.library.members)

    def test_borrow_book(self):
        result = self.library.borrow_book("MEM001", "12345")
        self.assertIn("successfully", result.lower())

    def test_return_book(self):
        self.library.borrow_book("MEM001", "12345")
        result = self.library.return_book("MEM001", "12345")
        self.assertEqual(result, "Book returned successfully")


if __name__ == "__main__":
    unittest.main()