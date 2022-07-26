'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

data = []
with open('large Sums.txt','r') as numbers:
    for line in numbers:
        data.append(line.strip())

#data = data[:10]
        
newArray = []    
for x in range(1,len(data[0])+5):
    y = int(x)
    tempSum = 0
    for number in data:
        try:
            tempSum+=int(number[-1*y])
        except:
            
            pass
    print(str(tempSum)[-1])
    tempSum *= 10**x
    data.append(str(tempSum))

print(data[-1])
    