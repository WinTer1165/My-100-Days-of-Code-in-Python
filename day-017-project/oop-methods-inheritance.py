
# ? parent class

class Bird:

    # * class attribute
    species = "bird"

    # * instance attribute
    def __init__(self, name, age):
        #! from blu = Parrot("Blu", 10)
        #!blu.name = Blu
        #!blu.age = 10
        print(f"{name} is ready.")
        self.name = name
        self.age = age

    # * instance method

    def whoisThis(self):
        return f"{self.name} is a bird."

    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"


# ? child class
class Parrot(Bird):

    def __init__(self, name):
        self.name = name
        print(f"{name} is ready")

    def whoisThis(self):
        print("Parrot")

    def run(self):
        return f"{self.name} run faster"


#! instantiate the Parrot class
blu = Bird("Blu", 10)
woo = Bird("Woo", 15)

#! access the class attributes
print(f"Blu is a {blu.species}")
print(f"Woo is also a {woo.species}")

#! access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")

#! call our instance methods
print(blu.sing("'Happy'"))
print(woo.dance())

#! Use of Inheritance
print(blu.whoisThis())
rio = Parrot("Rio")
rio.whoisThis()
print(rio.run())
