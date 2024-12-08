data = """190: 10 19 1"""
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
data = data.split("\n")

def mult(a, b):
    return a * b

def add(a, b):
    return a + b

for line in data:
    result, numbers_string = line.split(": ")
    numbers_list = numbers_string.split(" ")
    
    # loop through list to turn strings into ints
    for index, value in enumerate(numbers_list):
        numbers_list[index] = int(value)
    
    possible_equations = len(numbers_list) - 1
    
    sum_of_correct_values = 0
    line_result = 0
    from_index = 0
    for index, value in enumerate(numbers_list):
        if index == len(numbers_list) - 1:
            print("Last element of list")
            continue
        
        for i in range(from_index, len(numbers_list)):
            if i == len(numbers_list) - 1:
                continue
            
            line_result += add(numbers_list[i], numbers_list[i + 1])
        print(line_result)
            
        from_index += 1
        
        # This is for two values only
        # if int(value * numbers_list[index + 1]) == int(result):
        #     sum_of_correct_values += value * numbers_list[index + 1]
        
        # if int(value + numbers_list[index + 1]) == int(result):
        #     sum_of_correct_values += value + numbers_list[index + 1]
    
    # print(sum_of_correct_values)