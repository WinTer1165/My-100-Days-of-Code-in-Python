print('''
888888888888 88888888ba  88888888888        db        ad88888ba  88        88 88888888ba  88888888888      ,ad8888ba,        db        88b           d88 88888888888  
     88      88      "8b 88                d88b      d8"     "8b 88        88 88      "8b 88              d8"'    `"8b      d88b       888b         d888 88           
     88      88      ,8P 88               d8'`8b     Y8,         88        88 88      ,8P 88             d8'               d8'`8b      88`8b       d8'88 88           
     88      88aaaaaa8P' 88aaaaa         d8'  `8b    `Y8aaaaa,   88        88 88aaaaaa8P' 88aaaaa        88               d8'  `8b     88 `8b     d8' 88 88aaaaa      
     88      88""""88'   88"""""        d8YaaaaY8b     `"""""8b, 88        88 88""""88'   88"""""        88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""      
     88      88    `8b   88            d8""""""""8b          `8b 88        88 88    `8b   88             Y8,        88  d8""""""""8b   88   `8b d8'   88 88           
     88      88     `8b  88           d8'        `8b Y8a     a8P Y8a.    .a8P 88     `8b  88              Y8a.    .a88 d8'        `8b  88    `888'    88 88           
     88      88      `8b 88888888888 d8'          `8b "Y88888P"   `"Y8888Y"'  88      `8b 88888888888      `"Y88888P" d8'          `8b 88     `8'     88 88888888888  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input(
    "You\'re at a crossroad. Where do you want to go? Type \"left\" or \"right\"")
b = a.lower()

if b == "left":
    c = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    d = c.lower()
    if d == "wait":
        e = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        f = e.lower()
        if f == "yellow":
            print("You found the treasure! You Win!")
        elif f == "red":
            print("It's a room full of fire. Game Over.")
        elif f == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
