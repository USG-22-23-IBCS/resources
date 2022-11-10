from graphics import*
from Button import*


def main():

    # graphics windows are defined with (name, width, height)
    win = GraphWin("character creator", 800, 600)
    win.setBackground("light steel blue")

    '''C = Circle(Point(400, 100), 40)
    C.draw(win)
    C.setFill("maroon4")

    R = Rectangle(Point(550, 400), Point(650, 450))
    R.draw(win)
    R.setOutline("lemon chiffon")

    P = Polygon([Point(200, 0), Point(250, 100), Point(150, 120)])
    P.draw(win)

    T = Text(Point(300, 200), "Hello IBCS!")
    T.draw(win)
    T.setSize(25)
    T.setTextColor("red")'''
    F = Oval(Point(200, 100), Point(500, 500))

    BigEye1 = Circle(Point(300, 200), 50)
    BigEye2 = Circle(Point(400, 200), 50)

    SmallEye1 = Circle(Point(300, 200), 20)
    SmallEye2 = Circle(Point(400, 200), 20)

    smallEyes = Button(win, Point(600, 100), Point(700, 175), "tomato", "Small Eyes")
    Eyes = Button(win, Point(600, 200), Point(700, 275), "tomato", "Big Eyes")
    Face = Button(win, Point(600, 300), Point(700, 375), "tomato", "Face")
    Q = QuitButton(win, Point(600, 450), Point(700, 525))

    while True:
        m = win.getMouse()
        if Face.isClicked(m):
            F.undraw()
            F.draw(win)

        if Eyes.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            SmallEye1.undraw()
            SmallEye2.undraw()

            BigEye1.draw(win)
            BigEye2.draw(win)

        if smallEyes.isClicked(m):
            SmallEye1.undraw()
            SmallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()

            SmallEye1.draw(win)
            SmallEye2.draw(win)

        if Q.isClicked(m):
            break

    win.close()






    


if __name__ == "__main__":
    main()
