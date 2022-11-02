def main():


    # dictionaries are a data structure, they are a 'set'
    # a group of items, all items are unique and there is no order
    # set of 'key' : 'value' pairs

    vegetables = {"onion" : 1.25,
                  "tomato" : 0.75,
                  "squash" : 2.50,
                  "celery" : 0.50,
                  "cauliflower" : 1.75,
                  "russet potato" : 0.75}

    print(vegetables.get("onion"))
    print(vegetables)
    #print(vegetables.pop("squash"))

    vegetables.update({"scallions" : 3.50})
    vegetables.update({"tomato" : 1.50})
    print(vegetables)

    veggieList = list(vegetables.keys())

    for v in veggieList:
        print(v)

    

if __name__ == "__main__":
    main()
