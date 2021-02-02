#*while loop
i = 1
while i <= 10: 
    print(i)
    i += 1
# increment by 1 in Python is += 1 instead of ++i, same with decrement
print ("Loop is done!")
print()


#*for loop
array = ["K", "F", "Y", "R"]
for letter in array:
    print(letter)
print()


#prints from 0 to 9, does not print 10. Or (3, 10), which loop from 3 to 9
for index in range(3, 10): 
    print(index)
print()

#print by array index
array = ["K", "F", "Y", "R", "T"]
for index in range(len(array)):
    print(array[index])


# *nested for-loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for column in row:
        print(column)
