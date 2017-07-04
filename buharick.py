import random

def get_card(player):
    while True:
        yield player["колода"].pop()
        


def turn(player1, player2):
    k = 0
    for card1, card2 in zip(get_card(player1),get_card(player2)):
        schet1 = card1[0]
        schet2 = card2[0]  
        metka1 = card1[1]  
        metka2 = card1[1] 


        if (schet1>5 and schet1<11) and (schet2 >5 and schet2 <11):
            print(schet1, metka1)
            print(schet2, metka2)


        elif (schet1>5 and schet1<11) and not (schet2 >5 and schet2 <11):
            print(schet1, metka1)
            if schet2 == 11:
                print("Валет", metka2)
            elif schet2 == 12:
                print("Дама", metka2)
            if schet2 == 13:
                print("Король", metka2)
            else:
                print("Туз", metka2)    



        elif (not schet1>5 and schet1<11) and  (schet2 >5 and schet2 <11):
            if schet1 == 11:
                print("Валет", metka1)
            elif schet1 == 12:
                print("Дама", metka1)
            if schet1 == 13:
                print("Король", metka1)
            else:
                print("Туз", metka1)  
            print(schet2, metka2)


        else:
            if schet1 == 11:
                print("Валет", metka1)
            elif schet1 == 12:
                print("Дама", metka1)
            if schet1 == 13:
                print("Король", metka1)
            else:
                print("Туз", metka1) 
                
            if schet2 == 11:
                print("Валет", metka2)
            elif schet2 == 12:
                print("Дама", metka2)
            if schet2 == 13:
                print("Король", metka2)
            else:
                print("Туз", metka2)    



        k += 2
        if card1[0] < card2[0]:
            player2["счет"] += k
            break

        elif card2[0] < card1[0]:
            player1["счет"] += k
            break  

suits = ["сердце","кирпич","пика","крест"]
papka = ["Валет","Дама","Король","Туз"]
deck = [(num,suit) for suit in suits for num in range(6,15)]
random.shuffle(deck)
# print(deck)
player1 = {}
player2 = {}
player1["колода"] = deck[:len(deck)//2]
player2["колода"] = deck[len(deck)//2:]
player1["счет"] = 0
player2["счет"] = 0
while True:
    turn(player1, player2)
    print(player1["счет"], player2["счет"])
    input()
    if not player1["колода"] or not player2["колода"]:
        break