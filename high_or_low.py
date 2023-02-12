import random
"""numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,
45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,
67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,
89,90,91,92,93,94,95,96,97,98,99,100]
random_number=random.choice(numbers)
print(random_number)"""
numbers=[]
for i in range (1,101):
    numbers.append(i)
random_number=random.choice(numbers)

def hard_level():
    print("YOU HAVE ONLY 5 LIVES")
    chance=5
    while chance>0:
        user_number=int(input("enter your number"))
        if user_number==random_number:
            return print("you win")
        elif user_number<random_number:
            print ("too low")
        elif user_number>random_number:
            print ("you high")
        chance =chance-1
        print("YOU HAVE LEFT",chance,"chances")
    print("GAME OVER !!! you loose")
    
def easy_level():
    print("YOU HAVE ONLY 10 LIVES")
    chance=10
    while chance>0:
        user_number=int(input("enter your number"))
        if user_number==random_number:
            return print("you win")
        elif user_number<random_number:
            print ("too low")
        elif user_number>random_number:
            print ("you high")
        chance =chance-1
        print("YOU HAVE LEFT",chance,"chances")
    print("GAME OVER!!! you loose")
play_again=False

while play_again==False:
    level=input("WHAT LEVEL YOU WANNA PLAY EASY OR HARD:").lower()
    if level=="easy":
        easy_level()
    elif level=="hard":
        hard_level()
    play=input("enter y if you play again otherwise enter n:").lower()
    if play=="y":
        play_again=False
    else:
        play_again=True
        print("THANKYU FOR PLAYING♥♥♥") 
        
