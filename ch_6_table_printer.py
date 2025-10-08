# ch_6_table_printer.py
# A table printer program. that takes a list of lists of strings and displays it
# in a well-organized table with each column right-justified. Assume that all inner
# lists will contain the same number of strings.

# def print_table(table):
#     number_of_rows = len(table)
#     col_widths = [0] * number_of_rows

#     for idx in range(len(table)):
#         for idy in table[idx]:
#             col_widths[idx] = max(col_widths[idx], len(idy))

#     for idx in range(len(table[0])):
#         for idy in range(len(table)):
#             print(table[idy][idx].rjust(col_widths[idy]), end=' ')
#         print()


# def main():
#     table_data = [
#         ['apples', 'oranges', 'cherries', 'banana'],
#         ['Alice', 'Bob', 'Carol', 'David'],
#         ['dogs', 'cats', 'moose', 'goose']
#     ]

#     print_table(table_data)


# if __name__ == "__main__":
#     main()

# Refactored to improve readability and maintainability

def print_table(table):
    col_widths = [max(len(item) for item in row) for row in table]

    num_cols = len(table[0])
    num_rows = len(table)

    for col_idx in range(num_cols):
        for row_idx in range(num_rows):
            print(table[row_idx][col_idx].rjust(col_widths[row_idx]), end=' ')
        print()


def main():
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    print_table(table_data)


if __name__ == "__main__":
    main()


