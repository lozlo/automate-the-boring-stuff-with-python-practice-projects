# character_picture_grid.py
# This program rotates a grid 90 degrees clockwise and prints the result.

# def turn_grid_90_degrees(arr):
#     for i in range(len(arr[0])):
#         for j in range(len(arr)):
#             print(arr[j][i], end='')
#         print()


# def main():
    # grid = [['.', '.', '.', '.', '.', '.'],
    #         ['.', 'O', 'O', '.', '.', '.'],
    #         ['O', 'O', 'O', 'O', '.', '.'],
    #         ['O', 'O', 'O', 'O', 'O', '.'],
    #         ['.', 'O', 'O', 'O', 'O', 'O'],
    #         ['O', 'O', 'O', 'O', 'O', '.'],
    #         ['O', 'O', 'O', 'O', '.', '.'],
    #         ['.', 'O', 'O', '.', '.', '.'],
    #         ['.', '.', '.', '.', '.', '.']]
    
#     turn_grid_90_degrees(grid)


# if __name__ == "__main__":
#     main()


# Refactored to improve readability and maintainability


def turn_grid_90_degrees(grid):
    return [''.join(row) for row in zip(*grid[::-1])]


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    
    rotated_grid = turn_grid_90_degrees(grid)
    print(*rotated_grid, sep='\n')

if __name__ == "__main__":
    main()
