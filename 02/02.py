def check_if_level_is_safe(level: list) -> bool:
    differance = [x - y for x, y in zip(level, level[1:])]
    is_ascending_or_not =  all(d > 0 for d in differance) or all(d < 0 for d in differance)
    if not is_ascending_or_not:
        return False
    temp_val = level[0]
    for i in level[1:]:
        if not (0 <= abs(i - temp_val) <= 3):
            return False
        temp_val = i
    return True

def solution1(input:str) -> int:
    inputL = input.splitlines()
    safe_reports = 0

    for reports_S in inputL:
        levels_L = [*map(int, reports_S.split())]
        is_safe = check_if_level_is_safe(levels_L)
        if check_if_level_is_safe(levels_L):
            safe_reports +=1
    return safe_reports

def solution2(input:str) -> int:
    inputL = input.splitlines()
    safe_reports = 0

    for reports_S in inputL:
        levels_L = [*map(int, reports_S.split())]
        is_safe = check_if_level_is_safe(levels_L)
        if check_if_level_is_safe(levels_L):
            safe_reports +=1
        else:
            for x in range(0, len(levels_L)):
                allowed_levels = levels_L[:x] + levels_L[x + 1:]
                if check_if_level_is_safe(allowed_levels) == True:
                    safe_reports +=1
                    break
    return safe_reports


with open("02.txt", "r") as file:
    input_data = file.read()
solution1_ans = solution1(input_data)
print("Ans 1:", str(solution1_ans))
solution2_ans = solution2(input_data)
print("Ans 2:", str(solution2_ans))