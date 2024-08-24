print("exercise 2")
cabin_class = input("enter your cabin class: ")
if cabin_class == "LUX":
    print("you have an upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("you have an above the car deck, equipped with a window")
elif cabin_class == "B":
    print("you have a windowless cabin above the car deck")
elif cabin_class == "C":
    print("you have a windowless cabin below the car deck")
else:
    print("Error: invalid cabin class")
