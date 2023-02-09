import random

# Given a name return the name where each character is repeated once.
# Ex: "Considine" --> "CCoonnssiiddiinnee"

def problem1(name):

    name2 = ""
    for char in name:
        name2 = name2 + char*2

    return name2
    
# Given a list of integers. Randomize their order, then print out
# the first, last and middle integer
def problem2(L):

    L2 = []
    for i in range(len(L)):
        num = random.choice(L)
        L.remove(num)
        L2.append(num)
    print(L2)
    print(L2[0])
    print(L2[-1])
    print(L2[len(L2)//2])
    

def main():

    '''print(problem1("Jenny"))
    print(problem1("Yuliia"))
    print(problem1("Leah"))'''

    problem2([1, 3, 4, 6, 8, 9, 10])
    #this main method is mostly untouched

if __name__ == "__main__":
    main()
