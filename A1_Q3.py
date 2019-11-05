##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import math

def trial_division(n):
    factorList = []
    
    while (n % 2 == 0) : 
        factorList.append(2)  
        n = n // 2
  
    for i in range(3, int(math.sqrt(n)), 2): 
        while (n % i == 0) : 
            factorList.append(i)  
            n = n // i  
          
    if (n > 2) : 
        factorList.append(n)
    return factorList


def checkPrime(n):  
  
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True

    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5

    while(i**2 <= n): 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 1
  
    return True   


def findPrimitiveRoot(n) : 
    numSet = []

    if(not checkPrime(n)):
        return -1

    phiN = n - 1
    numSet.extend(trial_division(phiN))

    for j in range(2, phiN + 1):
        result = False

        for num in numSet:
            if(pow(j, phiN // num, n) == 1):
                result = True
                break
        
        if(not result):
            return j
    
    return -1


# print(findPrimitiveRoot(7))
# print(findPrimitiveRoot(21))
# print(findPrimitiveRoot(761))

