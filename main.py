from replit import clear
from art import logo

end = False
bids = {}
highest_bid = 0
highest_bidder = ""

print(logo)
print("Welcome to the secret auction program. ")

while not end:
    bidder_number = len(bids) + 1
    bidder = input(f"Bidder #{bidder_number}'s name: ")
    bid = int(input(f"{bidder}'s bid: $"))
    bids[bidder] = bid
    other_bidders = input("Are there other bidders (y/n): ").lower()

    if other_bidders == "n":
        end = True

    clear()

# for testing the loop
# bids = {"spam": 1, "eggs": 2}

for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
