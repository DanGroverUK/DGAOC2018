import collections


def compare_strings(str1, str2):
    error_count = 0
    for b in range(0, (len(str1) - 1)):
        # print("{} vs {}".format(str1[b], str2[b]))
        if str1[b] != str2[b]:
            if error_count == 1:
                return False
            error_count = 1
        # if b == (len(str1) - 1):
    return True

def diff(str1, str2):
    print("{} vs {}".format(str1, str2))
    str1 = list(str1)
    str2 = list(str2)
    for d in range(0, (len(str1) - 1)):
        if str1[d] == str2[d]:
            pass
        else:
            str1.pop(d)
            return str1


elphie = "C:/git/DGAOC2018/2018/Day_02/input.txt"

input_list = []

with open(elphie, mode="r") as doc:
    for line in doc:
        input_list.append(line)

for a in range(0, (len(input_list) - 1)):
    for c in range(0, (len(input_list) - 1)):
        if a == c:
            break
        str1 = input_list[a]
        str2 = input_list[c]
        if compare_strings(str1, str2):
            difference = diff(str1, str2)
            break

answer = ""
for e in difference:
    if e != "\n":
        answer = answer + e
print(answer)
