import os

index_list=[1,2,3,4,5,6,7,8,9]
choice =0
player=1
c='c'

#Display the tic tac tor board with the index numbers in each box

def display_board():
    print("\t\t    |    |     ")
    print("\t\t  {} | {}  | {}  ".format(index_list[6],index_list[7],index_list[8]))
    print("\t\t____|____|_____")
    print("\t\t    |    |     ")
    print("\t\t  {} | {}  | {}  ".format(index_list[3],index_list[4],index_list[5]))
    print("\t\t____|____|_____")
    print("\t\t    |    |     ")
    print("\t\t  {} | {}  | {}  ".format(index_list[0],index_list[1],index_list[2]))
    print("\t\t    |    |     ")
	

#Take inpur the user choice and display it on the board
def user_choice():

    choice=False
    global player
	
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        if player%2==0:
            choice=input("O's turn:")
            if choice not in ['1','2','3','4','5','6','7','8','9']:
                os.system('cls')
                print("Invalid choice\n")
                display_board()
        else:
            choice=input("X's turn:")
            if choice not in ['1','2','3','4','5','6','7','8','9']:
                os.system('cls')
                print("Invalid choice\n")
                display_board()
		    
    return int(choice)	


#change the index value to the user input
  
def change_index(choice):
        global player
        if player%2==0:
            index_list[choice-1]='O'
        else:
            index_list[choice-1]='X'
        player=player+1
        os.system('cls')
        display_board()
        
# Check for different conditions that may arise during the game

def condition():
    global c
    if index_list[0]==index_list[1] and index_list[1]==index_list[2]:
        return index_list[0]
    elif index_list[3]==index_list[4] and index_list[4]==index_list[5]:
        return index_list[3]
    elif index_list[6]==index_list[7] and index_list[7]==index_list[8]:
        return index_list[6]
    elif index_list[0]==index_list[3] and index_list[3]==index_list[6]:
        return index_list[0]
    elif index_list[1]==index_list[4] and index_list[4]==index_list[7]:
        return index_list[1]
    elif index_list[2]==index_list[5] and index_list[5]==index_list[8]:
        return index_list[2]
    elif index_list[0]==index_list[4] and index_list[4]==index_list[8]:
        return index_list[0]
    elif index_list[2]==index_list[4] and index_list[4]==index_list[6]:
        return index_list[2]
    else:
        return c

#Call all the functions in proper order

def play_game():
    play_choice='y'
    global result
    global player
    global c
    global choice
    global index_list
    while play_choice=='y':
        os.system('cls')
        index_list=[1,2,3,4,5,6,7,8,9]
        choice =0
        player=1
        c='c'
        while player<=9:
            os.system('clear')
            display_board()
            choice=user_choice()
            change_index(choice)
            result=condition()
            if result=='c':
                continue
            elif result in ['X','O']:
                print("\n\tPlayer {} won".format(result))
                print("\n\n\t-----GAME OVER-----")
                print("\n\n\t--THANK YOU FOR PLAYING--")
                break
        if player>9:
            print("\n\t\t----MATCH DRAW----")
        play_choice=input("\n\n\t Want to play again (y/n):")
    
        
    
    
    
    
play_game()
  
    


