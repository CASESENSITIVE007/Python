import random
hand=input("enter stone,paper,or scissors ").lower()
list1=["stone","paper","scissors"]
rand=random.choice(list1)
print("computer:",rand)
if hand=="stone" and rand=="stone":
    print("tie")
elif hand=="paper" and rand=="stone":
    print("you win")
elif hand=="scissor" and rand=="stone":
    print("you loose")
elif hand=="stone" and rand=="paper":
    print("you loose")
elif hand=="paper" and rand=="paper":
    print("tie")
elif hand=="scissors" and rand=="paper":
    print("you win")
elif hand=="stone" and rand=="scissors":
    print("you win")
elif hand=="paper" and rand=="scissors":
    print("you loose")
elif hand=="scissors" and rand=="scissors":
    print("tie")



