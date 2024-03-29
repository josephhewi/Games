
'''
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

array = [[08.0, 02.0, 22.0, 97.0, 38.0, 15.0, 00.0, 40.0, 00.0, 75.0, 04.0, 05.0, 07.0, 78.0, 52.0, 12.0, 50.0, 77.0, 91.0, 08.0], 
		 [49.0, 49.0, 99.0, 40.0, 17.0, 81.0, 18.0, 57.0, 60.0, 87.0, 17.0, 40.0, 98.0, 43.0, 69.0, 48.0, 04.0, 56.0, 62.0, 00.0], 
		 [81.0, 49.0, 31.0, 73.0, 55.0, 79.0, 14.0, 29.0, 93.0, 71.0, 40.0, 67.0, 53.0, 88.0, 30.0, 03.0, 49.0, 13.0, 36.0, 65.0], 
		 [52.0, 70.0, 95.0, 23.0, 04.0, 60.0, 11.0, 42.0, 69.0, 24.0, 68.0, 56.0, 01.0, 32.0, 56.0, 71.0, 37.0, 02.0, 36.0, 91.0], 
		 [22.0, 31.0, 16.0, 71.0, 51.0, 67.0, 63.0, 89.0, 41.0, 92.0, 36.0, 54.0, 22.0, 40.0, 40.0, 28.0, 66.0, 33.0, 13.0, 80.0], 
		 [24.0, 47.0, 32.0, 60.0, 99.0, 03.0, 45.0, 02.0, 44.0, 75.0, 33.0, 53.0, 78.0, 36.0, 84.0, 20.0, 35.0, 17.0, 12.0, 50.0], 
		 [32.0, 98.0, 81.0, 28.0, 64.0, 23.0, 67.0, 10.0, 26.0, 38.0, 40.0, 67.0, 59.0, 54.0, 70.0, 66.0, 18.0, 38.0, 64.0, 70.0], 
		 [67.0, 26.0, 20.0, 68.0, 02.0, 62.0, 12.0, 20.0, 95.0, 63.0, 94.0, 39.0, 63.0, 08.0, 40.0, 91.0, 66.0, 49.0, 94.0, 21.0], 
		 [24.0, 55.0, 58.0, 05.0, 66.0, 73.0, 99.0, 26.0, 97.0, 17.0, 78.0, 78.0, 96.0, 83.0, 14.0, 88.0, 34.0, 89.0, 63.0, 72.0], 
		 [21.0, 36.0, 23.0, 09.0, 75.0, 00.0, 76.0, 44.0, 20.0, 45.0, 35.0, 14.0, 00.0, 61.0, 33.0, 97.0, 34.0, 31.0, 33.0, 95.0], 
		 [78.0, 17.0, 53.0, 28.0, 22.0, 75.0, 31.0, 67.0, 15.0, 94.0, 03.0, 80.0, 04.0, 62.0, 16.0, 14.0, 09.0, 53.0, 56.0, 92.0], 
		 [16.0, 39.0, 05.0, 42.0, 96.0, 35.0, 31.0, 47.0, 55.0, 58.0, 88.0, 24.0, 00.0, 17.0, 54.0, 24.0, 36.0, 29.0, 85.0, 57.0], 
		 [86.0, 56.0, 00.0, 48.0, 35.0, 71.0, 89.0, 07.0, 05.0, 44.0, 44.0, 37.0, 44.0, 60.0, 21.0, 58.0, 51.0, 54.0, 17.0, 58.0], 
		 [19.0, 80.0, 81.0, 68.0, 05.0, 94.0, 47.0, 69.0, 28.0, 73.0, 92.0, 13.0, 86.0, 52.0, 17.0, 77.0, 04.0, 89.0, 55.0, 40.0], 
		 [04.0, 52.0, 08.0, 83.0, 97.0, 35.0, 99.0, 16.0, 07.0, 97.0, 57.0, 32.0, 16.0, 26.0, 26.0, 79.0, 33.0, 27.0, 98.0, 66.0], 
		 [88.0, 36.0, 68.0, 87.0, 57.0, 62.0, 20.0, 72.0, 03.0, 46.0, 33.0, 67.0, 46.0, 55.0, 12.0, 32.0, 63.0, 93.0, 53.0, 69.0], 
		 [04.0, 42.0, 16.0, 73.0, 38.0, 25.0, 39.0, 11.0, 24.0, 94.0, 72.0, 18.0, 08.0, 46.0, 29.0, 32.0, 40.0, 62.0, 76.0, 36.0], 
		 [20.0, 69.0, 36.0, 41.0, 72.0, 30.0, 23.0, 88.0, 34.0, 62.0, 99.0, 69.0, 82.0, 67.0, 59.0, 85.0, 74.0, 04.0, 36.0, 16.0], 
		 [20.0, 73.0, 35.0, 29.0, 78.0, 31.0, 90.0, 01.0, 74.0, 31.0, 49.0, 71.0, 48.0, 86.0, 81.0, 16.0, 23.0, 57.0, 05.0, 54.0], 
		 [01.0, 70.0, 54.0, 71.0, 83.0, 51.0, 54.0, 69.0, 16.0, 92.0, 33.0, 48.0, 61.0, 43.0, 52.0, 01.0, 89.0, 19.0, 67.0, 48.0]]


def listProd(array):
    if 0 in array:
        return(0)
    else:
        product = 1
        for number in array:
            product*=number
        return(product)

def searchY(sqrMat,length):
    high = 0
    highArray = []
    for i in range(0,len(sqrMat)):
      for j in range(0,len(sqrMat)-length+1):
         testLine = [row[i] for row in sqrMat[j:j+length]]
         testValue = listProd(testLine)
         if testValue > high:
             high = testValue
             highArray = testLine
    return(high,highArray)

def searchX(sqrMat,length):
    high = 0
    highArray = []
    for i in range(0,len(sqrMat)-length+1):
      for j in range(0,len(sqrMat)):
         testLine = sqrMat[j][i:i+length]
         testValue = listProd(testLine)
         if testValue > high:
             high = testValue
             highArray = testLine
    return(high,highArray)

def searchDiag(mat,length):
    high = 0
    highArray = []
    testLine1 = [i for i in range(0,length)]
    testLine2 = [i for i in range(0,length)]
    
    for i in range(0,len(mat)-length+1):
        
        for j in range(length-1,len(mat[0])-length+1):
            
            
            for k in range(length):
                testLine1[k] = mat[i+k][j+k]
                testValue1 = listProd(testLine1)
            if testValue1 > high:
                high = testValue1
                highArray = testLine1[:]
                    
                
            for k in range(length):
                testLine2[k] = mat[i+k][j-k]
                testValue2 = listProd(testLine2)
            if testValue2 > high:
                high = testValue2
                highArray = testLine2[:]
            
            
    return(high,highArray)

'''
import numpy as np
array = np.random.rand(10,10)*100
array = array.astype(np.int32)
'''
print(searchX(array,4))
print(searchY(array,4))
print(searchDiag(array,4))

    
