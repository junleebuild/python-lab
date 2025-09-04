from art import logo
print(logo)
# TODO-1: Ask the user for input
add = True
dictionary = {}
while add == True:
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  "))
    # TODO-2: Save data into dictionary {name: price}
    dictionary[name] = bid
    # TODO-3: Whether if new bids need to be added
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    if add_bidder == 'no':
        add = False
    else:
        print("\n" * 20)

# TODO-4: Compare bids in dictionary
highest_price = 0
highest_bidder = ""
for bidder in dictionary:
    if dictionary[bidder] > highest_price:
        highest_price = dictionary[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_price}")



