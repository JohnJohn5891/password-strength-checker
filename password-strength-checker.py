# password-strength-checker.py
# Gordon Lezama

from getpass import getpass

def lengthCheck(password):
    if len(password) < 8:
        print("You have a weak password. It is less than 8 characters")
    elif len(password) < 15:
        print("Your password is moderately strong. It is between 8 and 14 characters.")
    else:
        print("You have a strong password! It is over 14 characters.")

def specialCharacters(password):
    for x in password:
        if x == "!" or x == "#" or x == "@" or x == "%" or x == "$":
            print("Your password is strong, you have added special characters.")
            break

def main():
    # placeholder
    # Prompt the user to input a password
    password = getpass("Enter a password to be checked: ")

    # Check the length of the users password
    lengthCheck(password)

    # Check for special characters
    specialCharacters(password)

main()