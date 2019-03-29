#Paul Mann
#Import Libraries
import os;
import time;
import platform;

#OS Spicific values
clear = 'Tux';
opsys = 'Tux';

#globals
sum = 0;
num = 0;



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
	#call the globals
	global num;
	global sum;
	
	#reset sum
	sum = 0;
	
	#infinate loop
	while('true'):
		#clear screen
		os.system(clear);
		#print the current sum
		print('Curent sum', sum);
		#print the instructions 
		print('Input a positive number to add input a negative to quit');
		
		
				#try this
		try:
			#get the user input
			num = int(input('>>>'));
		

#			#check if the number is greater than 0
			if float(num) > 0:
				adder();
			#break the loop
			elif float(num) < 0:
				break;
			#fallback error
			else:
				print('imposible error');
			
		#if the input is not a number
		except TypeError:
				print('Please read the instructions fuck-tard');
				time.sleep(5);
				
				
		except ValueError:
			print('ValueError');
			time.sleep(5);
	
	#print results
	printer();
	
	
#add the input to the sum
def adder():
	#call the sum variable
	global sum;
	#add sum and num and put the result in tempSum
	tempSum = sum + num;
	#make sum = to sum
	sum = tempSum;
	
	#function to print the results
def printer():
	#clear the screen
	os.system(clear);
	#print the result
	print('The sum of all the numbers is', sum);
	#sleep
	time.sleep(5);
	#goto main function
	main();
		
osCheck();
main();
