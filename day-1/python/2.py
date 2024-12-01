left_list = []
right_list = []
similarity_sum = 0

data = open("../input-1.txt", "r")

for line in data:
    left, right = line.split()

    left_list.append(int(left))
    right_list.append(int(right))

data.close()

for i in range(len(left_list)):
    timesFound = 0

    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            timesFound += 1

    similarity_sum += left_list[i] * timesFound

print(similarity_sum)