
import random
letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
        "Q","R","S","T","U","V","W","X","Y","Z"]
number=["1","2","3","4","5","6","7","8","9"]
symbol=["@","#","$","%","^","&","*","(",")"]
let=int(input("enter how many letter you want in your password"))
num=int(input("enter how many number you want in your password "))
sym=int(input("enter how many symbol you want in your password"))
password=[]
for i in range(let):
    let_rand=random.choice(letter)
    password.append(let_rand)

for i in range(num):
    num_rand=random.choice(number)
    password.append(num_rand)

for i in range(sym):
    sym_rand=random.choice(symbol)
    password.append(sym_rand)
random.shuffle(password)
password_str=""
for  i in password:
    password_str+=i
print(password_str)


