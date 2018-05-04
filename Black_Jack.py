import random

d = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'K',
     'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', 'A', 'A', 'A', 'A']


def checkanswer():
    while True:
        answer = In.stinp()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Invalid input\nTRY AGAIN")
            continue


class Inp(object):
    def __init__(self):
        pass

    def intinp(self):
        while True:
            try:
                a = int(input())
            except:
                print("Invalid Input\nTRY AGAIN")
                continue
            else:
                break
        return a

    def stinp(self):
        while True:
            try:
                a = input().lower()
                if a == "":
                    print("Invalid Input\nTRY AGAIN")
                    continue
                else:
                    pass
            except:
                print("Invalid Input\nTRY AGAIN")
                continue
            else:
                break
        return a


class Deck(object):
    def __init__(self, deck):
        self.deck = deck

    def deckassign(self):
        x = random.randint(0, 51)
        y = random.randint(0, 51)
        return self.deck[x], self.deck[y]

    def hitdeckassign(self):
        x = random.randint(0, 51)
        return self.deck[x]

    def deckcheck(self, card1,card2, sum):
        while True:

            try:
                sum = sum + card1 + card2

            except:
                if card1 == 'A':
                    if sum<10:
                        card1 = 11
                        continue
                    else:
                        card1 = 1
                        continue
                elif card2 == 'A':
                    if sum<10:
                        card1 = 11
                        continue
                    else:
                        card1 = 1
                        continue
                elif card1 == 'K' or card1 == 'J' or card1 == 'Q':
                    card1 = 10
                    continue
                else:
                    card2 = 10
                    continue

            else:
                return sum

    def hitdeckcheck(self,sum,card):
        while True:
            try:
                sum += card
            except:
                if card == 'A':
                    if sum<10:
                        card = 11
                        continue
                    else:
                        card = 1
                        continue
                else:
                    card = 10
                    continue
            else:
                return sum

    def wincheck(self,sum,sum1):
        if sum1>21:
            return 2
        elif sum>sum1:
            return 1
        elif sum<sum1:
            return -1
        else:
            return 0


class Player(object):
    def __init__(self, balance):
        self.balance = balance

    def addbalance(self):
        print("What value of Chips would you like to Buy, Sir")
        amount = In.intinp()
        self.balance += amount
        print("Your new balance is {x}".format(x=self.balance))

    def subbalance(self, bet):
        self.balance -= bet

    def __str__(self):
        return self.balance

    def checkbalance(self, bet):
        while True:
            if bet <= self.balance:
                break
            else:
                print(
                    "Your bet is more than the amount of chips you have\nWould you like to buy more chips and try again Sir? press y for Yes and n to change you amount")
                if checkanswer():
                    Player.addbalance()
                else:
                    print("Okay, Place your Bet")
                    bet = In.intinp()
                    continue


print("Welcome to Black Jack\nPlease Enter your Name")
In = Inp()
name = In.stinp()
print("What amount of chips would you like to buy today Mr.{x}".format(x=name))
balance = In.intinp()
Player = Player(balance)

while True:

    print("Okay!, Mr. {x} lets Start\nPlace you Bet".format(x=name))
    Bet = In.intinp()
    Player.checkbalance(Bet)
    Player.subbalance(Bet)
    print("Press ENTER when you are ready to start the Game")
    input()
    b = Deck(d)
    x, y = b.deckassign()
    print("Your Cards are \n{x}, {y}".format(x=x, y=y))
    g, h = b.deckassign()
    print("The Dealer's Face up card is \n{x}".format(x=g))
    sum = b.deckcheck(x, y, 0)
    sum1 = b.deckcheck(g, h, 0)

    while sum<21:
        print("Will you Like to Hit or Stand\nPress y if you will Hit or n if you want to Stand")
        if checkanswer():
            x = b.hitdeckassign()
            print("Your card is {x}".format(x=x))
            sum = b.hitdeckcheck(sum, x)
        else:
            break

    if sum > 21:
        print("You are Busted!\nYour Balance is")
        print(Player.balance)
        print("\nWould you like to Play Again\nPress y for Yes and n for No")
        if checkanswer():
            continue
        else:
            quit()

    print("The dealer's cards are {x}, {y}".format(x=g, y=h))
    if sum1<17:
        print("The dealer will pick another card\nHis next card is:")
        g = b.hitdeckassign()
        sum1 = b.hitdeckcheck(sum1, g)
        print(g)
    check = b.wincheck(sum, sum1)
    if check == 2:
        print("Congrats you won!\n your balance is:")
        Player.balance = Player.balance + Bet * 2
        print(Player.balance)
    elif check == 1 and sum == 21:
        print("Congrats you won with a Blackjack!\n your balance is:")
        Player.balance = Player.balance + (Bet*2.5)
        print(Player.balance)
    elif check == 1:
        print("Congrats you won!\n your balance is:")
        Player.balance = Player.balance + Bet*2
        print(Player.balance)
    elif check == -1:
        print("Sorry you lost!\nyour balance is:")
        print(Player.balance)
    else:
        print("Its a draw!\nYour balance is:")
        Player.balance = Player.balance + Bet
        print(Player.balance)

    print("Would you like to Play Again\nPress y for Yes and n for No")
    if checkanswer():
        continue
    else:
        quit()


