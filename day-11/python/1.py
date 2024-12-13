data = "1117 0 8 21078 2389032 142881 93 385"
data = data.split(" ")
blink_amount = 25
current_blinks = 0

while current_blinks < blink_amount:
    new_data = data.copy()

    additional_elements = 0
    for index, number in enumerate(data):
        if int(number) == 0:
            new_data[index + additional_elements] = 1

        elif len(str(number)) % 2 == 0:
            middle = len(str(number)) / 2
            left, right = str(number)[:int(middle)], str(number)[int(middle):]
            insert_elements = [int(left), int(right)]
            
            new_data[index + additional_elements:index + 1 + additional_elements] = insert_elements
            additional_elements += 1
        else:
            new_data[index + additional_elements] = int(number) * 2024
    
    data = new_data
    current_blinks += 1
    
temp = ""
for element in data:
    temp += str(element) + " "

print(temp)
print("---")
print(len(data))