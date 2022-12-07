def main():

    L = [34, 20, 12, 24, 62, 13, 66, 42, 103, 800, 25, 50, 555, 320, 12, 18, 62]

    print(L)
    print("commence bubbling")
    steps = 0
    for i in range(len(L) - 1):
        for j in range(len(L) - 1 - i):

            if L[j] > L[j+1]:
                #swap
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            steps = steps + 1

    print("done")
    print(L)

    print(len(L))
    print(steps)

if __name__ == "__main__":
    main()
