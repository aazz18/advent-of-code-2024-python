# https://adventofcode.com/2024/day/1 

def solution1(input: str) -> int: # 
    num1L = []
    num2L = []
    inputL = input.splitlines() 
    
    for line in inputL: 
        linesP = line.split() 
        num1L.append(int(linesP[0]))
        num2L.append(int(linesP[1]))
    
    num1L.sort()
    num2L.sort()
    
    totalDistance = 0
    for i in range(len(num1L)):  
        totalDistance += abs(num1L[i] - num2L[i])
    
    return totalDistance

def solution2(input:str) -> int:
    num1L = []
    num2L = []
    inputL = input.splitlines() 
    
    for line in inputL: 
        linesP = line.split() 
        num1L.append(int(linesP[0]))
        num2L.append(int(linesP[1]))  # copied from solution 1
    num1L.sort()
    num2L.sort()

    similarity_score_totalL = []
    for i in num2L:
        num_time_in_L1 = num1L.count(i)
        similarity_score = i * num_time_in_L1
        similarity_score_totalL.append(similarity_score)
    
    return sum(similarity_score_totalL)

        

    

with open("01.txt", "r") as file:
    input_data = file.read()

solution1_ans = solution1(input_data)
print(solution1_ans)
solution2_ans = solution2(input_data)
print(solution2_ans)