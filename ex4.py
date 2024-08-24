print("exercise 4")
year = int(input("enter a year: "))
if year == 0:
    print("your year is not a gap year")
elif year % 100 == 0 and year % 400 == 0:
    print("your year is a gap year")
elif year % 4 == 0:
    print("your year is a gap year")
else:
    print("your year is not a gap year")