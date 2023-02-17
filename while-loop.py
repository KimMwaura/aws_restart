import random 

print("Welcome geuss the Number! ")
print("The rules are simple. I will think of a number and you will try to geuss it, ")

number = random.randint(1, 10)
isGeussRight = False
while isGeussRight != True:
    geuss = input ("Geuss a number 1 and 10 ")
    if int(geuss) == number:
        print("you geussed {}. That is correct. You win!".format(geuss))
        isGeussRight == True
    else:
        print("You geussed {}. Sorry, that isn't it. Try again".format(geuss))
        
#Writing pseudocode
