class House:

    def __init__(self):
        self.rating = 5

    def getRating(self):
        return self.rating

def calculatePath(num):
    path = []
    

def main():
    
    '''l = []
    a = ["apples", "oranges", "mangoes"]
    b = ["ice cream", "flan", "brookies"]
    c = ["lettuce", "zucchini", "broccoli"]
    l.append(a)
    l.append(b)
    l.append(c)

    print(l)
    #fruits
    print(l[0])
    #mangoes
    print(l[0][2])'''

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(House())

    print(m)

    num = int(input("how many houses"))

    calculatePath(num)

            
        

if __name__ == "__main__":
    main()
