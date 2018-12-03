def flip_and_add(val):
    if val > 0:
        return ((val) * -1)
    else:
        return ((val - 1) * -1)


entries = [[0]]
hold = 1
tip = 1
a = 0
fv = 0
height = 50
while a < (height - 1):
    while fv != tip:
        if tip > 0:
            fv = fv + 1
            entries.append([fv])
            a = a + 1
        if tip < 0:
            fv = fv - 1
            a = a + 1
            entries.append([fv])
    while fv == tip:
        for b in range(1, hold):
            entries.append([fv])
        hold = hold + 1
        if tip < 0:
            fv = fv - 1
        if tip > 0:
            fv = fv + 1
        if tip == 0:
            fv = fv + 1
    tip = flip_and_add(tip)


hold = 2
entries[0].append(0)
tip = 0
a = 1
fv = 0

while a < (height - 1):
    while fv != tip:
        if tip > 0:
            fv = fv + 1
            entries[a].append(fv)
            a = a + 1
        if tip < 0:
            fv = fv - 1
            entries[a].append(fv)
            a = a + 1
    while fv == tip:
        for b in range(1, hold):
            print("HOLD ADD! {}".format(fv))
            entries[a].append(fv)
            a = a + 1
        hold = hold + 1
        if tip < 0:
            fv = fv - 1
        if tip > 0:
            fv = fv + 1
        if tip == 0:
            fv = 1
    tip = flip_and_add(tip)

counter = 1
for a in entries:
    print("{}: {} and {}".format(counter, a[0], a[1]))
    counter = counter + 1