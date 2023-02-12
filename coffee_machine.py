
print ('''WELCOME TO SAAD COFFEE MACHINE
WE HAVE EXPRESSO LATTE AND CAPICHINO !!!! ''')
profit=0
resources={"water":500,"milk":500,"coffee":500}
menu={"expresso":{"ingridents":{"water":50,"coffee":18,"milk":0},
"cost":1.5},
"latte":{"ingridents":{"water":200,"coffee":24,"milk":150},
"cost":2.5},
"capichino":{"ingridents":{"water":250,"coffee":24,"milk":100},
"cost":3.5},
}
def is_resource_sufficient(order_ingridents):
    for items in order_ingridents:
        if order_ingridents[items]>=resources[items]:
            print(f"not enough {items}")
            return False
        else: return True
def amount():
    coin_p=input("how many number of penny coin you have")
    penny=int(coin_p)*0.01
    coin_n=int(input("enter how many number of nickel coins you have"))
    nickel=coin_n*0.05
    coin_d=int(input("enter how many number of dime coins you have"))
    dime=coin_d*0.1
    coin_q=int(input("enter how many number of quarter coins you have"))
    quarter=coin_q*0.25
    total_d=penny+nickel+dime+quarter
    return total_d
def is_transaction_successful(received_money,drink_cost):
    global profit
    if received_money>=drink_cost:
        change=round(received_money-drink_cost,2)
        print(f"here is your {change}$ change")
        profit+=drink_cost
        return True
    else:
        print("not enough money")
        return False
def make_coffee(drink_name,order_ingridents):
    for items in order_ingridents:
        resources[items]-=order_ingridents[items]
    print(f"here is you {drink_name}")
is_on=True
while is_on:
    choice=input("waht would you like (expresso/latte/capichino):").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water {resources['water']} ml")
        print(f"milk {resources['milk']} ml")
        print(f"coffee {resources['coffee']} gm")
        print(f"profit {profit}$ ")
    else:
        drink=menu[choice]
        if  is_resource_sufficient(drink["ingridents"]):
            payment=amount()
            is_transaction_successful(payment,drink["cost"])
            make_coffee(choice,drink["ingridents"])
