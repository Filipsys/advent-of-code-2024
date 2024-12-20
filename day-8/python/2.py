data = open("../day-8.input", "r").read()
data = data.split("\n")

possible_antenas = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
antennas_positions = []
antinodes_positions = set()

def get_distance_from_two_antenas(a, b):
  return {
    "x": a[0] - b[0], 
    "y": a[1] - b[1]
  }

# Find all the antenas
for line_index, line in enumerate(data):
  for char_index, char in enumerate(line):
    if char in possible_antenas:
      antennas_positions.append((char_index, line_index, char))

# Temporarily turn the data into a list
for index, line in enumerate(data):
  data[index] = list(line)

for index_antenna, antenna in enumerate(antennas_positions):  
  for index_other_antenna, other_antenna in enumerate(antennas_positions):
    if index_antenna == index_other_antenna:
      continue

    distances = get_distance_from_two_antenas(
      antennas_positions[index_antenna], 
      antennas_positions[index_other_antenna]
      )
    dist_x, dist_y = distances["x"], distances["y"]
    new_x = other_antenna[0] - dist_x
    new_y = other_antenna[1] - dist_y
    
    if antennas_positions[index_antenna][2] == antennas_positions[index_other_antenna][2]:
      while 0 <= new_x < len(data[0]) and 0 <= new_y < len(data):
        if (new_x, new_y) not in antinodes_positions:
          antinodes_positions.add((new_x, new_y))
        
          data[new_y][new_x] = "#"
        new_x = new_x - dist_x
        new_y = new_y - dist_y

# Print the output (optional)
for line in data:
  print("".join(line))

# Count the antinodes
total_positions = set()
for antinode in antinodes_positions:
  total_positions.add(antinode)
for antenna in antennas_positions:
  total_positions.add(antenna[:-1])

print("Antinodes amount: ", len(total_positions))