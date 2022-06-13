# Rock Paper Scissors
import random
def gameWin(comp, user):
    if comp == user:
        return None
    if comp == 'r': # Definig the rules for rock paper and scissors game
        if user == 's':
            return False
        if user == 'p':
            return True
    if comp == 'p':
        if user == 'r':
            return False
        if user == 's':
            return True    
    if comp == 's':
        if user == 'p':
            return False
        if user == 'r':
            return True




print("Comp Turn: Rock(r), Paper(p) or Scissors(s)?")
randNo = random.randint(1,3)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
else:
    comp='s'

user = input("Your Turn: Rock(r), Paper(p) or Scissors(s)?: ")

print(f"Computer choose:  {comp}")
print(f"User choose:  {user}")
a = gameWin(comp, user)
if a == None:
    print("The game is tie!")
elif a:
    print("User win!")
else:
    print("User lose!")