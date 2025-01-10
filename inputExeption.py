while True:
	try:
		x = int(input("what is youur age?"))
		break
	except:
		print("Please Enter the valid number")
	finally:
	
		print("your  age is: ", x)
