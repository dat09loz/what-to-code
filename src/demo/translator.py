def translate(phrase):
    translation = ""
    for letter in phrase: 
        if letter.lower() in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print("Result: " + translate(input("Enter a phrase: ")))