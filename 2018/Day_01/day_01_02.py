int_imp = []

fp = "C:/git/DGAOC2018/2018/Day_01/input.txt"
with open(fp, mode='r') as doc:
    for line in doc:
        int_imp.append(int(line))

total = 0
index = 0
all_totals_set = set()
all_totals_set.add(0)

while index < len(int_imp):
    total = total + int_imp[index]
    cur_total = len(all_totals_set)
    all_totals_se
    t.add(total)
    if len(all_totals_set) != (cur_total + 1):
        print(total)
        break
    index = index + 1
    if index == len(int_imp):
        index = 0

