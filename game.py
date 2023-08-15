import random

def gameWin(comp, you):
   if comp == you:
         return None
   elif comp == 's':
       if you == 'g':
            return False
       elif you == 'w':
            return True
   elif comp == 'w':
       if you == 'g':
            return False
       elif you == 's':
            return True
   elif comp == 'g':
       if you == 'w':
            return False
       elif you == 's':
            return True

print("Comp turn: Snake(s) Water(W) or Gun(g)!")
Number= random.randint(1, 4)
if Number == 1:
  comp ='s'
elif Number == 2:
  comp ='w'
elif Number == '3':
  comp = 'g'

you = input("Your turn: Snake(s) Water(W) or Gun(g)!")
a = gameWin(comp, you)
 
print(f"Compuer print {comp}")
print(f"Your print {you}")

if a==None:
     print("the game is tie!")
elif a:
     print ("You win!")
else:
     print("You lose!")