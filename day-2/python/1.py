safe_reports = 0
asc_or_desc = ""

def check_level(level):
    for i in range(0, len(level)):
        if i == len(level):
            return "max"

        if level[i] == level[i + 1]:
            return "unsafe"

        if level[i] > level[i + 1] and asc_or_desc == "desc":
            return "unsafe"

        if level[i] < level[i + 1] and asc_or_desc == "asc":
            return "unsafe"

        # 1 20 3 4 5 6
        if asc_or_desc == "asc" and abs(level[i + 1] - level[i]) > 3:
            return "unsafe"

        # 10 20 8 2 6 5
        if asc_or_desc == "desc" and abs(level[i] - level[i + 1]) > 3:
            return "unsafe"

        return "safe"

reports = open("../day-2.input", "r")

for line in reports:
    level_list = line.replace("\n", "").split(" ")
    level_list = list(map(int, level_list))

    asc_or_desc = "asc" if level_list[0] < level_list[1] else "desc"
    print(asc_or_desc)

    if check_level(level_list) == "safe":
        safe_reports += 1
        print(level_list, check_level(level_list))
    elif check_level(level_list) == "unsafe":
        print(level_list, check_level(level_list))
    elif check_level(level_list) == "max":
        pass

print(safe_reports)
