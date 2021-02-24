#!/usr/bin/python
import getpass
import string
import os

# creatinga lists of users, their PINs and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
n100 = 2
n500 = 5
n1000 = 5
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
	else:
		print('------------------------')
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		print('------------------------')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('-----------------------------------')
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	print('-----------------------------------')
	exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome to PTB ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement_____(S) \nWithdraw______(W) \nLodgement_____(L) \nTransfer______(T)  \nChange PIN____(P)  \nQuit__________(Q) \n: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 't' , 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'BATH ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		input_cash = input('SELECT WITHDRAW MONEY FOLLOWING : \n100 BATH______(A) \n500 BATH______(B) \n1000 BATH_____(C) \n5000 BATH_____(D) \n10000 BATH____(E) \nSPECIFY NUMBER___(I) \n: ').lower()
		print('---------------------------------------------')
		print('*********************************************')
		valid_input = ['a', 'b', 'c' , 'd', 'e', 'i']
		input_cash = input_cash.lower()
		if input_cash == 'a':
			cash_out = 100
		elif input_cash == 'b' :
			cash_out = 500
		elif input_cash == 'c' :
			cash_out = 1000	
		elif input_cash == 'd' :
    			cash_out = 5000	
		elif input_cash == 'e' :
    			cash_out = 10000
		elif input_cash == 'i' :	
				cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
				print('*********************************************')
				print('---------------------------------------------')
		
		if cash_out%100 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100,500,1000 BATH NOTES')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
			print('-----------------------------')
		elif 100 > cash_out or cash_out > 20000 :
			print('-----------------------------------------------------')
			print('*****************************************************')
			print('YOU CAN WITHDRAW MONEY IN THE RANGE OF 100-2000 BATH ')
			print('*****************************************************')
			print('-----------------------------------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			b1000 = cash_out//1000
			b500 = (cash_out%1000)//500
			b100 = (cash_out%500)//100
			if b100 > n100 :
				print('*************************************************************')
				print('ATM NOT ENOUGH 100 NOTES ONLY HAVE NOTE FOR 500 AND 1000 BATH')
				print('*************************************************************')
			elif b500 > n500 :
				print('*****************************************************')
				print('ATM NOT ENOUGH 500 NOTES ONLY HAVE NOTE FOR 1000 BATH')
				print('*****************************************************')
			elif b1000 > n1000 :
				print('****************************')
				print('ATM NOT ENOUGH MONEY FOR YOU')
				print('****************************')			

			else:		
				print('YOU WITHDRAW AMOUNT IS', cash_out , 'BATH')
				print('YOU GET 100 BATH :' ,b100, 'NOTES')
				print('YOU GET 500 BATH :' ,b500, 'NOTES')
				print('YOU GET 1000 BATH :' ,b1000, 'NOTES')
				print()
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'BATH')
				print('***********************************')
				print('-----------------------------------')    		

	elif response == 'l':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print('*********************************************')
		print('---------------------------------------------')

		print()
		if cash_in%100 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 100,500,1000 BATH NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			b1000_in = cash_in//1000
			b500_in = (cash_in%1000)//500
			b100_in = (cash_in%500)//100
			print('----------------------------------------')
			print('****************************************')
			print('YOU PUT 100 BATH :' ,b100_in, 'NOTES')
			print('YOU PUT 500 BATH :' ,b500_in, 'NOTES')
			print('YOU PUT 1000 BATH :' ,b1000_in, 'NOTES')
			print()
			print('----------------------------------------')
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'BATH')
			print('****************************************')
			print('----------------------------------------')

	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN MISMATCH')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('-------------------------------------')

	elif response == 't':
		bank = str(input('SELECT BANK FROM FOLLOWING : \nKBank______(KS) \nIbanking___(BBL) \nSCB Easy___(SCB) \nOther________(O) \n: ')).lower()
		valid_bank = ['ks', 'bbl', 'scb' , 'o']
		bank = bank.lower()
		if bank == 'ks':
			print('----------------------------------------------------')
			print('****************************************************')
			acount_id = int(input('ENTER KASIKORN ACCOUNT ID: '))	
			print('----------------------------------------------------')
			print('****************************************************')
			amount_trans = int(input('ENTER AMOUNT YOU WANT TO TRANSFER: '))
			print()

			amounts[n] = amounts[n] - amount_trans
			print('----------------------------------------------------')
			print('****************************************************')
			print('YOUR ARE SUCCESSFUL TRANSFER : \nBANk : KASIKORN \nACCOUNT_ID : ',acount_id, '\nAMOUNT_TRANSFER :' ,amount_trans, 'BATH' )
			print('YOUR LEDGER BALANCE IS: ', amounts[n], 'BATH')
			print('****************************************************')
			print('----------------------------------------------------')	
		elif bank == 'bbl':
			print('----------------------------------------------------')
			print('****************************************************')
			acount_id = int(input('ENTER BUALUANG ACCOUNT ID: '))	
			print('----------------------------------------------------')
			print('****************************************************')
			amount_trans = int(input('ENTER AMOUNT YOU WANT TO TRANSFER: '))
			print('----------------------------------------------------')
			print('****************************************************')
			print()

			amounts[n] = amounts[n] - amount_trans
			print('----------------------------------------------------')
			print('****************************************************')
			print('YOUR ARE SUCCESSFUL TRANSFER : \nBANk : BUALUANG \nACCOUNT_ID : ',acount_id, '\nAMOUNT_TRANSFER :' ,amount_trans, 'BATH' )
			print('YOUR LEDGER BALANCE IS: ', amounts[n], 'BATH')
			print('****************************************************')
			print('----------------------------------------------------')
		elif bank == 'scb':
			print('----------------------------------------------------')
			print('****************************************************')
			acount_id = int(input('ENTER SIAM COMERCAIL BANK ACCOUNT ID: '))	
			print('----------------------------------------------------')
			print('****************************************************')
			amount_trans = int(input('ENTER AMOUNT YOU WANT TO TRANSFER: '))
			print('----------------------------------------------------')
			print('****************************************************')
			print()

			amounts[n] = amounts[n] - amount_trans
			print('----------------------------------------------------')
			print('****************************************************')
			print('YOUR ARE SUCCESSFUL TRANSFER : \nBANk : SIAM COMERCAIL BANK \nACCOUNT_ID : ',acount_id, '\nAMOUNT_TRANSFER :' ,amount_trans, 'BATH' )
			print('YOUR LEDGER BALANCE IS: ', amounts[n], 'BATH')
			print('****************************************************')
			print('----------------------------------------------------')
		elif bank == 'o':
			print('----------------------------------------------------')
			print('****************************************************')
			morebank = str(input('ENTER BANK NAME: '))
			print('BANK NAME :',morebank)
			acount_id = int(input('ENTER BANK ACCOUNT ID: '))	
			print('----------------------------------------------------')
			print('****************************************************')	
			amount_trans = int(input('ENTER AMOUNT YOU WANT TO TRANSFER: '))
			print('----------------------------------------------------')
			print('****************************************************')
			print()

			amounts[n] = amounts[n] - amount_trans
			print('----------------------------------------------------')
			print('****************************************************')
			print('YOUR ARE SUCCESSFUL TRANSFER : \nBANk : ',morebank, ' \nACCOUNT_ID : ',acount_id, '\nAMOUNT_TRANSFER :' ,amount_trans, 'BATH' )
			print('YOUR LEDGER BALANCE IS: ', amounts[n], 'BATH')
			print('****************************************************')
			print('----------------------------------------------------')
		else :
			print('------------------')
			print('******************')
			print('PLEASE TRY AGAIN')
			print('******************')
			print('------------------')
    	  
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
