l = [10, 7, 5, 8, 11, 9]
for x, y in zip(l[::], l[1::]):
    print("line31", x, y)
    largest = None
    smallest = None
    if x > y:
        largest= x
        print('GRANDE',largest)
        # print(f"{x} is greater than{y}")
        # print('SMALLEST IS =>', smallest)
    elif y>x:
        # print(f"{x} is not greater than {y}")
        # print('else')
        smallest = y
        print('SMALL',smallest)
    print('OUTPUT',largest,smallest) 
    # You can add the comparision code here


another_list = [100, 90, 80, 50, 20, 10]