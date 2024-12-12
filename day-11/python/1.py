data = "0 1 1000 99 999"
blink_amount = 25
current_blinks = 0
# data = data.split("\n")
data = data.split(" ")

# while current_blinks <= 25:
new_data = data.copy()

additional_elements = 1
for index, number in enumerate(data):
    if int(number) == 0:
        new_data[index] = 1

    # Make 1000 -> 10 & 0
    elif len(str(number)) % 2 == 0:
        middle = len(number) / 2
        left, right = str(number[:int(middle)]), str(number[int(middle):])

        new_data.pop(index)
        new_data.insert(index, left)
        new_data.insert(index + additional_elements, right)
        additional_elements += 1
    else:
        new_data[index] = int(number) * 2024
    
print(new_data)
# data = new_data

temp = ""
for element in new_data:
    temp += str(element) + " "

print(temp)