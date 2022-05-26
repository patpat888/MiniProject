#blackjack in python
import random
#Creation of deck (52 cards in 2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace with 
    #Numbers as 2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace
    #Face as "Diamond","Spade","Heart","Club"
Card_Num = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
Card_Face = ["Diamond","Spade","Heart","Club"]
deck=[] #this is to create an empty deck to store the cards

for n in Card_Num: #13 different numbers
    for f in Card_Face: # 4 different faces
        deck.append((n,f))

#Sum of playercards
def SumPlayer():
    global sum_p
    sum_p=0 #sum of playercards
    for p,f in playercards:
        if p=="2":
            sum_p+=2
        elif p=="3":
            sum_p+=3
        elif p=="4":
            sum_p+=4
        elif p=="5":
            sum_p+=5
        elif p=="6":
            sum_p+=6
        elif p=="7":
            sum_p+=7
        elif p=="8":
            sum_p+=8
        elif p=="9":
            sum_p+=9
        elif p=="10" or p=="Jack" or p=="Queen" or p=="King":
            sum_p+=10
    #the above first calculate cards sum without Ace
    for p,f in playercards:
        if p=="Ace" and  sum_p>=11:
            sum_p+=1
        elif p=="Ace" and sum_p<11:
            sum_p+=11
    #the above then calculate total, once all nonAce summed
        
    return sum_p
        

#Sum of dealercards
def SumDealer():
    sum_d=0 #sum of dealercards
    for d,f in dealercards:
        if d=="2":
            sum_d +=2
        elif d=="3":
            sum_d+=3
        elif d=="4":
            sum_d+=4
        elif d=="5":
            sum_d+=5
        elif d=="6":
            sum_d+=6
        elif d=="7":
            sum_d+=7
        elif d=="8":
            sum_d+=8
        elif d=="9":
            sum_d+=9
        elif d=="10" or d=="Jack" or d=="Queen" or d=="King":
            sum_d+=10
        
    for d,f in dealercards:
        if d=="Ace" and sum_d>=11:
            sum_d+=1
        elif d=="Ace" and sum_d<11:
            sum_d+=11
    return sum_d

#Define gameflow
#creation of playercards and dealercards
def GameStart():
    random.shuffle(deck)
    global playercards
    playercards=[]
    global dealercards
    dealercards=[]
    playercards.append(deck.pop()) #give the 1st card from deck to player
    dealercards.append(deck.pop()) #give the 2nd card from deck to dealer
    playercards.append(deck.pop()) #give the 3rd card from deck to player
    dealercards.append(deck.pop()) #give the 4th card from deck to dealer
    sp=SumPlayer()
    sd=SumDealer()
    print("Your cards are ",list(zip(*playercards))[0],"and total point is ",sp)
    if (sp ==21):
            print("Wow!! Player Blackjack!!")
    print("Dealer card is ('",(dealercards[1][0]).strip(), "')") #only show one dealer card to player


 
def Hit_or_Stand():
    sp=SumPlayer()    
    sd=SumDealer()
    if (sp ==21):   #Instant blackjack after first two card    
        if sd==21:
            print("Dealer card is ",list(zip(*dealercards))[0],"and total point is ",sd)
            print("***Wow!!Dealer Blackjack!!***")
            print("***Its a tie!!***")
        else:
            print("Dealer card is ",list(zip(*dealercards))[0],"and total point is ",sd)
            print("***You Win!!***")

    elif (sp<21): #if no blackjack after the first two card, go for hit or stand        
        while True:            
            decision=input("hit or stand? ").lower()
            if decision=="hit" or decision =="h":
                playercards.append(deck.pop())
                sp=SumPlayer()
                print("Your cards are ",list(zip(*playercards))[0],"and total point is ",sp)
                if sp>21:
                    print("***Player burst!! You Lose!!***")
                    break                
            if decision=="stand" or decision == "s":
                print("Dealer card is ",list(zip(*dealercards))[0],"and total point is ",sd)
                while True:
                    sd=SumDealer()
                    if (sd>=17)and (sd>sp):
                        print("***You Lose!!***")
                        break
                    if (sd>=17)and (sd==sp):
                        print("***It's tie!!***")
                        break
                    if (sd>=17)and (sd<sp):
                        print("***You Win***!!")
                        break
                    if (sd<17):
                        dealercards.append(deck.pop())
                        sd=SumDealer()
                        print("Dealer card is",list(zip(*dealercards))[0],"and total point is ",sd)
                    if sd>21:                        
                        print("***Dealer burst!! You Win!!***")
                        break
                break
            
#next game
def GameON():
    #print(deck)
    Question= "Do you want to start a new game? (YES / NO) "
    while True:
        print("")
        Start =input(Question).upper()
        if Start == "YES" or Start=="Y":
            print("")
            GameStart()
            Hit_or_Stand()
            
        elif Start =="NO" or Start=="N":
            print("Goodbye")
            break


GameON()





