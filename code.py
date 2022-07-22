# We all have played snake, water, gun game in our childhood.Write a python program capable of playing this game with the user.
import random
'Returning None if game is tie or invalid input is entered, True if user wins and False if user lose'
def SnakeWaterGun(comp, you):
    if(comp==you):
        print(f'Computer choose {comp} and you choose {you}')
        print("Game is tie")
        return None
    elif(you=='s' and comp=='w'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You win")
        return True
    elif(you=='s' and comp=='g'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You lose")
        return False
    elif(you=='w' and comp=='s'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You lose")
        return False
    elif(you=='w' and comp=='g'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You win")
        return True
    elif(you=='g' and comp=='s'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You win")
        return True
    elif(you=='g' and comp=='w'):
        print(f'Computer choose {comp} and you choose {you}')
        print("You lose")
        return False
    else:
        print("Invalid input entered by you")
        return None
randNo=random.randint(1, 3)
if(randNo==1):
    comp='s'
elif(randNo==2):
    comp='w'
else:
    comp='g'
you=input("Your input:Enter 's' for snake, 'w' for water and 'g' for gun:")
result=SnakeWaterGun(comp, you)
print("SnakeWaterGun function returns", result)