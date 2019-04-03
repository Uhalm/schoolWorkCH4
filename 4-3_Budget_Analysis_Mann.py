#Paul Mann
import time;
import os;
import platform;

#system variables
opsys = 'Tux';
clear = 'Tux';

#set the software variables
budget = 0;
expenses = 0;


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
        
        

def budgetGet():
    #clear the screen
    os.system(clear);
    #call the budget function
    global budget;
    #get the budget 
    print('Input the budget for the month (30 day period)');
    try:
        budget = float(input('>>>'));
        looper();
        
    except ValueError:
        print('Please input a number.');
        time.sleep(1.75);
        budgetGet();
        
#the loop        
def looper():
    global expenses;
    #clear the screen
    os.system(clear);
    #set days to 1
    days = 1;
    #create a loop
    while days <= 30:
       #clear screen 
        os.system(clear);
        #print the instructions
        print('Input the amount of money spent each day.')
        print('Day',  days);
        print('Curent expenses',  format(expenses,   ',.2f'),  '$');
        print('Budget',  format(budget,  ',.2f'),  '$');
        #get the money to add to the expenses
        try:
            adder = float(input('>>>'));
            #add adder to expenses
            tempEx = adder + expenses;
            expenses = tempEx;
            #add to the days
            tempDay = days + 1;
            days = tempDay;
            
        except ValueError:
            print('Please input a number');\
            time.sleep(1.5);
            
    printer();
    
    
def printer():
    #call the globals
    global budget;
    global expenses;
    #check if under or over budget
    if expenses > budget:
        ou = 'over budget';
    else:
        ou = 'under budget';
        
    #clear the screen
    os.system(clear);
    #print the results    
    print('Your budget was',  format(budget,  ',.2f'),  '$');
    print('You spent',  format(expenses,  ',.2f'),  '$');
    print('You are',  ou);
    #wait 5 seconds
    time.sleep(5);
    #reset the variables
    budget = 0;
    expenses = 0;
    #restart the program
    budgetGet();
    
osCheck();
budgetGet();
