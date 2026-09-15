#  Stack market application
# 1.add money to your wallet
# 2.show stacks with prices
# 3. stack prices changes randomly
# 4. Buy stack if you enough your money
# 5. sell stack if you own money
# 6. portofolio shows your shares
# 7. wallet update after buy/sell 
# 8. quit any time and  see final summary
import random
wallet = int(input("enter your money into a wallet:"))# wallet add the money
stocks = {
    "TATA":100,
    "VOLVO":200,
    "BENZ":40

}# we have to create dictionary in stocks

portfolio = {} # user portfolio intialize
def update_prices():
    for stock in stocks:
        change = random.randint(-20, 20)
        new_prices = stocks[stock] + change
        stocks[stock] = max(10, new_prices)


while True: # loop contineous to be exceuted
    print()
    print('----Stock Market-------')# we have to display the starting the stack market
    for name, price in stocks.items():#We used a for loop to display the stacks available in our data.
        print(f'{name} - {price}') 
    print(f'wallet - {wallet}')# we used print statement to displey the wallet amount
    print(f'potfolio- {portfolio if portfolio else "Empty"}')

    choice = input('\nBUY-B \nSELL- S \nQUIT- Q:').lower() # we have to display the buttons
    if choice == 'b':
        stock = input("enter your stock name:").upper()
        if stock not in stocks:
            print("Invalid stock")
            continue
        qty = int(input('how many shares:'))
        cost = stocks[stock] * qty
        if cost > wallet:
            max_qty = wallet // stocks[stock]
            print(f'not enough money. you can buy max-{max_qty} shares')
        else:
            wallet -= cost
            portfolio[stock] = portfolio.get(stock,0) + qty
            print(f'bought {qty} {stock} for {cost}')

    elif choice == 's':
        stock = input("enter your stock name:").upper()
        if stock not in portfolio or portfolio[stock] == 0:
            print("you don't own any stock")
            continue
        
        qty = int(input('how many shares:'))
        if qty > portfolio[stock]:
            print(f'you only own {portfolio[stock]} shares')
        else:
            earning = stocks[stock] * qty
            wallet += earning
            portfolio[stock] -= qty
            print(f'sold {qty} {stock} for {earning}')

    elif choice == 'q':
        print(f'wallet - {wallet}')
        print(f'potfolio- {portfolio if portfolio else "Empty"}')
        print("Thanks for trading")

    else:
        print("Invalid choice")
    update_prices()