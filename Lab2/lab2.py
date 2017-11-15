#list = ["p","o","o","p"]
#def poop(list):
#	return [list[0],list[-1]]
#print (poop(list))
#
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in range(len(a)):
#	if a[i] < 5:
#		print (a[i])
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#new_list = []
#for i in range(len(a)):
#	if a[i] in b:
#		new_list.append(a[i])
#print(new_list)
x = 0
number = int(input("Please enter a natural number:"))
for i in range(2,int(number/2)):
	if number % i == 0:
		x += 1
if x == 0:
	print("The number is indeed prime")
else:
	print("The number is not prime")
