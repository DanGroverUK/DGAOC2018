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
for b in int_imp:
    total = total + b

print(total)
