import string

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

# A function to move a given letter from the input, both lower and upper


def remove_letter(inp, a):
    return_list = []
    for letter in inp:
        if letter == a.lower() or letter == a.upper():
            pass
        else:
            return_list.append(letter)
    return return_list


#-------Read in the input-----#

text = ""
with open("input.txt", mode="r") as inp:
    for line in inp:
        text = text + line

orig_text = list(text.strip())

###############################

# Main loop:
lowest_count = {"letter": "", "count": len(text)}
for letter in string.ascii_lowercase:
    text = remove_letter(orig_text, letter)
    # print(len(text))
    # print(text)
    # changes = True
    # print("Does this take a long time?")
    # while changes is True:
    # changes = False
    index = 1
    print("Starting Letter {}".format(letter.upper()))
    while index < (len(text) - 2):
        # print("Length: {}".format(len(text)))
        try:
            while check_match(text[index], text[index + 1]) or check_match(text[index - 1], text[index]):
                # print(index)
                if check_match(text[index], text[index + 1]):
                    del text[index]
                    del text[index]
                if check_match(text[index - 1], text[index]):
                    del text[index - 1]
                    del text[index - 1]
                if index >= len(text):
                    break
            index = index + 1
        except IndexError:
            print("Over we go!")
    if len(text) < lowest_count["count"]:
        lowest_count = {"letter": letter, "count": len(text)}
    print("Removing {} gives a length of {}".format(letter.upper(), len(text)))

print("So the lowest letter count is {} with {}!".format(lowest_count["letter"].upper(),
                                                         lowest_count["count"]))
