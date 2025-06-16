print("Welcome to Blind Auction!!")

#Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid is ${highest_bid}")

#To save data into dictionary
bidding = {}

#Whether if new bidders need to be added
continue_bidding = True
while continue_bidding:
    #Ask the user for input
    name = input("What's your name?: ")
    bid = int(input("How much you bid?: $"))
    bidding[name] = bid
    bidders = input("Are they any bidders left, type 'yes' if any otherwise 'no'\n" ).lower()
    if bidders == 'no':
        continue_bidding = False
        find_highest_bidder(bidding)
    elif bidders == 'yes':
        print("\n" * 20)


