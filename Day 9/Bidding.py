import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction_dictionary = {}
bidding_done = False

def clear():
    # Check if the operating system is Windows or not
    if os.name == 'nt':
        _ = os.system('cls')  # For Windows
    else:
        _ = os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_done:
    name = input('What is your name? ')
    price = int(input('What is your bidding price? $'))
    auction_dictionary[name] = price
    continue_bidding = input('Are there any other bidders (yes/no)?')
    if continue_bidding == 'no':
        bidding_done = True
        find_highest_bidder(auction_dictionary)
    elif continue_bidding == 'yes':
        clear()
