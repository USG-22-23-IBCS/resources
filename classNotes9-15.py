
class Vehicle:

    #constructor method has all of the instance variables (values / data)
    def __init__(self, brand, x, col):
        self.numWheels = x
        self.brand = brand
        self.color = col

    def getBrand(self):
        return self.brand

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color
        

def main():

    veh1 = Vehicle("Ford", 4, "purple")
    veh2 = Vehicle("BMW", 10, "seafoam-green")
    print(veh1.getBrand())
    print(veh1.getColor())
    veh1.setColor("yellow")
    print(veh1.getColor())
    #print("Hello World")

if __name__ == "__main__":
    main()
