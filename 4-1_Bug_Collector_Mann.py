#Paul Mann
#Import Things
import platform;
import time;
import os;

#define globals
bugs = 0;


#OS Spicific Values
opsys = 'Tux';
clear = 'Tux';


#check what OS the computer is running so things work correctly# 
def osCheck():
#call the global variables#
	global clear;
	global opsys;
#get the Operating System#
	opsys = platform.system();
	#opsys = 'Free BSD'; #TEST LINE TO MAKE SURE THAT SLEEPING FOR 604800 SECONDS WILL NOT CAUSE OVERFLOW ERROR#
#check if the OS is windows#
	if opsys.lower() == 'win' or opsys.lower() == 'win32' or opsys.lower() == 'windows':
#set the command to clear the screen#
		clear = 'cls';
#set the command to change the text to green#
		os.system('color 0A');
#check if the OS is a linux device#
	elif opsys.lower() == 'linux' or opsys.lower == 'linux1' or opsys.lower == 'linux2' or opsys.lower == 'linux3':
#set the command to clear the screen#
		clear = 'clear';
#do this if not windows or linux#
	else:
#print a message saying to use windows or linux#
		print("Please use a Windows or Linux device to run this program");
#sleep indefinetly (for a week)#
		time.sleep(604800);
		
		
		
		

#main function
def main():
	#call the bugs variable
	global bugs;

	#reset bugs
	bugs = 0;
	#set acumulator
	x = 0;
	#try
	try:
	#for loop
		for x in range(1, 6):
			#clear screen
			os.system(clear);
			#print the day
			print('Input the number of bugs caught on day', x);
			#get user input
			adder = input('>>>');
			#add adder to bugs
			tempBugs = int(bugs) + int(adder);
			#set the temp as the main
			bugs = int(tempBugs);
			#add to the acumulator
			xTemp = int(x) + int(1);
			#set the temp to the main
			x = int(xTemp);
			#
			#print(bugs, x);#TEST LINE TO CHECK IF THE VARIABLES WORK
	
		else:
			printer();
	
	except ValueError:
		print('Please input only numbers');
		time.sleep(5);
		main();

		
	except TypeError:
		print('TypeError');
		time.sleep(5);
		main();
		


def printer():
	os.system(clear);
	print('Over 5 days you caught', bugs, 'bugs');
	time.sleep(5);
	main();
		
		
osCheck();
main();