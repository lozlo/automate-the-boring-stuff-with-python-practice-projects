# ch_3_collatz_sequence.py
# This program generates the Collatz sequence for a given positive integer.


# def collatz(number):
#     while number != 1:
#         if number % 2 == 0:
#             print(number // 2)
#             return number // 2
#         elif number % 2 == 1:
#             print(3 * number + 1)
#             return 3 * number + 1
        

# def main():
#     while True:
#         try:
#             user_input = int(input("Enter a positive integer: "))
#             if user_input <= 0:
#                 print("Please enter a positive integer.")
#                 continue
#             while user_input != 1:
#                 user_input = collatz(user_input)
#             print("Sequence has reached 1.")
#             break
#         except ValueError:
#             print("Invalid input. Please enter a positive integer.")


# if __name__ == "__main__":
#     main()


# Refactored to improve readability and maintainability


def collatz(number):
    """Perform one step of the Collatz sequence and return the result."""
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    

def main():
    user_input = input("Enter a positive integer: ")
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Invalid input. Please enter a positive integer.")
        return
    
    number = int(user_input)
    while number != 1:
        number = collatz(number)
        print(number)
        
    print("Sequence has reached 1.")


if __name__ == "__main__":
    main()
