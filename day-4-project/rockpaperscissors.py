import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
a = rock, paper, scissors

user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user >= 3 or user < 0:
    print("You typed an invalid number. You lose!")
else:
    print("You chose:" + a[user])

    b = random.randint(0, 2)
    print("Computer chose:"+a[b])

    if user == 0 and b == 2:
        print("You Win!")
    elif b == 0 and user == 2:
        print("You Lose!")

    elif b > user:
        print("You lose")
    elif user > b:
        print("You win!")
    elif b == user:
        print("It's a draw")
