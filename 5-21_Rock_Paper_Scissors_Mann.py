#Paul Mann
#Rock Paper Scissors
#5-21
#import libraries
import time;
import random;
import os;
import platform;


#set the global variables
clear = 'Tux';
opsys = 'Tux';


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
    os.sytem(clear);
    #run the function to print the user interface
    mainUI();
    #try this code block
    try:
        #get user input
        userIn = int(input('Input the number of your option\n>>>'));
        #run the function to check what the user input
        aiGo(userIn);
        
        
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
    print('1. Rock');
    print('2. Paper');
    print('3. Scissors');
    print('4. Exit');
    print('============================');


def aiGo(usr):
    ai = random.ranint(1, 3);
    whoWon(usr, ai);


def whoWon(usr, ai):
    print(usr, ai);
    time.sleep(1.5);

def mainFun():
    while True:
        main();

osCheck();
mainFun();