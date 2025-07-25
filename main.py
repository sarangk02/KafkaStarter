import re


def is_valid_email(email):
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not email:
        return False
    if re.match(regex, email):
        return True
    return False


while True:
    email = input("Enter an email address (or 'exit/quit/q' to quit)\n-> ")
    if email.lower() == "exit" or email.lower() == "quit" or email.lower() == "q":
        break
    if is_valid_email(email):
        with open("valid_emails.txt", "a") as file:
            file.write(email + "\n")
            print(f"'{email}' added to database.")
    else:
        print(f"'{email}' is not a valid email address.")

print("Exiting the email validation program.")
