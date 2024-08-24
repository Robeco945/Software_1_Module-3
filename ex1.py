print("Exercise 1")

size = int(input("enter size of the zander: "))
dif = 42 - size
if dif <= 0:
    print("the zander fulfills the size limit")
else:
    print("your zander is " + str(dif), "cm below the size limit")