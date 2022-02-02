height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = round(weight/height**2, 2)

if a <= 18:
    print(f"BMI is {a}, underweight")
elif a <= 22:
    print(f"BMI is {a}, normal weight")
elif a <= 28:
    print(f"BMI is {a}, slightly overweight")
elif a <= 33:
    print(f"BMI is {a}, obsese")
else:
    print(f"BMI is {a}, clinically obsese")