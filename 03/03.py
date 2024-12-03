#https://adventofcode.com/2024/day/3

import re


def solution1(input: str) -> int:
    solution = 0
    valid_mul_regex = r'mul\((\d{1,3}),(\d{1,3})\)'
    found_muls_list = re.findall(valid_mul_regex, input)
    for i in found_muls_list:
        num1 = int(i[0])
        num2 = int(i[1])
        solution += (num1*num2)
    return solution

def solution2(input: str) -> int:
    solution = 0
    do = True
    valid_mul_regex = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    found_muls_list = re.findall(valid_mul_regex, "".join(input))
    for i in found_muls_list:
        if i[0] == "do()":
            do = True
        elif i[0] == "don't()":
            do = False
        elif i[0] and i[1] and i[2] and do:
            num1 = int(i[1])
            num2 = int(i[2])
            solution += int(num1) * int(num2)
        else:
            pass
    return solution

with open("03.txt", "r") as file:
    input_data = file.read()

solution1_ans = solution1(input_data)
print(solution1_ans)
solution2_ans = solution2(input_data)
print(solution2_ans)
