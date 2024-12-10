data = """..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
.........."""
data = data.split("\n")

possible_antenas = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
antennas_positions = []

# Find all the antenas
for line_index, line in enumerate(data):
  for char_index, char in enumerate(line):
    if char in possible_antenas:
      antennas_positions.append((char_index, line_index))

print(antennas_positions)

def get_distance_from_two_antenas(a, b):
  return {
    "x": abs(a[0] - b[0]), 
    "y": abs(a[1] - b[1])
  }



# Temporarily turn the data into a list
for index, line in enumerate(data):
  data[index] = list(line)

for index_antenna, antenna in enumerate(antennas_positions):
  if index_antenna == len(antennas_positions) - 1:
    continue

  distances = get_distance_from_two_antenas(antennas_positions[index_antenna], antennas_positions[index_antenna + 1])
  dist_x, dist_y = distances["x"], distances["y"]
  print(dist_x, dist_y)

  try:
    data[antennas_positions[index_antenna][1] - dist_y][antennas_positions[index_antenna][0] - dist_x] = "#"
  except IndexError:
    print("Out of bounds")

  try:
    data[antennas_positions[index_antenna + 1][1] + dist_y][antennas_positions[index_antenna + 1][0] + dist_x] = "#"
  except IndexError:
    print("Out of bounds")



for line in data:
  print("".join(line))
