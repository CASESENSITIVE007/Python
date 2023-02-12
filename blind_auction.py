from replit import clear
bid={}
bidding_finished=False
def heighest_bidder(bidding_record):
    hieghest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>hieghest_bid:
            hieghest_bid=bid_amount
            winner=bidder
    print("The auction winner is:",winner)

while not bidding_finished:
    name=input("enter your name")
    price=int(input("enter the bid: $"))
    bid[name]=price
    should_continue=input("If there are any other bidders type Yes else type No:").lower()
    if should_continue=="no":
        bidding_finished=True
        heighest_bidder(bid)
    elif should_continue=="yes":
        clear()












 
