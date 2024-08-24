print("exercise 3")
gender = input("enter your biological gender: ")
hem = int(input("enter your hemoglobin value(g/l): "))
if gender == "male" and 134 <= hem <= 167:
    print("you have normal hemoglobin levels")
if gender == "male" and 134 > hem:
    print("you have low hemoglobin levels")
if gender == "male" and hem > 167:
    print("you have high hemoglobin levels")
if gender == "female" and 117 <= hem <= 155:
    print("you have normal hemoglobin levels")
if gender == "female" and 117 > hem:
    print("you have low hemoglobin levels")
if gender == "female" and hem > 155:
    print("you have normal hemoglobin levels")