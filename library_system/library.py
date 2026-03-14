import json
from library_system.book import Book
from library_system.member import Member


class Library:
    """Library system to manage books and members"""

    def __init__(self):

        self.books = {}
        self.members = {}

    def add_book(self, book):

        self.books[book.isbn] = book

    def register_member(self, member):

        self.members[member.member_id] = member

    def find_book(self, keyword):

        results = []

        for book in self.books.values():

            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)

        return results

    def borrow_book(self, member_id, isbn):

        if member_id not in self.members:
            return "Member not found"

        if isbn not in self.books:
            return "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = member.borrow_book(isbn)

        if not success:
            return message

        success, message = book.check_out(member_id)

        return message

    def return_book(self, member_id, isbn):

        if member_id not in self.members or isbn not in self.books:
            return "Invalid member or book"

        member = self.members[member_id]
        book = self.books[isbn]

        member.return_book(isbn)
        book.return_book()

        return "Book returned successfully"

    def save_data(self):

        with open("data/books.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open("data/members.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)

    def load_data(self):

        try:
            with open("data/books.json") as f:
                data = json.load(f)
                self.books = {k: Book.from_dict(v) for k, v in data.items()}
        except:
            self.books = {}

        try:
            with open("data/members.json") as f:
                data = json.load(f)
                self.members = {k: Member.from_dict(v) for k, v in data.items()}
        except:
            self.members = {}