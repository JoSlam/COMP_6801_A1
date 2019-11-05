##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1


import math
import random

#part 1
def fermat_primality(a, p):
    result = False
    powerResult = 0

    if(a > 1 and a < (p-1) and p > 1):
        powerResult = math.pow(a, p-1)
        result = (powerResult % p) == 1
    return result

#part 2
def square_root_primality(a, p):
    i = 2
    while (i < p-1):
        if (math.pow(i, 2) % p == 1):
            return False
        i += 1
    return True

#part 3
def miller_rabin(a, p):
    if(a < 1):
        print("Please supply an iteration value greater than 0")
        return False

    if(p < 2):
        return False
    if(p != 2 and p % 2 == 0):
        return False
    
    d = p-1
    s = 0

    while (d % 2 == 0):
        d = d // 2
        s += 1

    for i in range(0, a):
        k = random.randint(2, p-1)
        mod = pow(k, d, p)

        if(mod == 1 or mod == p-1):
            return True

        for j in range(1, s):
            mod = pow(mod, 2, p)

            if(mod == 1):
                return False

            if(mod == p-1):
                return True
    return False    
        

#part 4
def gcd(a,p):
    temp = 0

    while p != 0:
        temp  = a
        a = p
        p = temp % p

    return a
    
    
#part 5
def inverse(a, p):
    if(a >= 1 and p >= 2):
        return (int)(math.pow(a, p-2)) % p
    print("No inverse exists.")
    return -1

# print(fermat_primality(2, 15))
# print(fermat_primality(4, 15))

# print(square_root_primality(2, 15))
# print(square_root_primality(4, 15))
# print(square_root_primality(4, 11))

# print(inverse(8, 11))

# print(miller_rabin(1, 61))
