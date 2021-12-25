list1 = (1, 2, 3, 4, 5)

def invokeme(func1, func2, list):
    for (index, item) in enumerate(list):
        if (index + 1) % 2 == 0:
            print(func1(item))
        else:
            print(func2(item))

invokeme(lambda num: num + 1, lambda num: num + 10, list1)