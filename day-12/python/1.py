data = """AAAA
BBCB
BBCC
EEEC"""
data = data.split("\n")
for index, line in enumerate(data):
  data[index] = list(line)

def get_surrounding_plants(plant_type):
  indicies = []
  for line_index, line in enumerate(data):
    for char_index, char in enumerate(line):
      if char == plant_type:
        indicies.append((char_index, line_index))

  print("All the indicies of plant type: ", indicies)

print(data)
get_surrounding_plants("B")
