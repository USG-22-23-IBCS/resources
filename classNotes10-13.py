def main():

    l = []
    l.append("Lemons")
    l.append("Up")
    l.append("bacon")
    l.append(5)
    l.append("Teddybear")
    '''print(l)
    print(l[0])
    print(l[2])
    print(l[-1])'''

    for elem in l:
        print(elem)

    for i in range(5):
        print(l[i])

    stop = 0
    while (stop < 30):
        
        print(l)
        stop = stop + 1
        


if __name__ == "__main__":
    main()
