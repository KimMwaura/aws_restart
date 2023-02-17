userReply = input("Do you need to ship a package? (yes or no ) ")
if userReply == "yes":
    print ("We can help you to ship the package")
else:
    print ("Please comeback when you need to ship a package. Thank You.")

#Working with the elif statement
userReply = input ("Would you like to buy stamp, buy an envelop, or make a copy? (enter stamps, envelop, or copy) ")
if userReply =="stamps":
    print("We have many stamp design to choose from.")
elif userReply == "envelop":
    print ("we have many envelop size to choose from")
elif userReply == "copy":
    copies = input ("how many copies would you like, (Enter a number)" )
    print ("Here are {} copies.".format(copies))
else:
    print("Thank you, please come back again")
    