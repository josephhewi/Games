'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
 that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

known = {0:0,1:1}


def check(x):
    y = x
    n = 1
    while y!=1:
        n+=1
        if y in known:
            n+=known[y]
            break
        else:
            if y%2==0:
                y /= 2
            else:
                y = y*3+1
    known.update({x:n})
    return(n)

highest = [0,0]
for i in range(2,int(1e6)):
    n = check(i)
    if n>highest[1]:
        highest = [i,n]