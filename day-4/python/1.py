input_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
converted_data = []

# Convert the data into a list of data
for line in input_data.split("\n"):
  converted_line = []

  for letter in line:
    converted_line.append(letter)
  converted_data.append(converted_line)

print(converted_data)

def check_for_letter(letter):
  instructions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1]
  ]
  found_letter = 0

  for instruction in instructions:
    try:
      found_letter += 1 if converted_data[line_index + instruction[0]][letter_index + instruction[1]] == "X" else 0

      if found_letter:
        check_for_letter("M")
    except IndexError:
      pass

times_full = 0
for line_index, line in enumerate(converted_data):
  for letter_index, letter in enumerate(line):
    ...

print(times_full)
