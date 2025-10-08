# ch_6_password_locker.py
# An insecure password locker program.

# import sys
# import pyperclip

# PASSWORDS = {'email': 'email123',
#                 'phone': 'phone123'}


# def main():
#     if len(sys.argv) == 1:
#         print('Usage: app.py [account] - copy account password')

#     account = sys.argv[1]

#     if account in PASSWORDS:
#         pyperclip.copy(PASSWORDS[account])
#         print('Password for ' + account + ' copied to clipboard.')
#     else:
#         print(f'No password for {account}. Would you like to add? [y/N]: ', end='')
#         add_new_password = input()
#         if add_new_password == 'y' or add_new_password == 'Y':
#             print('Write account name: ', end='')
#             new_account = input()
#             print('Write account password: ', end='')
#             new_password = input()
#             PASSWORDS[new_account] = new_password
#             print(f'Added password for {new_account}: {new_password}'.replace(new_password, "********"))

# if __name__ == '__main__':
#     main()

# Refactored to improve readability and maintainability

import sys
import pyperclip

PASSWORDS = {
    "email": "email123",
    "phone": "phone123",
}


def main():
    if len(sys.argv) < 2:
        print("Usage: app.py [account] - copy account password")
        sys.exit(1)

    account = sys.argv[1]

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print(f"Password for {account} copied to clipboard.")
    else:
        add_new = input(
            f"No password for '{account}'. Would you like to add one? [y/N]: "
        ).strip().lower()

        if add_new == "y":
            new_account = input("Enter account name: ").strip()
            new_password = input("Enter account password: ").strip()

            if new_account and new_password:
                PASSWORDS[new_account] = new_password
                print(
                    f"Added password for {new_account}: {'*' * len(new_password)}"
                )
            else:
                print("Account name and password cannot be empty.")


if __name__ == "__main__":
    main()


