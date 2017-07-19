# 1. Write a Python script to check if a given key already exists in a dictionary.

dict_1 = {'key1':1, 'key2': 2, 'key3':3, 'key4': 4,'key5':5, 'key6': 6}

given_key = 'key1'
if given_key in dict_1:
    print '{}, the given key is present in dictionary'.format(given_key)
else:
    print '{}, the given key is not present in dictionary'.format(given_key)




# 2. Write a Python program to iterate over dictionaries using for loops.
dict_2 = {'key1':1, 'key2': 2, 'key3':3, 'key4': 4,'key5':5, 'key6': 6}
for key, value in dict_2.items():
    print key, value

# 3. Write a Python script to merge two Python dictionaries.
dict_3 = {'key1':1, 'key2': 2, 'key3':3, 'key4': 4,'key5':5, 'key6': 6}
dict_4 = {'key7':7, 'key8': 8}

dict_3.update(dict_4)
dict_5 = dict_3.copy()
print dict_5


# 4.Write a Python program to multiplies all the items in a list.

list_1 = [1, 2, 5, 6, 7, 8]

list_multiplication_with2 = [i*2 for i in list_1]
print list_multiplication_with2


# 5. Write a Python program to remove duplicates from a list.

list_1 = [1, 2, 5, 6, 7, 8, 8, 1, 4, 5]
print list_1
with_out_duplicates1 = list(set(list_1))
print with_out_duplicates1


# 6. Write a Python class to implement pow(x, n).
class PowerOfTwoNum():
    """ This will print pow(x, n) output"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

        count = 1
        for i in range(self.y):
            count *= self.x

        print count


z = PowerOfTwoNum(10, 2)


# 7. Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle.
import math
class Circle():
    """ It gives Area, perimeter of circle"""

    def __init__(self, radius):

        self.radies = radius

    def area(self):
        area = math.pi * self.radies*self.radies
        print 'Area of circle is : {}'.format(area)

    def perimeter(self):
        perimeter = 2 * math.pi * self.radies
        print 'perimeter of circle is : {}'.format(perimeter)




# c is a instance of class
x = Circle(6)
x.area()
x.perimeter()


# 8 Write a Python program that accepts a word from the user and reverse it

print 'enter the value in : \t'
a = raw_input()
print a[::-1]


