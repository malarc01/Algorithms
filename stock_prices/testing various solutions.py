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
# min - max
l = [10, 7, min, 8, max, 9]

l = [10, 7, 5, 8, 11, 9]
# max min
([max, 90, 80, 50, 20, min]), -10
100-10
([100, 90, 80, 50, 20, 10]), -10
([100, 90, 80, 50, 20, 10]), -10
#find smallest
100>90
90= smallest
90>80
# from index search for max
# if no max set max to 0 


[1050, 270, 1540, 3800, 2]
[1050, 270, 1540, max, min]
[1050, min, 1540, max, 2]
# if min is at the end of list 
# search for another min exclude it from search 
# from index search for max
# if no max set max to 0 
3530
# find min value first

if value > value2
elif expression:
    pass
# 100>55
# min = value2
# min = 55

#if so set value2 to min_price
# continue
# 55 = min_price 
# is 55<4 
# continue
# is 55< 
[100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79], 94
[max, 55, min, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79], 94
[100, 55, min, max, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79], 94





for x, y in zip(l[::], l[1::]):
    print("line31", x, y)
    smallest = x
    if x > y:
        smallest = x
        print(smallest)
        # print(f"{x} is greater than{y}")
        # print('SMALLEST IS =>', smallest)
    else:
        # print(f"{x} is not greater than {y}")
        print('else')

    # You can add the comparision code here


another_list = [100, 90, 80, 50, 20, 10]