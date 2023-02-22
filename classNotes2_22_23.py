def main():

    #String formatting
    #Use {} as placeholders for any other variable

    '''name = input("Type your name\n")
    greeting = "Hello, {}! How are you liking Computer Science?"
    print(greeting.format(name))

    ia = "CS"
    score = 1
    phrase = "Here in IB AI SL 2, I completed the {1} IA, and scored {0}"
    print(phrase.format(score, ia))

    price = 4.5
    order = "One Matcha Green Tea Lemonade (way too lemony btw). That will be ${:1f}"
    print(order.format(round(price*1.0675, 2)))'''

    #File reading

    file = open("sample2.txt")
    contents = file.read()
    myList = contents.split()
    for word in myList:
        if "n" in word:
            print(word)






    

if __name__ == "__main__":
    main()
