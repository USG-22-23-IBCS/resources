import math

def problem1(x, y, z):

    mean = (x + y + z)/3

    L = [x, y, z]
    L.sort()
    median = L[1]

    return mean, median

def main():
    
    print(problem1(5, 10, 42))
    mean, median = problem1(44, 123, -5)
    print(mean)
    print(median)

    x = 4
    y = 3
    h = math.sqrt(x*x + y*y)

    angle = math.asin(y/h)
    print(angle)



if __name__ == "__main__":
    main()
