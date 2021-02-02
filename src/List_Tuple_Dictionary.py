
#*LIST BASIC

friends = ["R", "T", "K", "O", "B"]
print(friends[0] + " fucks " + friends[2] + " in front of " + friends[1])
print(friends[-2])  # print the element count from the end of the list 
                    # -1 is the first element start from the end (equivalent to 0 is the initial element in the list), in this case is B.

print(friends[2:])  # run from the element with the index number to the right of the list
print(friends[1:3])  # grab the 1 and 2, but not 3 (strange)

friends[1] = "dead"
print(friends)
print()

#* LIST FUNCTIONS

# friends = ["R", "T", "K", "O", "B"]
lucky_nums = [4, 567, 3, 46, 76, 6, 7, 86, 435, 523, 745, 156]
print("")
friends.extend(lucky_nums)  # include another list at the end of the list
print(friends)

friends.append("E")  # include a new element at the end of the list
print(friends)

friends.insert(1, "insert here")  # insert an item inside the list (position, element)
print(friends)

friends.remove("insert here") # remove an element in the list
print(friends)


# *friends.clear() : delete EVERYTHING
# []


friends.pop() # get rid (pop) an item at the very end out of the list
print(friends)

print(friends.index("dead")) # find an element in the list and show the exact position of that element

friends.append("dead")
friends.insert(4, "dead")
print(friends.count('dead')) # count the number of elements exist in the list (3)

lucky_nums.sort()
print(lucky_nums) # sort the list in alphabetical/numeric order

lucky_nums = [4, 567, 3, 46, 76, 6, 7, 86, 435, 523, 745, 156]
print(lucky_nums)
lucky_nums.reverse() # reverse the order of the list (NOT in alphabetical/numeric order)
print(lucky_nums)

friends2 = friends.copy() # make a copy of a existing list into the new list
print(friends2)
print()


# *this is tuple : immutable
# (tuple) vs [list]
coordinates = (335, 574)
print(coordinates[0])
print()


# *{dictionary}
# key: value 
# stores different types of data
monthConversion = {
    "Jan": "January",
    "Feb": "Febrary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion.get("Dec"))
print(monthConversion.get("Aug"))
print()


#*2D List (lists in a list)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])
print(number_grid[1][0])
print()

# *nested for-loop
for row in number_grid:
    for column in row:
        print(column)