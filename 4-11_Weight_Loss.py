#Paul Mann
#import things
import os;
import time;
import platform;

#constants
#pounds per month
PPM = 4;

#user input variables
userWeight = 0;

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


#function to get the user input
def userInput():
    #call the globals
    global userWeight;
    #clear the screen
    os.system(clear);
    
    #print the instructions
    print('Please enter your current weight.');
    #try this
    try:
        #get the input
        userWeight = float(input('>>>'));
        loop();
        
    except ValueError:
        print('Please input a number');
        time.sleep(1.5);
        userInput();
        
#the loop function
def loop():
    #clear the screen
    os.system(clear);
    #print the things that won't be printed multiple times
    print('Months   | Weight');
    print('=========|=======');
    print('Current  |',  format(userWeight,  ',.2f'),  'lbs');
    
    #set the weight variable to 4 less than userWeight
    weight = userWeight - PPM
    #set the counter to 0
    months = 1;
    
    #for loop
    for months in range (1,  7):
        #print the months passed and the weight of the user
        print(months,  '       |',  format(weight,  ',.2f'),  'lbs');
        #subtact 4 pounds from the users weight
        temp = weight - PPM;
        weight = temp;
    
osCheck();
userInput();
userInput();
