from datetime import datetime, timedelta


class Book:
    """Represents a book in the library"""

    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None
        self.date_added = datetime.now().strftime("%Y-%m-%d")

    def check_out(self, member_id, loan_period=14):
        """Borrow a book"""

        if not self.available:
            return False, "Book already borrowed"

        self.available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=loan_period)).strftime("%Y-%m-%d")

        return True, f"Book borrowed successfully. Due date: {self.due_date}"

    def return_book(self):
        """Return book to library"""

        if self.available:
            return False, "Book already available"

        self.available = True
        self.borrowed_by = None
        self.due_date = None

        return True, "Book returned successfully"

    def is_overdue(self):
        """Check overdue status"""

        if self.due_date and not self.available:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return datetime.now() > due

        return False

    def days_overdue(self):
        """Calculate overdue days"""

        if self.is_overdue():
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return (datetime.now() - due).days

        return 0

    def to_dict(self):
        """Convert object to dictionary"""

        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date,
            "date_added": self.date_added
        }

    @classmethod
    def from_dict(cls, data):
        """Create object from dictionary"""

        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("year")
        )

        book.available = data["available"]
        book.borrowed_by = data.get("borrowed_by")
        book.due_date = data.get("due_date")
        book.date_added = data.get("date_added")

        return book

    def __str__(self):

        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"