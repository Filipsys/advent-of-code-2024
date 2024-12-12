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
  
  print(f"All the indicies of plant type {plant_type}: {indicies}")

  # Check for islands
  islands = {}
  for index_1, loop_element_1 in enumerate(indicies):
    for index_2, loop_element_2 in enumerate(indicies):
      if loop_element_1 == loop_element_2:
        continue
      
      if (abs(loop_element_1[0] - loop_element_2[0]) > 1 or
          abs(loop_element_1[1] - loop_element_2[1]) > 1):
        continue

      if index_2 == len(data[0]) - 1 or index_1 == len(data) - 1:
        continue

      # Check if island already exists
      print(islands.get(data[index_1][index_2]))
      if islands.get(data[index_1][index_2]) is None:
        islands[data[index_1][index_2]] = [(index_1, loop_element_1[0]), (index_2, loop_element_2[0])]
      else:
        islands[data[index_1][index_2]] = [(index_1, loop_element_1[0]), (index_2, loop_element_2[0])]

print(data)
get_surrounding_plants("B")