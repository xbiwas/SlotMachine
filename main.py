import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Deposited")
                break
            else:
                print("Amount should be greater than zero.")
        else:
            print("Please enter a number.")
    return amount

def numberOfLines():
    while True:
        lines = input("Enter the number of lines. ")
        if lines.isdigit():
            lines = int(lines)
        
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines should be between 1-" + str(MAX_LINES))
        
        else:
            print("Please enter a number")
    return lines

def getBets():
    while True:
        bet = input("Enter the betting amount. $")
        if bet.isdigit():
            bet = int(bet)
        
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Betting amount should be between {MAX_BET} - {MIN_BET} ")
        
        else:
            print("Please enter a number")
    return bet

def main():    
    balance = deposit()
    lines = numberOfLines()
    while True:
        bets = getBets()
        totalBet = lines * bets
        if totalBet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bets} on {lines} lines. Your total betting is ${totalBet}. your current balance is {balance - totalBet}")
main()