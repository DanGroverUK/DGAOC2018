import collections
elphie = "C:/git/DGAOC2018/2018/Day_02/input.txt"

input_list = []

with open(elphie, mode="r") as doc:
    for line in doc:
        input_list.append(line)


two_list = 0
three_list = 0
for entry_str in input_list:
    two_done = False
    three_done = False
    new_counter = collections.Counter(entry_str)
    print(new_counter)
    for a in new_counter:
        if new_counter[a] == 2:
            if not two_done:
                two_list = two_list + 1
                two_done = True
        if new_counter[a] == 3:
            if not three_done:
                three_list = three_list + 1
                three_done = True


result = two_list * three_list
print("The result is: {}".format(result))
