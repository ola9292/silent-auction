
import art

bid_on = True
bids = {}

def calculate_winner():
    winning_amount = 0
    winning_name = ''
    for key in bids:
        if bids[key] > winning_amount:
            winning_amount = bids[key]
            winning_name = key
    print(f"The winner is {winning_name} with a bid of ${winning_amount}")      

print(art.logo)        
while bid_on:
 
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $")) 
    bids[name] = bid_amount
    continue_bid = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if continue_bid == 'yes':
        print("\n" * 100)
    else:
        bid_on = False
calculate_winner()
