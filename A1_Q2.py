##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import math

def trial_division(n):
    factorList = []
    factorList.append(1)
    
    while(n % 2 == 0): 
        n = n // 2
        
    for i in range(3,int(math.sqrt(n))+1,2): 
        while(n % i == 0): 
            factorList.append(i)
            n = n // i 
              
    if(n > 2): 
        factorList.append(n)
    return factorList

 
def fermat_method(n):
    factorList = []
    factorList.append(1)

    a = math.ceil(math.sqrt(n))
    bsqr = a**2 - n

    result = math.sqrt(bsqr)
    while(not result.is_integer()):
        a += 1
        bsqr = a**2 - n
        result = math.sqrt(bsqr)

    factorList.append(subtractIntegers(a, result))
    factorList.append(addIntegers(a, result))


    return factorList


def addIntegers(x, y):
    return int(x + y)

def subtractIntegers(x, y):
    return int(x - y)

def main():
    inp = input("Enter a number in the range 2-1000: ")

    try:
        val = int(inp)
    except:
        print("Input is not a number.")
        return -1

    if(val < 2 or val > 1000):
        print("Input exceeds given range")
        return -1

    print("Trial division: ", trial_division(val))
    print("Fermat's method: ", fermat_method(val))

main()