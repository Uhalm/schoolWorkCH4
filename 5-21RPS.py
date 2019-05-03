#Paul Mann
#Rock Paper Scissors
#5-21
#import libraries
import time;
import random;
import os;
import platform;

#DEBUGING
#import pdb;
#pdb.set_trace()


#set the global constants that will be set later
clear = 'Tux';
opsys = 'Tux';
#set the global constants that will be set now
options1 = [1,  2,  3];
#set the variables that will keep track of the users score
userPoints = 0;
aiPoints = 0;

#function to set the clear and opsys variable depending on the operating system user is running
def osCheck():
    #call the global variables
    global clear;
    global opsys;
    
    #check what operating system user is running and set opsys to that
    opsys = platform.system().lower();

    #if os is windows
    if opsys == 'windows' or opsys == 'win32':
        #set clear to clear command
        clear = 'cls';
        #set terminal to black back and green text
        os.system('color 0A');
        #set terminal window title to Rock Paper Scissors!
        os.system('TITLE Rock Paper Scissors!');
		#goto main fucntion
        
    #if os is linux
    elif opsys == 'linux' or opsys == 'linux1' or opsys == 'linux2':
        #set clear to clear command
        clear = 'clear';
        #error fix
        os.system('set | grep TERM'); 
        #goto main function
        
    #if os is not windows or linux
    else:
        #print error
        print('You are using a incompatable operating system.\nPlease use Linux or Windows.');
        #sleep so user reads the message
        time.sleep(5)
	
	
    
#main function    
def main():
    #clear the screen
    os.system(clear);
    #run the function to print the user interface
    mainUI();
    #try this code block
    try:
        #get user input
        userIn = int(input('Input the number of your option\n>>>'));
        #make sure user input is valid
        if userIn in options1:
            #run RPS function
            RPS();
            #run the ai fucntion
            aiGo(userIn);
        
        #if user wants to exit
        elif userIn == 4:
            os.system(clear);
            print('Exiting');
            time.sleep(1.5);
            exit();
            
        else:
            print('Please enter a valid option.');
            time.sleep(1.5);
        
        
    #if code in try: caused a ValueError then do this
    except ValueError:
        #print error
        print('Please input one of the options');
        #sleep for 1.5 seconds
        time.sleep(1.5);



#the function that stores the user interface
def mainUI():
    print('Rock Paper Scissors - PYTHON');
    print('============================');
    print('SCORE:');
    print('You:',  userPoints);
    print('Computer:',  aiPoints);
    print('============================');
    print('1. Rock');
    print('2. Paper');
    print('3. Scissors');
    print('4. Exit');
    print('============================');


#Print Rock Paper Scissors
def RPS():
    os.system(clear);
    print('Rock!');
    time.sleep(0.5);
    print('Paper!');
    time.sleep(0.5);
    print('Scissors!');
    time.sleep(0.5);
    
#have the AI pick Rock Paper or Scissors
def aiGo(usr):
    #clear the screen
    os.system(clear);
    #generate a random number between 1 and 3
    ai = random.randint(1, 3);
    #check who won
    whoWon(usr, ai);

#check who won
def whoWon(usr, ai):
    #DEBUG
    #print(ai)
    #print(usr)    
    #check who won
    #UI vs USER
    #Rock vs Rock
    if ai == 1 and usr == 1:
        draw();

    #Rock vs Paper
    elif ai == 1 and usr == 2:
        userWin();
        
    #Rock vs Scissors
    elif ai == 1 and usr == 3:
        aiWin();
        
    #Paper vs Rock
    elif ai == 2 and usr == 1:
        aiWin();
        
    #Paper vs Paper    
    elif ai == 2 and usr == 2:
        draw();
        
    #Paper vs Scissors
    elif ai == 2 and usr == 3:
        userWin();
    
    #Scissors vs Rock
    elif ai == 3 and usr == 1:
        userWin();⎄
    #Scissors vs Paper
    elif ai == 3 and usr == 2:
        aiWin();
        
    #Scissors vs Scissors
    elif ai == 3 and usr == 3:
        draw();
        
    else:
        print('FATAL ERROR ABORTING');
        exit();
    

#if ai wins
def aiWin():
    #call the global
    global aiPoints
    #print the computer wins
    print('Computer wins');
    #add 1 to the ai points
    aiPoints += 1;
    #print the points
    print('AI', aiPoints, 'You',  userPoints);
    #sleep for 1.5 seconds
    time.sleep(1.5);
    
def userWin():
        #call the global
    global userPoints
    #print the user wins
    print('You win');
    #add 1 to the users points
    userPoints += 1;
    #print the points
    print('AI', aiPoints, 'You',  userPoints);
    #sleep for 1.5 seconds
    time.sleep(1.5);
    
#if the match is a draw
def draw():
    #say its a draw
    print('DRAW!');
    #sleep for 1.5 seconds
    time.sleep(1.5);
    
    
def mainFun():
    while True:
        main();

osCheck();
mainFun();
