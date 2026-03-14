# Week5-Library-Management-System
A console-based Library Management System built in Python using Object-Oriented Programming to manage books, members, borrowing, and returning with JSON file storage.

## Project Overview
The **Library Management System** is a Python console-based application built using **Object-Oriented Programming (OOP)** principles.
This project allows librarians to manage books, register members, and handle borrowing and returning operations efficiently.

The system demonstrates how real-world entities such as **Books, Members, and Libraries** can be modeled using Python classes and objects.

##  Project Objectives

* Understand **Object-Oriented Programming concepts**
* Practice **class and object creation**
* Implement **methods and attributes**
* Work with **JSON file storage**
* Build a **menu-driven Python application**

##  OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Attributes and Methods
* Encapsulation
* Class interactions

##  Features

* Add new books to the library
* Register new members
* Borrow books
* Return books
* Search books by title, author, or ISBN
* View all books and members
* Track overdue books
* Save and load data using JSON files
* Simple and user-friendly menu interface

##  Project Structure

week5-library-system/

library_system/
│
├── __init__.py
├── book.py
├── member.py
├── library.py
└── main.py

data/
│
├── books.json
├── members.json
└── backup/

tests/
│
├── test_book.py
├── test_member.py
└── test_library.py

requirements.txt
README.md
.gitignore


##  Technologies Used

* Python 3
* Object-Oriented Programming
* JSON for data storage

No external libraries are required.


##  How to Run the Project

1. Clone the repository
git clone https://github.com/your-username/week5-library-system.git

2. Navigate to the project folder
cd week5-library-system

3. Run the program
python -m library_system.main


##  Example Menu

==============================
   LIBRARY MANAGEMENT SYSTEM
==============================

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Search Book
6. View Books
7. View Members
8. Save and Exit


## Example Output

Enter your choice: 1

Enter book title: Python Programming
Enter author: John Smith
Enter ISBN: 12345
Enter year: 2023

Book added successfully!

##  Data Storage

The system stores information using JSON files.

data/
│
├── books.json
├── members.json
└── backup/

These files allow the program to **save and load data automatically**.


##  Testing

Basic test files are included to verify system functionality:

* `test_book.py`
* `test_member.py`
* `test_library.py`


##  What I Learned

Through this project I learned:

* Object-Oriented Programming concepts
* Designing classes for real-world systems
* Managing relationships between objects
* File handling using JSON
* Building structured Python projects
  
##  Conclusion

The **Library Management System** demonstrates how Python and Object-Oriented Programming can be used to build practical applications.
It provides a structured and efficient way to manage books and members while maintaining persistent data storage.

---

⭐ This project was developed as part of **Week 5 – Object-Oriented Programming Basics**.
