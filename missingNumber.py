#Missing Number Problem
#Given an array and the fact that array should go from 1 to N
#Find the missing number in the array
#Done in O(n) time

def missingNumber(list1,N):
	sum = 0
	for i in range(1,N+1):
		sum+=i
	for i in range(0,len(list1)):
		sum-=list1[i]
	missingElement = sum
	return missingElement


tester = [1,2,3,4,6,7,8,9]
n = 9
print("The element is dound by finding sum from one to N then subtracting the elements in our array")
print("From the given input the missing number is " + str(missingNumber(tester,n)))


