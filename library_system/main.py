from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


def menu():

    print("\n==============================")
    print("  LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. View All Books")
    print("7. View All Members")
    print("8. Save and Exit")
    print("==============================")


def main():

    library = Library()
    library.load_data()

    while True:

        menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            book = Book(title, author, isbn)
            library.add_book(book)

            print("Book added successfully")

        elif choice == "2":

            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")

            member = Member(name, member_id)
            library.register_member(member)

            print("Member registered successfully")

        elif choice == "3":

            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")

            print(library.borrow_book(member_id, isbn))

        elif choice == "4":

            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")

            print(library.return_book(member_id, isbn))

        elif choice == "5":

            keyword = input("Enter title or author: ")

            results = library.find_book(keyword)

            if results:
                for book in results:
                    print(book)
            else:
                print("No books found")

        elif choice == "6":

            for book in library.books.values():
                print(book)

        elif choice == "7":

            for member in library.members.values():
                print(member)

        elif choice == "8":

            library.save_data()
            print("Data saved successfully")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()