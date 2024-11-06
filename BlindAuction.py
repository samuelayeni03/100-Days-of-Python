import os

logo = '''
                         ___________
                         |         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                       .-------------.
                      /_______________|
'''

print(logo)
print("Welcome to the secret auction program.")
auction_bids = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction_bids[name] = bid

    print("Are there any other bidders? Type 'yes' or 'no'.")
    choice = input()
    os.system('cls')
    if choice == 'yes':
        continue
    else:
        break

highest_bid = 0
bidder = ""
for bidders in auction_bids:
    if auction_bids[bidders] > highest_bid:
        highest_bid = auction_bids[bidders]

    bidder = next((k for k, v in auction_bids.items() if v == highest_bid), None)

print(f"The highest bidder is {bidder.title()} with a bid of ${round(highest_bid, 2)}")