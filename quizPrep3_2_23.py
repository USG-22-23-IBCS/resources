from graphics import*

#Create a GUI that displays a circle inscribed in a square of at least 100
# pixels wide
def problem1():
    win = GraphWin("Inscribed Circle", 500, 400)
    S = Rectangle(Point(100, 100), Point(300, 300))
    S.draw(win)
    radius = 100
    center = Point(200, 200)
    C = Circle(center, radius)
    C.draw(win)

#Create a GUI which gets two user inputs as integers and displays
# in text if they are the same number
def problem2():
    win2 = GraphWin("Same number check", 600, 400)
    T = Text(Point(300, 100), "HELLO CLASS")
    T.draw(win2)
    e1 = Entry(Point(200, 300), 20)
    e1.draw(win2)
    e2 = Entry(Point(400, 300), 20)
    e2.draw(win2)
    while True:

        num1 = e1.getText()
        num2 = e2.getText()
        if num1 == num2:
            T.setText("They are the same number!")
        else:
            T.setText("Not the same!")

#Create a GUI which gets one user input as an integer and
#draws a circle of that radius
def problem3():
    win3 = GraphWin("Same number check", 600, 400)
    
    e1 = Entry(Point(200, 300), 20)
    e1.draw(win3)

    while True:
        num1 = e1.getText()
        if num1 == "":
            num1 = 0
        C = Circle(Point(300,200), int(num1))
        C.draw(win3)

#Create a GUI which draws a table with 3 columns and 5 rows
def problem4():

#Create a GUI which gets a string as user input and gets a character
#as user input, and checks to see if the string contains that character
#It prints the result in a Text object
def problem5():


def main():
    problem3()


if __name__ == "__main__":
    main()
