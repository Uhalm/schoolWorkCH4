#Paul Mann
#Import Things
import os;
import time;
import platform;

#system variables
opsys = 'Tux';
clear = 'Tux';

### software variables
##constants
#tuition constant
BASE_TUITION = 8000;
#present of tuition each year
PRESENT_UP = 0.03

##changeing variables
#tuition
tuition = 0;

#function to check the operating system
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
        
#loop function        
def loop():
    #call the globals
    global tuition;
    tuition = BASE_TUITION;
    years = 0
    #clear the screen
    os.system(clear);
    #print the 1 time print items
    print('Years    | Tuition');
    print('=========|========');
    #the for loop
    for years in range (0, 6):
        #print the years and tuition
        print(years,  '       |',  format( tuition,  ',.2f'), '＄');
        #add to the year counter
        tempYear = years + 1;
        years = tempYear
        #calculate the tuituion increase
        increase = tuition * PRESENT_UP;
        #add to the tuition
        #print(tempYear,  increase);
        temp = tuition + increase;
        tuition = temp;
        
        
osCheck();
loop();
