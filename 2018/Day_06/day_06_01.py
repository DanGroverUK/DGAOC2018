#-------Read in the input-----#

input_pairs = []
with open("input.txt", mode="r") as inp:
    for line in inp:
        # print(line)
        a, b = line.split(",")
        input_pairs.append([int(a), int(b.strip())])


###############################
# Highest X: 359
# Highest Y: 351

# Main loop:

print(input_pairs)
