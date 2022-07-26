def testPrime(n):
    prime = True
    for j in range(2,n):
        if n%j == 0:
            return(False)
    return(True)

runCode = True
found = [2]
i=3
n = 1
while runCode:
   if testPrime(i):
       found.append(i)
       n+=1
   i+=2
   if n>=10001:
       runCode=False
print(found[-1])
