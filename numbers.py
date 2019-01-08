no1 = input("Enter first operand")
no2 = input("Enter second operand")
ch=0
while ch<7:
	print("1.Addtion \n 2.Subtraction \n 3.Division \n 4.Multiplication \n 5.Modulus \n 6.Integer Division")

	ch = input("Enter your choice")

	if ch==1 :
		print(no1+no2)
	elif ch==2 :
		print(no1-no2)
	elif ch==3 :
		print(no1/no2)
	elif ch==4 :
		print(no1*no2)
	elif ch==5 :
		print(no1%no2)
	elif ch==6 :
		print(no1//no2)
	else:
		print("Wrong choice")
		break;

