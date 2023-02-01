def csClass():
    print("I enjoy coding")
    print("not sarcastic...")

def bioClass(name):
    happy = True
    study = False
    return name + str(study)

def main():

    #data types and their uses


    #String
    name = "Yuliia"
    name2 = "Jenny"
    name3 = "Anna is in computer science class"
    # characters can be accessed through the index
    print(name[0])
    print(name2[3])
    print(name[-1])
    # substrings can be accessed through the index
    print(name2[0:3])
    print(name3[1:])
    # reverse a string
    print(name3[::-1])
    # strings can be added together through 'concatenation'
    print(name + name2)
    print(name, name2)
    print(name2*10)
    #String data types cannot be added with integer data types
    #Sometimes it is necessary to convert the integer into a string
    x = 100
    print(name3 + " " + str(x))

    #Integers are number data types
    y = 40
    z = 30.5
    print(z)
    z = int(z)
    print(z)

    #rounding . Floats always printed with .0 to show a float
    w = 20.65678
    print(round(w, 2))
    print(round(w, 0))
    #rounding a float up and converting to an integer
    print(int(round(w,0)))

    #integer division
    g = 12
    print(g/5)
    print(g/4)
    # sometimes referred to as 'div'
    print(g//4)
    print(g//5)
    # modulo operator
    print(g % 5)

    #Lists can have different types of data within the collection
    L = ["Leah", "Mr. Considine", 10, 2.5, True]
    print(L[0])
    print(L[4])
    # sublists can be accessed by positions [start : stop]
    subL = L[1:3]
    for element in subL:
        print(element)
    #Lists can be added to other lists
    L2 = L + ["Anna", "Mr. Phillips", False]
    print(L2)

    #nested loop
    names = ["John", "Jerry", "Liam", "Wilson"]
    for n in names:
        for char in n:
            print(char)

    csClass()

    csClass()
    csClass()

    S = bioClass("Jenny")
    print(S)
    
    

    
    

    

if __name__ == "__main__":
    main()
