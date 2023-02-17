#Introducing the string data type
myString = "This is a String."
print(myString)
print(type(myString))
print(str(myString) + " is of data type " + str(type(myString)))

#Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Working with input strings
name = input ("What is your name")
print(name)

#Formatting output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
