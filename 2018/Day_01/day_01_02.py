int_imp = []

fp = "C:/git/DGAOC2018/2018/Day_01/input.txt"
with open(fp, mode='r') as doc:
    for line in doc:
        int_imp.append(int(line))

total = 0
index = 0
all_totals = [0]

while index < len(int_imp):
    total = total + int_imp[index]
    if total in all_totals:
        print(total)
        break
    all_totals.append(total)
    index = index + 1
    if index == len(int_imp):
        index = 0
    if (len(all_totals) % 10000) == 0:
        print(len(all_totals))
