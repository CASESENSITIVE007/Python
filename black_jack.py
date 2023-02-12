import random
from replit import clear
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(card):
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "DRAW!"
    elif computer_score==0:
        return"COMPUTER WIN"
    elif user_score==0:
        return "YOU WIN"
    elif computer_score>21:
        return "YOU WIN"
    elif user_score>21:
        return "YOU LOOSE"
    elif user_score > computer_score:
        return "YOU WIN"
    else: return "COMPUTER WINS"
def play_game():
    user_cards=[]
    computer_cards=[]
    game_over=False
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while game_over==False:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print("your cards:",user_cards,"your score",user_score)
        print("computer cards:",computer_cards[0])

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            draw=input("type yes if you want to add another card otherwise press any button:").lower()
            if draw == "yes":
                user_cards.append(deal_cards())
                print(user_cards)
                print(calculate_score(user_cards))
            else:
                game_over=True
            
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)
    print("Final computer cards=",computer_cards,"Final Computer score=",computer_score)
    print("Final user cards=",user_cards,"Final user score=",user_score)
    print(compare(user_score,computer_score))

while input("YOU WANT TO PLAY A BLACKJACK GAME?? TYPE Y:::").lower()=="y":
    clear()
    play_game()
