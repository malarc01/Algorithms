# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print('LINE 11 =>', list(enumerate(l1)))

# changing start index to 2 from 0
print('LINE 14 =>', list(enumerate(s1, 2)))


# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print('line23', ele)
print
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)


colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])

for tint in colors:
    print(tint)

for tint in range(3, len(colors)+1):
    print(tint)

for tint in range(len(colors)):
    print(tint)

for number, color in enumerate(colors, start=1):
    print("Color {} : {}".format(number, color))
stock_list = [10, 7, 5, 8, 11, 9]


for number, price in enumerate(stock_list,):
    # init = stock_list[0]
    # print("$ {} : {}".format(number, price))
    print(stock_list[1:len(stock_list)])
    if price > stock_list[1:len(stock_list)]:
        print(f"{price} is greater than {stock_list[number]}")
        # price, init = init = price
    else:
        print(f"{price} is NOT greater than {stock_list[number]}")


for number, color in enumerate(colors, start=1):
    print("Color {} : {}".format(number, color))

