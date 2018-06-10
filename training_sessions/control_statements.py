def m1():
	print("Use of return... It will return out of block....")
	for value in range(1,10):
		print(value)
		if value == 5:
			return
		print("after if")
	print("for completed.....")
m1()

