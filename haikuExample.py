import random

def genLine(syl, val):
    line = ""
    while True:
        v = random.randint(1,4)
        if val - v >= 0:
            myList = syl.get(v).split()
            line = line + random.choice(myList) + " "
            val = val - v
        if val == 0:
            break
    
    return line

def main():
    f1 = open("oneSyllable.txt")
    f2 = open("twoSyllable.txt")
    f3 = open("threeSyllable.txt")
    f4 = open("fourSyllable.txt")
    readOne = f1.read()
    readTwo = f2.read()
    readThree = f3.read()
    readFour = f4.read()
    syl = {1 : readOne,
           2 : readTwo,
           3 : readThree,
           4 : readFour}

    print(genLine(syl, 5))
    print(genLine(syl, 7))
    print(genLine(syl, 5))

if __name__ == "__main__":
    main()
