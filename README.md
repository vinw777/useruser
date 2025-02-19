# User Management System

## Overview

This is a simple **User Management System** I created to practice working with classes, class methods, static methods, and unit testing in Python. The project includes a `User` class, a `UserService` class to manage users, and a `UserUtil` class that provides utility functions for generating emails, passwords, and more.

## Technologies Used

- **Python** – This project is written in Python 3.8+.
- **unittest** – I used the built-in `unittest` library to write test cases for the different functionalities of the system.

## Classes and Functions

### `User` Class
The `User` class represents a user with the following functions:
- `__init__(self, user_id, name, surname, birthday)`: Initializes the user with a unique ID, name, surname, and birthday.
- `get_details(self)`: Returns a formatted string with the user's details.
- `get_age(self)`: Calculates and returns the user's age based on their birthday.

### `UserService` Class
The `UserService` class is responsible for managing users. It provides functions like:
- `add_user(cls, user)`: Adds a new user to the system.
- `find_user(cls, user_id)`: Searches for a user by their ID and returns the user if found.
- `delete_user(cls, user_id)`: Removes a user from the system by their ID.
- `update_user(cls, user_id, user_update)`: Updates a user’s details.
- `get_number(cls)`: Returns the total number of users in the system.

### `UserUtil` Class
The `UserUtil` class contains utility functions that help in user creation and validation:
- `generate_user_id()`: Generates a unique 9-digit user ID using the current year and random digits.
- `generate_password()`: Generates a random password with at least 8 characters, including uppercase, lowercase, digits, and special characters.
- `is_strong_password(password)`: Validates whether a password is strong enough.
- `generate_email(name, surname, domain)`: Creates an email using the user's name, surname, and a given domain.
- `validate_email(email)`: Checks if the email format is valid.

## What I Learned

- **Classes and Objects**: I learned how to create and work with Python classes, and how to use instance variables and methods.
- **Class and Static Methods**: I explored the difference between instance methods, class methods, and static methods, and when to use them.
- **Unit Testing**: I practiced writing unit tests using the `unittest` module to ensure that my classes and methods are working correctly.
- **Random Data Generation**: I gained experience generating random values like user IDs, passwords, and emails.
- **Email Validation**: I learned how to use regular expressions to validate email addresses and ensure they follow the correct format.

## UML
![UML](https://i.ibb.co/zVK6qLW5/Untitled-Diagram.jpg)
