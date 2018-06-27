#Problem Statement
#Given a 2-d array find the total number of negative numbers present 

def negativeNumbers(matrix):
    count = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] < 0:
                count+=1
            else:
                break
    return count

tester = [[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]
print("There are " + str(negativeNumbers(tester) ) + " negative numbers present ")

