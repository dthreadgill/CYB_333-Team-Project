# Simple Password Checker

## Description
This is a simple password checker written in Python. It verifies if a password meets basic security criteria such as minimum length, inclusion of both uppercase and lowercase letters, digits, and special characters.

## Features
- Checks if the password is at least 8 characters long.
- Ensures the password contains both uppercase and lowercase characters.
- Verifies the presence of at least one digit in the password.
- Checks if the password includes at least one special character.

## Usage
To use this password checker, follow these steps:

1. Ensure you have Python installed on your system. This script is compatible with Python 3.x.
2. Copy the provided code into a file named `password_checker.py`.
3. Open a terminal or command prompt and navigate to the directory containing `password_checker.py`.
4. Run the script by executing the following command:
   ```sh
   python password_checker.py

## Code Explanation
The script contains several functions that each perform a specific check on the password:

`check_length(password)`: Checks if the password is at least 8 characters long.

`check_case(password)`: Ensures the password contains both uppercase and lowercase characters.

`check_digit(password)`: Verifies the presence of at least one digit in the password.

`check_special_character(password)`: Checks if the password includes at least one special character.

`check_password_strength(password)`: Completes all checks to determine the overall strength of the password and provides feedback.

Each function is well-documented with comments explaining its purpose and parameters.
