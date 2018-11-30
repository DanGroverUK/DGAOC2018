# import itertools
# fp = "C:/git/DGAOC2018/2017/day2.txt"
# lol = []
# with open(fp, mode='r') as doc:
#     for line in doc:
#         # print(line)
#         line = line.strip(" \t")
#         line = line.split()
#         lol.append(line)

# total = 0
# for a in lol:
#     lowest = 9999
#     highest = 0
#     for num in a:
#         num = int(num)
#         if num > highest:
#             highest = num
#         if num < lowest:
#             lowest = num
#     print("Total: {}\nHighest: {}\nLowest: {}\n".format(total, highest, lowest))
#     total = total + (highest - lowest)

# print(total)
tot = 0
lst = [9, 4, 7, 3]
for a in lst:
    for b in lst:
        if a == b:
            break
        if a % b == 0:
            tot = tot + (a / b)
            break
        if b % a == 0:
            tot = tot + (b / a)
            break
print(tot)
