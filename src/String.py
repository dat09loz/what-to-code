phrase = "what the fuck is going on"

print(phrase + " here?") #print the instance with something

print(phrase.upper().isupper()) #convert the string to upper case and check if it is true

print(phrase.lower().islower()) #convert the string to lower case and check if it is true

print(len(phrase)) #count the length of the string (including space)

print(phrase[5]) #give the element which the index number has assigned to in the string

print(phrase.index("o")) #give the index number of a given element in the string (will output the index number of the first "o" in the phrase)

print(phrase.index("fuck")) #give the index number of the first element in the inputted phrase

print(phrase.replace("fuck", "frick")) #replace the element on the left to the one on the right
