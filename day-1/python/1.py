left_list = []
right_list = []
diff_sum = 0

data = open("../input-1.txt", "r")

for line in data:
    left, right = line.split()

    left_list.append(int(left))
    right_list.append(int(right))

data.close()

for i in range(len(left_list)):
    diff_sum += abs(left_list[i] - right_list[i])

print(diff_sum)