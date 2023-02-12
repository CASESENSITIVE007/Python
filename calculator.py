from replit import clear
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2
def calculator():
    operations={"+":add,"-":subtract,"*":multiply,"/":devide}
    num1=float(input("enter the first number"))
    continue_operation=True
    while continue_operation:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("enter the operation you want to perform")
        num2=float(input("type the next number"))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(num1,operation_symbol,num2,"=",answer)
        if (input("type y for continue the operation or type n for exit"))=="y":
            num1=answer
        else:
            continue_operation=False
            calculator()

calculator()




    
