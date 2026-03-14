import unittest
from library_system.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python Basics", "John Doe", "12345")

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Python Basics")
        self.assertEqual(self.book.author, "John Doe")
        self.assertTrue(self.book.available)

    def test_check_out(self):
        success, message = self.book.check_out("MEM001")
        self.assertTrue(success)
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.book.check_out("MEM001")
        success, message = self.book.return_book()
        self.assertTrue(success)
        self.assertTrue(self.book.available)


if __name__ == "__main__":
    unittest.main()
