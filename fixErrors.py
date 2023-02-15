# IBCS "Find my error"

# Each method below currently does not run properly. Either it throws an error
# or it prints out/returns the wrong thing. Fix each method one by one.
# Comment out the method call in the main to run it and test it.


#calculate sum, product and mean of three numbers
def calcThree(x, y, z):
    x = x + y + z
    y = x*y*z
    z = (x+y+z)/3
    return x, y, z

#determine the minimum value in a list of numbers
def myMax(L):
    m = 100
    for e in L:
        if e > m:
            m = e

    return m

# The user inputs an integer between 1-15. If the user's number is
# greater than the random number, the method should print "lower". If
# the user was less than the random number, the method should print "higher".
# If the user got it right, the method should print "You got it!" and stop.
# The user gets to guess 3 times before the method stops otherwise.
def threeGuessGame():
    n = random.randint(1,15)
    while (n != num):
        num = input("Please enter a number between 1 and 15.\n")
        if num > n:
            print("lower")
        elif num == n:
            print("You got it!")
            break
        else:
            print("higher")
    

#randomize the characters in a user input name (First and Last)
# and print out the users new name
def randomName():
    name = input("Please enter your first name")
    name2 = input("Please enter your last name")
    for n in name:
        name = name + random.choice(name)
    for n in name2:
        name2 = name2 + random.choice(name2)

    print("Hello" + name + " " name2)


def main():
    #calcThree()
    #myMax()
    #threeGuessGame()
    #randomName()


if __name__ == "__main__":
    main()
