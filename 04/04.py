import math
import typing


def get_diagonals(inputL: list) -> typing.Tuple[dict, dict]:
    rows_len = len(inputL) # INFO: this was so hard 😭
    cols_len = len(inputL[0]) # this is done via by a transversal via a matrix
    left_diagonal_dict = {}
    right_diagonal_dict = {}

    for a in range(rows_len):
        for y in range(cols_len):
            left_key = a - y
            if left_key not in left_diagonal_dict:
                left_diagonal_dict[left_key] = []
            left_diagonal_dict[left_key].append(inputL[a][y])

            right_key = a + y
            if right_key not in right_diagonal_dict:
                right_diagonal_dict[right_key] = []
            right_diagonal_dict[right_key].append(inputL[a][y])

    return left_diagonal_dict, right_diagonal_dict


def solution1(input: str) -> int:
    inputA = [line for line in input.splitlines() if line.strip()]
    rows = inputA[:]
    cols = ["".join([row[i] for row in inputA]) for i in range(len(inputA[0]))]
    matrix = [list(row) for row in inputA]

    left_diagonal_dict, right_diagonal_dict = get_diagonals(matrix)

    search_space = rows + cols
    search_space.extend(["".join(i) for i in left_diagonal_dict.values()])
    search_space.extend(["".join(i) for i in right_diagonal_dict.values()])

    valid_words_to_detect = ["XMAS", "XMAS"[::-1]]
    solution = 0

    for line in search_space:
        solution += sum(line.count(word) for word in valid_words_to_detect)

    return solution


def solution2(input: str) -> int: #  
    inputA = [line for line in input.splitlines() if line.strip()]
    rows = inputA[:]
    cols = ["".join([row[i] for row in inputA]) for i in range(len(inputA[0]))]
    matrix = [list(row) for row in inputA]
    solution = 0 
    correct_letters_dict = {"M", "S"}

    for a in range(1, len(rows) -1):
        for y in range(1, len(cols) -1):
            if matrix[a][y] == "A":
                if {matrix[a - 1][y - 1], matrix[a + 1][y + 1]} == correct_letters_dict and {matrix[a - 1][y + 1], matrix[a + 1][y - 1]} == correct_letters_dict:
                    solution +=1
    return solution

with open("04.txt", "r") as file:
    input_data = file.read()

solution1_ans = solution1(input_data)
print(solution1_ans)
solution2_ans = solution2(input_data)
print(solution2_ans)
