import collections

input_list = []

fp = "C:/git/DGAOC2018/2018/Day_04/input.txt"
with open(fp, mode='r') as imp:
    for line in imp:
        new_data = {}
        new_data["month"] = int(line[6:8])
        new_data["day"] = int(line[9:11])
        new_data["hour"] = int(line[12:14])
        new_data["minute"] = int(line[15:17])
        new_data["sortable"] = (
            line[6:8] +
            line[9:11] +
            line[12:14] +
            line[15:17])
        new_data["string"] = line[19:].strip()
        input_list.append(new_data)

sorted_list = sorted(input_list, key=lambda k: k["sortable"])
minutes_asleep = []
a = 0
# Cycle through the sorted list
while a < (len(sorted_list) - 3):
    # Make a new dict for a new guard
    data = {"id": "", "minutes": []}
    # Check to see if the guard's already got a record, though
    for w in minutes_asleep:
        if w["id"] == sorted_list[a]["string"][7:-13]:
            # And if it does, grab its record and remove it from the
            # list so that we can put it back in without duplicates
            data = w
            minutes_asleep.remove(w)
    # Now we need to check if the guard fell asleep at all
    if sorted_list[a + 1]["string"][0] == "G":
        # This means they didn't fall asleep. As such, we need to
        # Pop that element back in if it's not empty
        if data["id"] != "":
            minutes_asleep.append(data)
        a = a + 1
    else:
        # Here's where we actually add the right data
        sleep_time = sorted_list[a + 1]["minute"]
        wake_time = sorted_list[a + 2]["minute"]
        data["id"] = sorted_list[a]["string"][7:-13]
        # Add each minute into the 'minutes' array for this guard
        # This will enable us to easily count how many minutes they're
        # asleep for in total, and which minute they're asleep during
        # most frequently
        for m in range(sleep_time, wake_time):
            data["minutes"].append(m)
        # Now we check if the guard fell asleep more than once. I don't think
        # They ever fall asleep more than twice.
        while sorted_list[a + 3]["string"][0] != "G":
            sleep_time = sorted_list[a + 3]["minute"]
            wake_time = sorted_list[a + 4]["minute"]
            for m in range(sleep_time, wake_time):
                data["minutes"].append(m)
            # This is to allow for us arriving at the end of the array
            if a > (len(sorted_list) - 6):
                break
            else:
                a = a + 2
        # Now we pop it back into the list and increment the counter by 3
        # because we know the next two are sleep and wake descriptions
        minutes_asleep.append(data)
        a = a + 3

# Now we have a list featuring one dict per guard, detailing the exact minutes that they
# fall asleep in total - from this we can get both the length of time they're asleep and
# the minute they do so most frequently.

highest_minutes = 0
winner_winner_chicken_dinner = 0
for i in minutes_asleep:
    # Find the #1 most common minute for this person to be asleep during
    mc = collections.Counter(i["minutes"]).most_common(1)
    # from this we can also get how many times they are
    which_minute = mc[0][0]
    most_common = mc[0][1]
    # Compare that to the current highest
    if most_common > highest_minutes:
        # if it's the new highest, set this value as the highest
        highest_minutes = most_common
        # Also set the winning variable to be the answer we need
        winner_winner_chicken_dinner = int(i["id"]) * which_minute

print("Result: {}".format(winner_winner_chicken_dinner))

