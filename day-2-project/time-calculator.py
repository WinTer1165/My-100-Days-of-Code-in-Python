age = input("What is your current age?")

age_int = int(age)

x = age_int
y = age_int
z = age_int

p = 90*12
q = 90*365
r = 90*365/7

a = p-(x*12)
b = q-(y*365)
c = int(r-(z*365/7))

print(f"You have {b} days, {c} weeks, and {a} months left.")