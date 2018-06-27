def trappedWater(brickHeight):
	maxLeftHeight = []
	maxRightHeight = []
	reversedList = brickHeight[::-1]

	maxLeftHeight.append(-1)
	maxLeftHeight.append(brickHeight[0])
	maxRightHeight.append(-1)
	maxRightHeight.append(reversedList[0])

	for i in range(2,len(brickHeight)):
		
		maxBrickHeight = max(brickHeight[i-1],maxLeftHeight[i-1])
		maxLeftHeight.append(maxBrickHeight)

	for i in range(2,len(brickHeight)):
		
		maxRightBrickHeight = max(reversedList[i-1],maxRightHeight[i-1])
		maxRightHeight.append(maxRightBrickHeight)

	trappedWater = 0
	trueRightHeight = maxRightHeight[::-1]
	for k in range(1,len(brickHeight)-1):
		trappedWater += min(maxLeftHeight[k],trueRightHeight[k]) - brickHeight[k]
	return trappedWater

tester = [3,0,0,2,0,4]
print("The maximum amount of water that can be trapped will be " + str(trappedWater(tester)) + " gallons of water")

