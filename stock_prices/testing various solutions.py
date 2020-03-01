# max


stock_list = [10, 7, 5, 8, 11, 9]


print(max(stock_list))
print(min(stock_list))


print(max(stock_list)-min(stock_list))


# using nested loops
def list_diff(list1, list2):
    output = []
    for element in list1:
        if not element in list2:
            output.append(element)
    return output


# Test Input
list1 = [10, 7, 5, 8, 11, 9]
list2 = [10, 7, 5, 8, 11, 9]


# find smallest value
#l = [max, 7, 5, 8, 11, 9]
# is 10 smaller than 7 if yes => smallest = value
l = [10, 7, 5, 8, 11, 9]

for x, y in zip(l[::], l[1::]):
    print("line31", x, y)
    smallest = x
    if x > y:
        smallest = x
        print(f"{x} is greater than {y}")
        print('SMALLEST IS =>', smallest)
    else:
        print(f"{x} is not greater than {y}")

    # You can add the comparision code here
