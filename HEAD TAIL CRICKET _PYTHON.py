import random # importing random module for playing game with computer
#First code block for the introduction for the game
n=input("Enter your name: ")
print(f"Hello {n} you are going to play'HEADS AND TAILS CRICKET'")
R=input("Do you know the rules(yes/no)")
if R =='no': #if R is no then the rules will be shown to the user 
    #zaryab.txt is a text file containing rules of the game
    rules=open("zaryab.txt","r") # The variable rules will open the file (zaryab.txt)
    data = rules.read()#Data is a variable which read the rules from the file zaryab.txt
    print(data) #This will print text read by the variable data in the output 
    rules.close()#After printing the text from the file the file will be close
elif R == 'yes':
    pass #Nothing will be executed when elif statement is true.  
print("STARTING THE GAME.....")
    
def toss(): # function for toss   
    l1=['heads','tails']# Choices for a toss
    x=input("Enter the choice_1(heads/tails) for toss: ")
    r1=random.choice(l1)#r1 is a variable which choose random value from l1
    try:
        if x == 'heads':        
            y ='tails'
        elif x == "tails":
            y='heads'
        if x == r1:   #when the choice of player is equal to r1 then the player will win the toss 
            print(f'{n} won the toss')
            return 'player 1'
        elif y == r1: # when the if statement is false then  the computer will win the toss 
            print('computer won the toss') 
            return 'computer'
    except:
        print("you have give incorrect input in toss")
        print("make the input given in bracket")

run=[1,2,3,4,5,6,10]#list for the input of run
def person_batting():#This function execute when person won toss and choose batting
    player_run=[]#empty list which will be used below in the function
    print("Start batting!")
    while True:
        a=input("enter the number for run(1-6 or 10): ")# variable for taking user input for scoring run
        batting_run=int(a)
        Computer_balling=random.choice(run)# random input for computer balling
        if (batting_run == Computer_balling):
        # when this con.statement become true then the while loop will break
            break
        if batting_run in run: 
        #when the input of a is present in the [run] then the input will be added in the [player_run]
            player_run.append(batting_run)
        else:
            print("if you want to make 'runs' enter the number (1-6 or 10)")
    print(player_run)#print the total list of player_run after batting
    add=0
    for i in player_run:# the loop to sum the [player_run]
        add=add+i
    total_score=add #variable to show total sum of[player_run]
    print(f"you have give the target of {total_score+1}")
    return total_score+1 # This return target for computer 

def person_balling(x):#This function execute when person won toss and choose balling
    computer_run=[]#empty list which will be used below in the function
    total_score=0# a variable for counting the runs scored by computer
    print("Start Balling!")
    test=True
    while test:#This loop will execute untill the test is True 
        a=input("enter the number for balling(1-6 or 10): ")# variable for taking user input for scoring run
        Balling=int(a)
        Computer_batting=random.choice(run)#random input for computer batting
        if (Balling == Computer_batting):# when this con.statement become true then the while loop will be false
            computer_run.pop(-1)#this will remove the last index of [computer_run]
            if total_score<x:
                print("person wons")
            test=False
        elif total_score>=x:# when this con.statement become true then the while loop will be false
            print("computer wons")
            test=False
        if Balling in run:
    #when the input of a is present in the [run] then input of computer_batting will be added in the [computer_run]
            computer_run.append(Computer_batting)
        else:
            print("if you want to out the computer enter the number (1-6 or 10)")
        add=0
        for i in computer_run:# the loop to sum the [computer_run]
            add=add+i
        total_score=add #variable to show total sum of [computer_run]
    print(computer_run) #print the total list of computer_run after batting
    print(f"computer have scored {total_score} run")
    return total_score
def game_first_batting():#function execute when the player got first batting*
    r=person_batting()
    l=person_balling(r)
    return r
    
def computer_batting():#This function execute when computer won toss and choose batting
    computer_run=[]#empty list which will be used below in the function
    print("Start balling !")
    while True:
        a=input("enter the number for balling(1-6 or 10): ")# variable for taking user input for scoring run
        Balling=int(a)
        Computer_batting=random.choice(run)#random input for computer batting
        if (Balling == Computer_batting):# when this con.statement become true then the while loop will break
            break
        if Balling in run:
    #when the input of a is present in the [run] then input of computer_batting will be added in the [computer_run]    
            computer_run.append(Computer_batting)
        else:
            print("if you want to out the computer enter the number (1-6 or 10)")
    print(computer_run)#print the total list of computer_run after batting
    add=0
    for i in computer_run:# the loop to sum the [computer_run]
        add=add+i
    total_score=add#variable to show total sum of [player_run]
    print(f"You have given the Target of {total_score+1}")
    return total_score+1 # This return target for computer
def computer_balling(x):#This function execute when computer lost toss and choose batting
    total_score=0
    player_run=[]#empty list which will be used below in the function
    print("Start Batting!")
    test=True
    while test:
        a=input("enter the number for run(1-6 or 10): ")# variable for taking user input for scoring run
        Batting=int(a)
        Computer_batting=random.choice(run)
        if (Batting == Computer_batting):# when this con.statement become true then the while loop will be false
            player_run.pop(-1)
            if total_score<x:
                print("computers wons")
            test=False
        if total_score>=x:# when this con.statement become true then the while loop will be false
            print("player wons")
            test=False
        if Batting in run:
        #when the input of a is present in the [run] then the input will be added in the [player_run]
            player_run.append(Batting)
        else:
            print("if you want to make run! enter the number (1-6 or 10)")
        total_score=sum(player_run)#variable to show total sum of [player_run]

    print(player_run)#print the total list of player_run after batting
    print(f"you have score {total_score} runs")
    return total_score
def game_second_batting():##function execute when the player got second batting*
    r=computer_batting()
    l=computer_balling(r)
    return l
#second code block for logics
toss_winner=toss()
b_b=['bat','ball']
score = 0
try:
    if toss_winner == 'player 1':
        try:
            choice=input("enter your choice (batting or balling): ")
            if(choice!="batting" and choice !="balling"):
                raise Exception("invalid choice")
        except:
            choice=input("enter the choice again which is given in bracket(batting or balling):")
        if choice == "batting":
           score=game_first_batting()
        elif choice == 'balling':
           score=game_second_batting()
    elif toss_winner == 'computer':
        choice=random.choice(b_b)
        print(f'computer decide to {choice} first')
        if choice == 'bat':        
           score=game_second_batting()
        elif choice == "ball":
           score=game_first_batting()
    with open("hi_score.txt") as f:        
        hi_score=f.read()
        data=int(hi_score)     
        if data<score:       
            print(f"Congrats you have made high score previous score is {data}")
            with open("hi_score.txt","w") as f:
                f.write(f"{score}")    
    print('game over! thanks for playing')
    
except:
    print("play the game correctly")
    
