# comma_code.py
# This program takes a list of items and returns a string with the items separated by commas,


# def comma_code(sequence):
#     result = ''
#     if not sequence:
#         return ''
#     elif len(sequence) == 1:
#         return sequence[0]
#     else:
#         for i in range(len(sequence) - 1):
#             result += str(sequence[i]) + ', '
#         result += 'and ' + str(sequence[-1])
#         return result
    

# def main():
#     spam = ['apples', 'bananas', 'tofu', 'cats']
#     print(comma_code(spam))
    

# if __name__ == "__main__":
#     main()


# Refactored to improve readability and maintainability


def comma_code(sequence):
    if not sequence:
        return ''
    elif len(sequence) == 1:
        return sequence[0]
    else:
        return f"{', '.join(map(str, sequence[:-1]))}, and {sequence[-1]}"


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
    

if __name__ == "__main__":
    main()