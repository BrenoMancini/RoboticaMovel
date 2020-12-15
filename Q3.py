def __checkPerfectNumber(Number):
    SumDivisors = 0
    for i in range(1, Number):
        if(Number % i == 0):
            SumDivisors = SumDivisors + i

    if (SumDivisors == Number):
        return True
    else:
        return False

def __main__():
    print("form 1 to 10000")
    for i in range(1, 10000):
        if(__checkPerfectNumber(i)):
             print(" %d is a Perfect Number" %i)
    
        
__main__()