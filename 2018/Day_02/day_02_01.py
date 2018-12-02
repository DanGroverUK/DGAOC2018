elphie = "C:/git/DGAOC2018/2018/Day_02/input.txt"

input_list = []

with open(elphie, mode="r") as doc:
    for line in doc:
        line = line[0:(len(line) - 2)]
        input_list.append(line)


# print(input_list)
two_list = 0
three_list = 0
for entry_str in input_list:
    done2 = False
    done3 = False
    entry = []
    for c in entry_str:
        entry.append(c)
    entry.sort()
    for letter in range(0, (len(entry) - 1)):
        try:
            if entry[letter] == entry[letter + 1]:
                if entry[letter] == entry[letter + 2]:
                    if entry[letter] == entry[letter + 3]:
                        pass
                    else:
                        if not done3:
                            three_list = three_list + 1
                            done3 = True
                else:
                    if not done2:
                        two_list = two_list + 1
                        done2 = True
        except IndexError:
            pass

        # if letter in lol:
        #     index = lol.index(letter)
        #     lol.pop(index)
        #     # if it's STILL in there:
        #     if letter in lol:
        #         three_list = three_list + 1
        #     else:
        #         two_list = two_list + 1
        #     lol.insert(index, letter)
        # lol.append(letter)

result = two_list * three_list
print("The result is: {}".format(result))