year = int(input("Which year do you want to check? "))
a = year

if a % 4:
    print()
elif a % 100:
    print("This is a leap year")
elif a % 400:
    print("This is not a leap year")
else:
    print("This is a leap year.")
