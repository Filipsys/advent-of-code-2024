left_list = []
right_list = []
similarity_sum = 0

data = open("../day-1.input", "r")

for line in data:
    left, right = line.split()

    left_list.append(int(left))
    right_list.append(int(right))

data.close()

for i in range(len(left_list)):
    times_found = 0

    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            times_found += 1

    similarity_sum += left_list[i] * times_found

print(similarity_sum)