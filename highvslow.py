import random
from replit import clear
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data=[
{
    "Name":"cristiano ronaldo",
    "Follower_count":156,
    "discription":"footballer",
    "country":"portugal"
},
{
    "Name":"instagram",
    "Follower_count": 346,
    "discription":"social_media_platform",
    "country":"US"
},
{
    "Name":"Ariana",
    "Follower_count": 345,
    "discription":"Singer",
    "country":"US" 
},
{
    "Name":"saad",
    "Follower_count": 999,
    "discription":"coder",
    "country":"INDIA" 
},
{
    "Name":"sharukh khan",
    "Follower_count": 991,
    "discription":"actor",
    "country":"INDIA" 
},
{
    "Name":"elon musk",
    "Follower_count": 69,
    "discription":"businessman",
    "country":"foreign" 
},
{
    "Name":"mia",
    "Follower_count": 34,
    "discription":"singer",
    "country":"foreign" 
}

]

def game():
    print(logo)
    count=0
    game_over=False
    random_data2=random.choice(data)
    while game_over==False:
        random_data1=random_data2
        random_data2= random.choice(data)
        while random_data1==random_data2:
            random_data2=random.choice(data)
        print("A=",random_data1["Name"],",",random_data1["discription"],",",random_data1["country"])
    
        print(vs)
        
        print("B=",random_data2["Name"],",",random_data2["discription"],",",random_data2["country"])
        more_followers=input("who has more followers").lower()
        if (random_data1["Follower_count"]>random_data2["Follower_count"]) and more_followers=="a":
            count+=1
            clear()
            print("you score is",count)
        elif (random_data2["Follower_count"]>random_data1["Follower_count"]) and more_followers=="b":
            count+=1
            clear()
            print("you score is",count)    
        else:
            clear()
            print("you loose")
            print("you final score is",count)
            game_over=True

game()