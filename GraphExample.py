from graphics import*
import random

class Node:
    def __init__(self, x, y, win):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        #self.neighbors = []

    def draw(self, win):
        self.C.draw(win)


class Graph:

    def __init__(self, n, win):
        self.nodes = []
        for i in range(n):
            x = random.randint(200, 600)
            y = random.randint(100, 500)
            N = Node(x, y, win)
            self.nodes.append(N)
        for node in self.nodes:
            node.draw(win)
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    G = Graph(5, win)

if __name__ == "__main__":
    main()
