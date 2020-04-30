# Basic operators

print("2+2 = " + str(2 + 2))
print("5-2 = " + str(5 - 2))
print("3*5 = " + str(3 * 5))
print("5/4 = " + str(5 / 4))
print("5.0/4.0 = " + str(5.0 / 4.0))
print("9%2 = " + str(9 % 2))
print("5**2 = " + str(5 ** 2))
print("3>5 = " + str(3 > 5))
print("5<10 = " + str(5 < 10))
print("10==10 = " + str(10 == 10))
# Data types, variables and expressions
print("type(1) = " + str(type(1)))
print("type(1.0) = " + str(type(1.0)))
print("type(\"Hello\") = " + str(type("Hello")))
print("type(3==5) = " + str(type(3 == 5)))
pi = 3.15159
# radius = float(raw_input("Radius = "))
radius = 15
area = pi * radius ** 2
print("area = " + str(area))


# Functions
def sum_numbers(number1: int, number2: int) -> int:
    return number1 + number2


print("sum(1,2) = " + str(sum_numbers(1, 2)))

# Strings
print("hello.upper() = " + "hello".upper())
print("hello.find('o') = " + str("hello".find("o")))
print("hello[2:] = " + "hello"[2:])
print("hello[0:4:2] = " + "hello"[0:4:2])
print("hello[::-1] = " + "hello"[::-1])

# Ranges, For, While
print("range(3) = " + str(list(range(3))))
print("range(3, 40) = " + str(list(range(3, 40))))
print("range(1, 100, 5) = " + str(list(range(0, 100, 5))))

for i in range(1, 20, 5):
    print(str(i))

limit = 20
i = 0
while i <= 100:
    if i == limit:
        print("Limit {} found".format(limit))
    i = i + 1

# List
friends = list()
friends.append("Juan")
print(friends)
friends.append("Marcos")
print(friends)
print("friends[0] = " + friends[0])

numbers = [3, 4, 5]
print(numbers)
print("list1 + list2 = " + str(friends + numbers))
pairs = [num for num in range(1, 31) if num % 2 == 0]
print("pairs = [num for num in range(1,31) if num % 2 == 0] = " + str(pairs))
print(str("[1] * 4 = {}".format([1] * 4)))

# Dictionaries
dictionary = {'first_element': 'Hello', 'second_element': 'Friends'}
print('dictionary = ' + str(dictionary))
for key in dictionary:
    print("key = {}".format(key))

for key in dictionary.keys():
    print(key)

for key, value in dictionary.items():
    print('Key: {}, Value: {}'.format(key, value))
squares = {num: num ** 2 for num in range(1, 10)}
print("squares = {num: num ** 2 for num in range(1, 10)} = " + str(squares))

# Tuples
my_tuple = (1, 2, 3, 4)
print("my_tuple(1,2,3,4) = " + str(my_tuple))
print("my_tuple[0] = " + str(my_tuple[0]))

# Sets
s = {1, 2, 3}
t = {3, 4, 5}
print("s = {1, 2, 3}")
print("t = {3, 4, 5}")
print('s.union(t) = ' + str(s.union(t)))
print('s.intersection(t) = ' + str(s.intersection(t)))
print('s.difference(t) = ' + str(s.difference(t)))
