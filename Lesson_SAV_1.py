list = [1, 5, 0, -5, 2.5]
for n in list:
    print(n)
    print("---------------------------------")
    str = "Python"
    print(str[0])
    for s in str:
        print(s)
        for s in str:
            if s == "Y" :
                break
            else :
                print("Символа Y в строке, нет")



