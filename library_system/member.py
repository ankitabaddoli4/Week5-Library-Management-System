class Member:
    """Represents a library member"""

    def __init__(self, name, member_id):

        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 5

    def borrow_book(self, isbn):
        """Borrow a book"""

        if len(self.borrowed_books) >= self.max_books:
            return False, "Borrow limit reached"

        self.borrowed_books.append(isbn)
        return True, "Book added to borrowed list"

    def return_book(self, isbn):
        """Return a book"""

        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True, "Book returned"

        return False, "Book not found"

    def to_dict(self):
        """Convert object to dictionary"""

        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        """Create member from dictionary"""

        member = cls(
            data["name"],
            data["member_id"]
        )

        member.borrowed_books = data.get("borrowed_books", [])

        return member

    def __str__(self):

        return f"{self.name} (ID: {self.member_id}) - Borrowed Books: {len(self.borrowed_books)}"