# Simple Password Checker

## Description
This Python script is designed to check the strength of a password based on customizable company policies. The script allows users to specify requirements for uppercase characters, lowercase characters, digits, special characters, and overall length. It also provides suggestions for valid passwords if the entered password does not meet the specified policy.

## Features
- Customizable Password Policy: Define the minimum and maximum length, required number of uppercase, lowercase, digits, and special characters.
- Password Validation: Check if a given password meets the defined policy.
- Password Suggestion: Generate a suggested password that complies with the policy requirements.

##Requirements
- Python 3
  
## How to Use

1. Clone the repository or download the script.
2. Run the script using a Python interpreter.
3. Follow the prompts to enter your company’s password policy.
4. Enter passwords to check their strength based on the defined policy.
5. The script will inform you if the password meets the requirements or suggest a valid password.

## Code Explanation
`get_company_policy()`: Prompts the user to enter the password policy requirements with validation.

`check_length(password, min_length, max_length)`: Checks if the password length is within the specified range.

`check_case(password, require_upper, require_lower)`: Checks if the password contains the required number of uppercase and lowercase characters.

`check_digit(password, require_digit)`: Checks if the password contains the required number of digits.

`check_special_character(password, require_special, special_characters)`: Checks if the password contains the required number of special characters.

`suggest_password(policy)`: Generates a suggested password that meets the policy requirements.

`check_password_strength(password, policy)`: Checks the overall strength of the password based on the company policy.

`main()`: Main function to run the script.
