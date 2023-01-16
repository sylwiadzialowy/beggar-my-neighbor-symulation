colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
allCards=[]

for color in colors:
    for figure in figures:
        aCard=figure.copy()
        aCard['Color']= color
        allCards.append(aCard)

import random
random.shuffle(allCards)
#print(allCards)
#print(len(allCards))

player1=allCards[0:11]
player2=allCards[12:23]

#print("1st player cards:",player1)
#print("2nd player cards:",player2)

i=0
while len(player1)>0 and len(player2)>0:
    print("*"*len(player1))
    print("*"*len(player2))
    card1=player1.pop(i)
    card2=player2.pop(i)
    stock=[]
    while card1.get('Power')==card2.get('Power'):
        print("Player 1 card power:",card1.get('Power'),"\n","Player 2 card power:",card2.get('Power'),"\n","This is a war!")
        stock.append(card1)
        stock.append(card2)
        if len(player1) <2:
            player2.extend(stock)
            player2.extend(player1)
            player1.clear()
            break
        if len(player2) <2:
            player1.extend(stock)
            player1.extend(player2)
            player2.clear()
            break
        if len(player1) >=2 and len(player2)>=2:
            card1=player1.pop(i)
            card2=player2.pop(i)
            stock.append(card1)
            stock.append(card2)
            card1=player1.pop(i)
            card2=player2.pop(i)
    else:  
        if card1.get('Power')>card2.get('Power'):
            stock.append(card1)
            stock.append(card2)
            player1.extend(stock)
            print("Player 1 card power:",card1.get('Power'),"\n","Player 2 card power:",card2.get('Power'),"\n", "Player 1 won")
        if card1.get('Power')<card2.get('Power'):
            stock.append(card1)
            stock.append(card2)
            player2.extend(stock)
            print("Player 1 card power:",card1.get('Power'),"\n","Player 2 card power:",card2.get('Power'),"\n", "Player 2 won")
    
    print("---------------------")        
print("Player 1 has",len(player1),"cards")
print("Player 2 has",len(player2),"cards")
if len(player1) == 0:
    print("Player 2 won the war!")
if len(player2) == 0:
    print("Player 1 won the war!")
