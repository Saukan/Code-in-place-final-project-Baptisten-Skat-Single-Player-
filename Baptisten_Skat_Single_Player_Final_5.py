"""
Baptisten-Skat Card Game - Single Player: 
The project is going to create a single player and simplified version of the German card game Baptisten-Skat. 
The game is about placing bids and then trying to achieve the bid values in rounds. 
The user is going to play against two AI players that I set up. Of coz, their strategies could be changed or made more complex, but for now their plays are kind of okay. 
An introduction is included in beginning of the game. 
For more info about Baptisten-Skat, pls visit: http://ftp.informatik.rwth-aachen.de/Brettspielvarianten/v-036-01.htm

The game is fun, I hope you like it too. 
"""

from random import randint
from random import choice

NUM_PLAYERS =3


def main():
    total_score_user=0
    total_score_player_2=0
    total_score_player_3=0

    intro()
    print("Number of players: " + str(NUM_PLAYERS))
    #enter rounds (10 rounds in total)
    #Loop of rounds 
    for i in range(10):
        print("Press Enter to start the round!")
        input("")
        num_round = i+1
        print("Round "+str(num_round))
        if num_round ==10:
            print("Last round!")

        #establish card pile
        print("Press Enter to distribute cards")
        input("")
        card_pile =set_card_pile()
        #print(card_pile)
        #distribute cards to players
        #user is player 1 
        player_1_hand =distribute_card_to_player_1(card_pile ,num_round ,NUM_PLAYERS)
        player_2_hand =distribute_card_to_player_2(card_pile ,num_round ,NUM_PLAYERS)
        player_3_hand =distribute_card_to_player_3(card_pile ,num_round ,NUM_PLAYERS)
        #reveal trump cards
        trump_color =reveal_trump(card_pile)
        #show the user his card
        print("")
        print("Press Enter to reveal your hand")
        input("")
        show_cards(player_1_hand)
        print("")
        #ask the user to predict number of tricks 
        #make sure input can become int
        while True:
            try: 
                num_expect_user_trick =int(input("What is your bid value? From 0- "+str(num_round)+" : "))
            except ValueError:  
                print("Not a valid bid value, please try again")
                continue
            except None:
                print("Not a valid bid value, please try again")
                continue

            else:
                break
        #make sure input within range 
        while num_expect_user_trick>num_round or num_expect_user_trick <0:
            print("Not a valid bid value, please try again")
            num_expect_user_trick =int(input("What is your bid value? From 0- "+str(num_round)+" : "))
        #generate expected number of tricks for computer players 
        num_expect_player_2_trick =gen_expect_trick_player_2(trump_color ,player_2_hand,num_round)
        num_expect_player_3_trick=gen_expect_trick_player_3(trump_color,player_3_hand)
        #reveal the bid value of each player
        print("Bid values: "+ "You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
        total_number_expected_tricks=num_expect_user_trick+num_expect_player_2_trick+num_expect_player_3_trick
        #reveal the total bid vlaue 
        print("Total bid value: "+ str(total_number_expected_tricks))
        print("")
        #Adjusting the number of tricks if needed 
        num_expect_player_3_trick,num_expect_player_2_trick,total_number_expected_tricks,num_expect_user_trick=adjust_tricks(num_round,total_number_expected_tricks,num_expect_player_3_trick,num_expect_user_trick,num_expect_player_2_trick)
        
        #player with the highest expected tricks play the first card 
        first_player_number=get_first_player_number(num_expect_player_3_trick,num_expect_user_trick,num_expect_player_2_trick)
        second_player_number=get_second_player_number(first_player_number)
        third_player_number=get_third_player_number(second_player_number)
        #
        total_won_trick_user=0
        total_won_trick_player_2=0
        total_won_trick_player_3=0

        #The number of tricks = the number of rounds
        #Loop of tricks 
        for i in range(num_round):
            print("Press enter to start the trick!")
            input("")
            #print play sequence 
            print("Here is the play sequence: "+ "Player" +str(first_player_number)+ "--> Player "+str(second_player_number)+"-->Player "+str(third_player_number))
            print("")
            #play the first card 
            if first_player_number==1:
                print("Your hand:"+str(player_1_hand))
                card_played_user=user_plays_a_card(player_1_hand)
                first_card_played=card_played_user
            elif first_player_number==2: 
                #for checking 
                #print(player_2_hand)
                card_played_player_2=player_2_plays_a_card(player_2_hand)
                first_card_played=card_played_player_2
            else:
                #for checking 
                #print(player_3_hand)
                card_played_player_3=player_3_plays_a_card(player_3_hand)
                first_card_played=card_played_player_3
            print("")
            #play the second card 
            if second_player_number==1:
                print("Your hand:"+str(player_1_hand))
                card_played_user=user_plays_a_card_b(player_1_hand,first_card_played,trump_color)
                second_card_played=card_played_user
            elif second_player_number==2:
                #for checking
                #print(player_2_hand)
                card_played_player_2=player_2_plays_a_card_b(player_2_hand,first_card_played,trump_color)
                second_card_played=card_played_player_2
            else:
                #for checking
                #print(player_3_hand)
                card_played_player_3=player_3_plays_a_card_b(player_3_hand,first_card_played,trump_color)
                second_card_played=card_played_player_3
            print("")
            #play the third card
            if third_player_number==1:
                print("Your hand:"+str(player_1_hand))
                card_played_user=user_plays_a_card_b(player_1_hand,first_card_played,trump_color)
                third_card_played=card_played_user
            elif third_player_number==2:
                #for checking:
                #print(player_2_hand)
                card_played_player_2=player_2_plays_a_card_b(player_2_hand,first_card_played,trump_color)
                third_card_played=card_played_player_2
            else:
                #for checking:
                #print(player_3_hand)
                card_played_player_3=player_3_plays_a_card_b(player_3_hand,first_card_played,trump_color)
                third_card_played=card_played_player_3
            print("")
            #find who got the trick 
            #get winner card
            winner_card=get_winner_card(second_card_played,third_card_played,trump_color,first_card_played)
            print("Winner card is: "+str(winner_card))
            #associate winner card with player and announce the trick winner 
            if winner_card== card_played_user:
                print("You got the trick!")
                total_won_trick_user+=1
                winner_num=1
            if winner_card== card_played_player_2:
                print("Player 2 got the trick!")
                total_won_trick_player_2+=1
                winner_num=2
            if winner_card== card_played_player_3:
                print("Player 3 got the trick!")
                total_won_trick_player_3+=1
                winner_num=3
            print("")
            print("")
            #get new play sequence. winner of the last trick starts. 
            first_player_number= winner_num
            if winner_num!=3:
                second_player_number= winner_num+1
            else:
                second_player_number=1
            if second_player_number!=3:
                third_player_number=second_player_number+1
            else:
                third_player_number=1

        #print expected trick and total won tricks 
        print("Bid value      : User: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
        print("Tricks achieved: User: "+str(total_won_trick_user)+" Player 2: "+str(total_won_trick_player_2)+" Player 3: "+str(total_won_trick_player_3))
        # calculate total scores after the round 
        print("")
        total_score_user,total_score_player_2,total_score_player_3=cal_total_score(total_score_user,total_score_player_2,total_score_player_3,total_won_trick_user,total_won_trick_player_2,total_won_trick_player_3,num_expect_user_trick,num_expect_player_2_trick,num_expect_player_3_trick)
        print("Total score: "+"User:" +str(total_score_user)+" Player 2: "+str(total_score_player_2)+" Player 3: "+str(total_score_player_3))
        print("")
        print("")
        print("**************************************")
    
    print("Game Over!")
    input("Press enter to see the winner!")
    #Declare Winner 
    print("Total score: "+"User:" +str(total_score_user)+" Player 2: "+str(total_score_player_2)+" Player 3: "+str(total_score_player_3))
    winner=get_winner(total_score_user,total_score_player_2,total_score_player_3)
    print("")
    print("")
    k=input("Press enter to exit")


def intro():
    print("")
    print("Welcome to this simplified version of Baptisten-Skat")
    print("")
    input("Press enter to continue")
    print("In this game we play with a pile of 80 cards with four colors: Red, Yellow, Green and Blue, and from 1-20")
    print("You are going to play against "+str(NUM_PLAYERS-1)+" players")
    print("There are in total 10 rounds")
    print("")
    input("Press enter to continue")
    print("In each round, the number of cards you will be given and the number of tricks correspond to the number of the round. For example, in Round 1, 1 card will be given, and there is only one trick")
    print("In each round, a trump card will be revealed. The color of the trump card is the trump color")
    print("Cards with the trump color are higher than cards with other colors")
    print("")
    input("Press enter to continue")
    print("In each trick, the color of the card played first is the trick color")
    print("After the first play, if a player has cards with the trick color in hand, he/she has to play a card with the trick color")
    print("If no cards with the trick color are present, any card can be played")
    print("")
    input("Press enter to continue")
    print("In each trick, the player who played the highest card gets the trick")
    print("While cards with the trump color are the highest, cards with the trick color are higher than cards with other non-trump colors")
    print("For cards with the same color, cards with higher numbers are higher than cards with lower numbers")
    print("")
    input("Press enter to continue")
    print("After you look at your card/cards, you will be asked to bid a game value of the round -- the number of expected tricks")
    print("Each players bids on his/her game value independently. The bid value of each player will be announced") 
    print("If the total bid value (the sum of the bid values from all three players) equals to the maximal possible number of tricks, the following adjustment will be made on the bid values")
    print("One player will be randomly selected and his/her bid value either increases or decreases by 1")
    print("")
    input("Press enter to continue")
    print("The player with the highest bid value will start the first trick. From the second trick on, the player who won the previous trick will start the trick")
    print("")
    input("Press enter to continue")
    print("At the end of each round, for each player the number of tricks achieved will be compared with his/her bid value")
    print("If the bid is correct, the total score of the player increases by (20 + (bid value*10))")
    print("If the bid is not correct, the total score of each player decreases by ((the difference between the bid value and the tricks achieved)*10)")
    print("")
    input("Press enter to continue")
    print("At the end of the game, total score will be announced. The player with the highest score wins. It could be a draw as well")
    print("")
    print("Let's try!")
    input("Press Enter to begin!")



#set the pile of cards as a list, and every card is also a list with two elems[Color,intnum]
def set_card_pile():
    card_pile=[]
    for i in range(20):
        card_color="Red"
        card_number=i+1
        card_code=[card_color, card_number]
        card_pile.append(card_code)
    for i in range(20):
        card_color="Green"
        card_number=i+1
        card_code=[card_color, card_number]
        card_pile.append(card_code)
    for i in range(20):
        card_color="Yellow"
        card_number=i+1
        card_code=[card_color, card_number]
        card_pile.append(card_code)
    for i in range(20):
        card_color="Blue"
        card_number=i+1
        card_code=[card_color, card_number]
        card_pile.append(card_code)
    return card_pile


#distribution of cards should be random 
#a card is removed from the pile after being distributed to a player
def distribute_card_to_player_1(card_pile,num_round,num_players):
    player_1_hand=[]
    for i in range (num_round):
        card_taken=choice(card_pile)
        card_pile.remove(card_taken)
        player_1_hand.append(card_taken)
    return player_1_hand 

def distribute_card_to_player_2(card_pile,num_round,num_players):
    player_2_hand=[]
    for i in range (num_round):
        card_taken=choice(card_pile)
        card_pile.remove(card_taken)
        player_2_hand.append(card_taken)
    return player_2_hand 

def distribute_card_to_player_3(card_pile,num_round,num_players):
    player_3_hand=[]
    for i in range (num_round):
        card_taken=choice(card_pile)
        card_pile.remove(card_taken)
        player_3_hand.append(card_taken)
    return player_3_hand 

def reveal_trump(card_pile):
    trump_card=choice(card_pile)
    print("Trump is "+str(trump_card))
    trump_color=trump_card[0]
    print("Trump color is "+str(trump_color))
    return trump_color

def show_cards(player_1_hand):
    print("Your hand: "+str(player_1_hand))

def gen_expect_trick_player_2(trump_color,player_2_hand,num_round):
    num_expect_player_2_trick=0
    for elem in player_2_hand: 
        if elem[0]==trump_color or elem[1]>=18:
            num_expect_player_2_trick+=1
    #extra strategy of player 2
    if num_round>5:
        if num_expect_player_2_trick>5 and num_expect_player_2_trick<8:
            num_expect_player_2_trick-=1
        if num_expect_player_2_trick>=8:
            num_expect_player_2_trick-=2 
    return num_expect_player_2_trick

# player 3 is a less conservative player than player 2
def gen_expect_trick_player_3(trump_color,player_3_hand):
    num_expect_player_3_trick=0
    for elem in player_3_hand: 
        if elem[0]==trump_color or elem[1]>=19:
            num_expect_player_3_trick+=1
    #extra strategy of player 3
    if num_expect_player_3_trick>=4 and num_expect_player_3_trick<7:
        num_expect_player_3_trick-=1
    if num_expect_player_3_trick>=7:
        num_expect_player_3_trick-=2
    return num_expect_player_3_trick

def adjust_tricks(num_round,total_number_expected_tricks,num_expect_player_3_trick,num_expect_user_trick,num_expect_player_2_trick):
    #choice a random player and adjust his/her bid value if needed 
    if total_number_expected_tricks==num_round:
        player_num=randint(1,3)
        if player_num==1:
            #adjust the number up 1 if possible, otherwise down 1
            if total_number_expected_tricks!=num_expect_user_trick:
                num_expect_user_trick+=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
            else:
                num_expect_user_trick-=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
        if player_num==2:
            if total_number_expected_tricks!=num_expect_player_2_trick:
                num_expect_player_2_trick+=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
            else:
                num_expect_player_2_trick-=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
        if player_num==3:
            if total_number_expected_tricks!=num_expect_player_3_trick:
                num_expect_player_3_trick+=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
            else:
                num_expect_player_3_trick-=1
                print("Tricks adjusted: "+"You: "+str(num_expect_user_trick)+" Player 2: "+str(num_expect_player_2_trick)+" Player 3: "+str(num_expect_player_3_trick))
    else: 
        print("No need to adjust tricks")
    total_number_expected_tricks=num_expect_player_3_trick+num_expect_user_trick+num_expect_player_2_trick
    return num_expect_player_3_trick,num_expect_player_2_trick,total_number_expected_tricks,num_expect_user_trick

def get_first_player_number(num_expect_player_3_trick,num_expect_user_trick,num_expect_player_2_trick):
    if num_expect_user_trick>=num_expect_player_2_trick and num_expect_user_trick>=num_expect_player_3_trick:
        first_player_number=1
    elif num_expect_player_2_trick>=num_expect_player_3_trick and num_expect_player_2_trick>num_expect_user_trick:
        first_player_number=2
    else: first_player_number=3
    return first_player_number


def get_second_player_number(first_player_number):
    if first_player_number !=3:
        second_player_number=first_player_number+1
    else: 
        second_player_number=1 
    return second_player_number

def get_third_player_number(second_player_number):
    if second_player_number !=3:
        third_player_number=second_player_number+1
    else: 
        third_player_number=1
    return third_player_number
        

# if user plays the first card of a trick 
# any card is possible 
def user_plays_a_card(player_1_hand): 
    #make sure input format is valid
    card_played_user=user_card_input()
    #make sure input is valid (should be a card on hand)
    while True:
        if card_played_user not in player_1_hand:
            print("Not a valid card, please play again.")
            card_played_user=user_card_input()
            continue
        else:
            break

    #remove the card from hand after it is played
    player_1_hand.remove(card_played_user)
    return card_played_user

#make sure input format is valid
def user_card_input():
    while True:
        try:
            card_played_user=input("Play a card (eg.Green 10):")
            card_played_user = card_played_user.split()
            card_played_user[1] = int(card_played_user[1])
        except (EOFError, ValueError, IndexError, TypeError, SyntaxError):
            print("Not a valid card, please play again")
            continue
        else:
            break
    return card_played_user



# if user plays the second or third card of a trick
# if the hand contains cards of the trick color, one must play those cards 
# if not, any card can be played 
def user_plays_a_card_b(player_1_hand,first_card_played,trump_color):
    trick_color=first_card_played[0]
    # establish a list for cards with the trick color and check the card played against the list
    card_with_trick_color = []
    for card in player_1_hand:
        if card[0]==trick_color:
            card_with_trick_color.append(card)
    #make sure input format is valid
    card_played_user=user_card_input()
    # make sure the trick color rule is followed
    if card_with_trick_color!=[]:
        while card_played_user not in card_with_trick_color or card_played_user not in player_1_hand:
            print("Not a valid play, please play a card with the trick color:"+str(trick_color))
            card_played_user=user_card_input()
            continue

    #make sure input is valid (should be a card on hand)
    while card_played_user not in player_1_hand:    
        print("Not a valid card, please play again.")
        card_played_user=user_card_input()
        continue


    #remove the card from the hand after it is played 
    player_1_hand.remove(card_played_user)


    return card_played_user
        
# if a player plays the first card of a trick

# any card is possible 
def player_2_plays_a_card(player_2_hand):
    card_played_player_2=choice(player_2_hand)
    player_2_hand.remove(card_played_player_2)
    print("Player 2 played "+ str(card_played_player_2))
    return card_played_player_2

# if user plays the second or third card of a trick
# if the hand contains cards of the trick color, one must play those cards 
# if not, any card can be played 
def player_2_plays_a_card_b(player_2_hand,first_card_played,trump_color):
    #make sure the trick color rule is followed 
    #establish a list for cards with the trick color and check the card played against the list 
    trick_color=first_card_played[0]
    card_with_trick_color=[] 
    #randomly select a card 
    card_played_player_2=choice(player_2_hand)
    for card in player_2_hand:
        if card[0]==trick_color:
            card_with_trick_color.append(card)
    if card_with_trick_color!=[]:
        #if the conditions not met, randam select a card again until conditions fulfilled 
        while card_played_player_2 not in card_with_trick_color:
            card_played_player_2=choice(player_2_hand)
    #announce the play of Player 2 
    print("Player 2 played "+ str(card_played_player_2))
    #remove the card played from the pile 
    player_2_hand.remove(card_played_player_2)
    return card_played_player_2


def player_3_plays_a_card(player_3_hand):
    card_played_player_3=choice(player_3_hand)
    player_3_hand.remove(card_played_player_3)
    print("Player 3 played "+str(card_played_player_3))
    return card_played_player_3

def player_3_plays_a_card_b(player_3_hand,first_card_played,trump_color):
    trick_color=first_card_played[0]
    card_with_trick_color=[] 
    card_played_player_3=choice(player_3_hand)
    for card in player_3_hand:
        if card[0]==trick_color:
            card_with_trick_color.append(card)
    if card_with_trick_color!=[]:
        while card_played_player_3 not in card_with_trick_color:
            card_played_player_3=choice(player_3_hand)
    player_3_hand.remove(card_played_player_3)
    print("Player 3 played "+str(card_played_player_3))
    return card_played_player_3

#cards of the trump color are the highest 
#cards of the trick color are higher than cards with other non-trump colors 
#cards with higher numbers are higher
def get_winner_card(second_card_played,third_card_played,trump_color,first_card_played):
    #check for cards with the trump color 
    #develop trump list
    trump_list=[]
    if trump_color in first_card_played[0]:
        trump_list.append(first_card_played)
    if trump_color in second_card_played[0]:
        trump_list.append(second_card_played)
    if trump_color in third_card_played[0]:
        trump_list.append(third_card_played)
    #look into the trump list if there is anything
    #if the trump list not empty, decide winner based on the len of the list and the numbers of the cards 
    if trump_list!=[]:
        if len(trump_list)==1:
            winner_card=trump_list[0]
        if len(trump_list)==2:
            trump_list_card_1=trump_list[0]
            trump_list_card_2=trump_list[1]
            if trump_list_card_1[1]>trump_list_card_2[1]:
                winner_card=trump_list[0]
            else: 
                winner_card=trump_list[1]
        if len(trump_list)==3:
            trump_list_card_1=trump_list[0]
            trump_list_card_2=trump_list[1]
            trump_list_card_3=trump_list[2]
            if trump_list_card_1[1]>trump_list_card_2[1] and trump_list_card_1[1]>trump_list_card_3[1]:
                winner_card=trump_list[0]
            elif trump_list_card_2[1]>trump_list_card_1[1] and trump_list_card_2[1]>trump_list_card_3[1]:
                winner_card=trump_list[1]
            else:
                winner_card=trump_list[2]
    #if there is not cards with trump color, need to check for cards with the trick color
    else: 
        #the first card played must be on the trick color list 
        trick_color_list=[first_card_played]
        trick_color=first_card_played[0]
        if second_card_played[0]==trick_color:
            trick_color_list.append(second_card_played)
        if third_card_played[0]==trick_color:
            trick_color_list.append(third_card_played)
        #decide winner based on the len of the list and the numbers of the cards 
        if len(trick_color_list)==1:
            winner_card=first_card_played
        if len(trick_color_list)==2:
            trick_color_card_1=trick_color_list[0]
            trick_color_card_2=trick_color_list[1]
            if trick_color_card_1[1]>trick_color_card_2[1]:
                winner_card=trick_color_list[0]
            else:
                winner_card=trick_color_list[1]
        if len(trick_color_list)==3:
            trick_color_card_1=trick_color_list[0]
            trick_color_card_2=trick_color_list[1]
            trick_color_card_3=trick_color_list[2]
            if trick_color_card_1[1]>trick_color_card_2[1] and trick_color_card_1[1]>trick_color_card_3[1]:
                winner_card=trick_color_list[0]
            elif trick_color_card_2[1]>trick_color_card_1[1] and trick_color_card_2[1]>trick_color_card_3[1]:
                winner_card=trick_color_list[1]
            else: 
                winner_card=trick_color_list[2]
    return winner_card 

# if a bid is correct, total score of a player + (20+ bid value*10)  
# if a bid is incorrect, total score of a player -(difference*10)
def cal_total_score(total_score_user,total_score_player_2,total_score_player_3,total_won_trick_user,total_won_trick_player_2,total_won_trick_player_3,num_expect_user_trick,num_expect_player_2_trick,num_expect_player_3_trick):
    #total score of the user
    #if bid correct 
    if total_won_trick_user==num_expect_user_trick:
        total_score_user+=(20+(num_expect_user_trick*10))
    #if bid not correct
    else:
        total_score_user-=abs((total_won_trick_user-num_expect_user_trick)*10)
    #total score of player 2
    if total_won_trick_player_2==num_expect_player_2_trick:
        total_score_player_2+=(20+(num_expect_player_2_trick*10))
    else:
        total_score_player_2-=abs((total_won_trick_player_2-num_expect_player_2_trick)*10)
    #total score of player 2
    if total_won_trick_player_3==num_expect_player_3_trick:
        total_score_player_3+=(20+(num_expect_player_3_trick*10))
    else:
        total_score_player_3-=abs((total_won_trick_player_3-num_expect_player_3_trick)*10)
    return total_score_user,total_score_player_2,total_score_player_3

def get_winner(total_score_user,total_score_player_2,total_score_player_3):
    if total_score_user>total_score_player_2 and total_score_user>total_score_player_3:
        print("Congratulations!You are the winner!")
    elif total_score_player_2>total_score_user and total_score_player_2>total_score_player_3:
        print("Player 2 is the winner! Try again next time!")
    elif total_score_player_3>total_score_user and total_score_player_3>total_score_player_2:
        print("Player 3 is the winner! Try again next time!")
    elif total_score_user==total_score_player_2 and total_score_player_2>total_score_player_3:
        print("This is a draw between you and Player 2!")
    elif total_score_user==total_score_player_3 and total_score_player_3>total_score_player_2:
        print("This is a draw between you and Player 3!")
    else: 
        print("This is a draw between Player 2 and Player 3!d Try again next time!")




if __name__ == '__main__':
    main()
