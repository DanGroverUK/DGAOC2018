fp = "C:/git/DGAOC2018/2017/day2.txt"
lol = []
with open(fp, mode='r') as doc:
    for line in doc:
        # print(line)
        line = line.strip(" \t")
        line = line.split()
        lol.append(line)

tot = 0
for c in lol:
    for a in c:
        for b in c:
            a = int(a)
            b = int(b)
            if a == b:
                break
            if a % b == 0:
                tot = tot + (a / b)
                break
            if b % a == 0:
                tot = tot + (b / a)
                break
print(tot)

# print(total)
# tot = 0
# for a in lst:
#     for b in lst:
#         if a == b:
#             break
#         if a % b == 0:
#             tot = tot + (a / b)
#             break
#         if b % a == 0:
#             tot = tot + (b / a)
#             break
# print(tot)
