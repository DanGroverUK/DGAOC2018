# A function that takes two values, checks if the first is lower or upper, then
# finds out if it inverse-matches the value and case of the second


def check_match(a, b):
    if a.lower() == a:
        if a.upper() == b:
            return True
        else:
            return False
    if a.upper() == a:
        if a.lower() == b:
            return True
        else:
            return False


#-------Read in the input-----#

text = ""
with open("input.txt", mode="r") as inp:
    for line in inp:
        text = text + line

text = list(text.strip())

###############################

# Main loop:

changes = True
while changes is True:
    changes = False
    index = 0
    while index < (len(text) - 2):
        if check_match(text[index], text[index + 1]):
            del text[index]
            del text[index]
            changes = True
        else:
            index = index + 1

print("The answer is: {}".format(len(text)))
