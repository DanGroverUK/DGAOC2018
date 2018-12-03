fp = "C:/git/DGAOC2018/2018/Day_03/input.txt"
input_list = []
total_width = 0
total_height = 0
with open(fp, mode="r") as inp:
    for line in inp:
        # This is all string conversion stuff - converting
        # the strings from the input into usable integers in
        # the a dict.
        first_half, second_half = line.split("@")
        id_val = first_half[1:(len(first_half) - 1)]
        id_val = id_val[0:(len(first_half) - 2)]
        # print("ID: {}".format(id_val))
        loc, dim = second_half.split()
        left, top = loc.split(",")
        top = top.split(":")[0]
        width, height = dim.split("x")
        data_dict = {
            "id": int(id_val),
            "left": int(left),
            "top": int(top),
            "width": int(width),
            "height": int(height)
        }
        input_list.append(data_dict)
        # whilst we're here, I'll also use this opportunity
        # to calculate the highest required width and height
        # of the fabric
        if (data_dict["left"] + data_dict["height"]) > total_width:
            total_width = data_dict["left"] + data_dict["height"]
        if (data_dict["top"] + data_dict["height"]) > total_height:
            total_height = (data_dict["top"] + data_dict["height"])

total_list = []
for h in range(0, total_height):
    width_list = []
    for w in range(0, total_width):
        width_list.append([])
    total_list.append(width_list)

for entry in input_list:
    for h in range(entry["top"], (entry["top"] + entry["height"])):
        for w in range(entry["left"], (entry["left"] + entry["width"])):
            total_list[h][w].append(entry["id"])

for entry in input_list:
    entry["overlap"] = False
    for h in range(entry["top"], (entry["top"] + entry["height"])):
        for w in range(entry["left"], (entry["left"] + entry["width"])):
            if len(total_list[h][w]) > 1:
                entry["overlap"] = True
    if entry["overlap"] is False:
        print(entry["id"])
