#Paul Mann
#Import things
import time;
import os;
import platform;

#software variables
opsys = 'Tux';
clear = 'Tux';

#Constant variables
CPM = 4.2;

#check the os
def osCheck():
    #call the global variables
    global opsys;
    global clear;
    #get the operating system and asign it to opsys
    opsys = platform.system();
    #check if os is compatable
    
    #if linux
    if opsys.lower() == 'linux' or opsys.lower() == 'linux2':
        #clear command is clear
        clear = 'clear';
        
    #if windows
    elif opsys.lower() == 'win' or opsys.lower() == 'windows':
        clear = 'cls';
        os.system('color 0A');
   
   #what to do if os uncompatable
    else:
        #print the error
        print('Your Operating System is not a compatable OS');
        print('Please use a Windows or Linux Operating System');
        #wait for 6000000 seconds
        time.sleep(600000);
        exit();



#main function
def main():
    #clear the screen
    os.system(clear);
    #timer is the accumulator 5 will be added every time
    timer = 10;
    #print the one time print UI
    print('Time | Calories');
    print('-----|---------');
    #for loop
    for timer in range (5,  31, +5):
        #add 5 minutes to timer
        tempTimer = timer + 5;
        timer = tempTimer;
        #calculate the calories
        calories = timer * CPM;
        #print the time and calories
        print(timer, '  | ',  calories);
        
    #wait 5 seconds
    time.sleep(5);
    #exit
    exit();


osCheck();
main();
