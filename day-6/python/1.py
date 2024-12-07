data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
data = data.split("\n")
row_length = len(data[0])
column_length = len(data)

guard_location = (0, 0) # x & y
guard_direction = "N"

movement_dict = {
  "N": (0, -1),
  "E": (1, 0),
  "S": (0, 1),
  "W": (-1, 0)
}

direction_cursor_dict = {
  "N": "^",
  "E": ">",
  "S": "V",
  "W": "<"
}

def rotate_direction():
  if guard_direction == "N":
    guard_direction = "E"
  elif guard_direction == "E":
    guard_direction = "S"
  elif guard_direction == "S":
    guard_direction = "W"
  elif guard_direction == "W":
    guard_direction = "N"
  
  data[guard_location[1]][guard_location[0]] = direction_cursor_dict[guard_direction]

def check_guard_direction(data_char):
  if data_char == "^":
    return "N"
  elif data_char == ">":
    return "E"
  elif data_char == "V":
    return "S"
  elif data_char == "<":
    return "W"
  else:
    return ValueError

def check_if_guard_path_blocked(x, y):
  print("===")
  print("Guard location: ", x, y)
  print("North of guard: ", data[y - 1][x] )
  print("East of guard: ", data[y][x + 1] )
  print("South of guard: ", data[y + 1][x] )
  print("West of guard: ", data[y][x - 1] )
  
  if (data[y + movement_dict[guard_direction][1]][x] == "#" or
      data[y][x + movement_dict[guard_direction][0]] == "#"):
    print("Blocked")
    rotate_direction()
  else:
    print("Clear, moving on")

def move_forward(guard_location):
  x, y = guard_location
  
  check_if_guard_path_blocked(x, y)
  
  if (guard_location[0] + movement_dict[guard_direction][0] < 0 or 
      guard_location[0] + movement_dict[guard_direction][0] > row_length):
    raise IndexError
  
  if (guard_location[1] + movement_dict[guard_direction][1] < 0 or
      guard_location[1] + movement_dict[guard_direction][1] > column_length):
    raise IndexError
  
  # print("Changing")
  # print("Current location: ", x, y)
  # print("Directions: ", movement_dict[guard_direction][0], movement_dict[guard_direction][1])
  # print("New location: ", x + movement_dict[guard_direction][0], y + movement_dict[guard_direction][1])
  return (x + movement_dict[guard_direction][0], y + movement_dict[guard_direction][1])

# Find the guard initial location
for data_line_index, data_line in enumerate(data):
  for data_char_index, data_char in enumerate(data_line):
    if data_char == "^":
      guard_location = (data_char_index + 1, data_line_index + 1)
      guard_direction = check_guard_direction(data_char)
      print("Found guard")
      print(guard_location, guard_direction)
      
      check_if_guard_path_blocked(data_char_index + 1, data_line_index + 1)

running = True
while running:
  try:
    guard_location = move_forward(guard_location)
    print("Guard location: ", guard_location)
  except IndexError:
    running = False
    print("Out of bounds")