alphabet=["a","b","c","d","e","f","g","h","i","j"
    ,"k","l","m","n","o","p","q","r","s","t","u","v",
    "w","x","y","z","a","b","c","d","e","f","g","h","i","j"
    ,"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def caesar(plain_text,shift_amount,direction):
    text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        if direction=="encode":
            new_position=position+shift_amount
            text+=alphabet[new_position]
        elif direction=="decode":
            new_position=position-shift_amount
            text+=alphabet[new_position]
    print(text)
again="yes"
while again!="no":
    dir=input("enter encode to encrypt and decode to decrypt").lower()
    shift=int(input("enter the shift number"))
    text_=input("enter the text").lower()
    caesar(plain_text=text_,shift_amount=shift,direction=dir)
    again=input("if you want to run the encryot or decrypt again type yes else type no:").lower() 







        
    
        



