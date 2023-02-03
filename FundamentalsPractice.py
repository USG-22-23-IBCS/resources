import math
import random


def problem5(name):

    name = name.lower()

    score = 0
    for char in name:
        if char in ["a", "e", "i", "o", "u", "l", "n", "s", "t", "r"]:
            score = score + 1
        elif char in ["c", "d", "m", "q", "w", "v", "p"]:
            score = score + 2
        else:
            score = score + 5

    return score 
        

def problem1(x, y, z):

    mean = (x + y + z)/3

    L = [x, y, z]
    L.sort()
    median = L[1]

    return mean, median

def problem2(num):

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return True
    
    return False
        
   

def problem3(nums):

    nMax = nums[0]
    nMin = nums[0]
    
    for n in nums:
        if n > nMax:
            nMax = n
        if n < nMin:
            nMin = n

    rangeVals = nMax - nMin
    return nMax, nMin, rangeVals
            
   

def problem4(P):
    x = P[0]
    y = P[1]

    h = math.sqrt(x*x+y*y)
    angle = math.asin(y/h)

    angle = angle*180 / math.pi
    angle = round(angle, 2)
    
    return [h, angle]
        

def main():
    
    print(problem1(5, 10, 42))
    mean, median = problem1(44, 123, -5)

    print(problem4([2,2]))

    num = random.randint(1, 100)
    print(num)
    print(problem2(num))

    L = []
    for i in range(10):
        L.append(random.randint(1, 50))

    print(problem3(L))

    name = input("Please enter a name to play scrabble with?\n")
    print(problem5(name))

    #L = [random.randint(1, 50) for i in range(10)]
   

if __name__ == "__main__":
    main()
