
class Coffeeshop:

    def __init__(self):
        self.coffee = 3.5
        self.espresso = 4
        self.staleScone = 6
        self.menu = "1. coffee 2. espresso..."

    def getMenu(self):
        return self.menu

    def getOption(self, optionNum):
        return False

    def getPrice(self, choice):
        if choice == "coffee":
            return self.coffee
        
        

def main():

    C = Coffeeshop()
    #name = input("Hello, what is your name?\n")

    #print("Hi " + name)

    num = int(input("Give me a number between 1 and 10\n"))
    
    print("Here is the number multiplied by 3: " + str(num * 3))

    print(C.getMenu())

    
if __name__ == "__main__":
    main()
