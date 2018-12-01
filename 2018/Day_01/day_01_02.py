imp = []

fp = "C:/git/DGAOC2018/2018/Day_01/input.txt"
with open(fp, mode='r') as doc:
    for line in doc:
        imp.append(line)

# imp = ["-1", "-1", "-1"]
int_imp = []
for a in imp:
    int_imp.append(int(a))

total = 0
all_totals = [0]
index = 0
while index < len(int_imp):
    total = total + int_imp[index]
    if total in all_totals:
        print(total)
        break
    all_totals.append(total)
    # print(all_totals)
    index = index + 1
    if index == len(int_imp):
        index = 0
    if (len(all_totals) % 10000) == 0:
        print(len(all_totals))





# print(total)
