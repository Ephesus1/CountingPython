# count.py
# prog to ask uder for name and nummber, then count by 2's

print ('Hello We Are Counting By 2*s Right Nah')


while True:
	myName = input('Your name? ')
	if myName.isalpha():
		print("Whats hannin " + myName)
		break
	else:
		print("This Has Something Other Then Letters")
		
	
while True:
	endNum = input('Enter a number: ')
	if (endNum.isdigit()):
		if int(endNum) > 1000:
			print("It's over 1000")
		else:
			print("That Is A Number")
			endNum=int(endNum)
			input('So you really trying to count to ' + str(endNum) + ' -press Enter to start :')
			for x in range(0, endNum+1,20):
				print(x)
			print('Your Welcome!')
			break
	else:
		print("That Is Not A Number")


# input('So you really trying to count to ' + str(endNum) + ' -press Enter to start :')

# for x in range(1, endNum+1,2):
# 	print(x)

# print('Your Welcome!')