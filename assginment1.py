

# 1. Write a program to check if a number is even or odd.

def even_or_odd(list):
    for i in list:
        if i % 2 == 0:
            print 'Given number is {} is an even number'.format(i)
        else:
            print 'Given number is {} is an odd number'.format(i)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_or_odd(number)

#2. Write a program to find greater number between three number.
def grater_number_bw_3(x, y, z):
    if x > y :
        if x > z:
            print '{} is a max number in given three numbers--> {}, {}, {}'.format(x, x, y, z)
        else:
            print '{} is a max number in given three numbers--> {}, {}, {}'.format(z, x, y, z)
    else:
        print '{} is a max number in given three numbers--> {}, {}, {}'.format(y, x, y, z)

grater_number_bw_3(55,333,12)

#3. Write a program to find prime number
def prime_number(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print "{} is not a prime number".format(x)
                break
        else:
            print "{} is a prime number".format(x)
    else:
        print "{} is a prime number".format(x)


prime_number(27)


#4. Write a program to find the factorial of a number.
def factorial(x):
    count = 1
    for i in range(1, x+1):
        count *= i
    return count


print factorial(6)

#Write a program to swap(exchange value of two variables) without using third variable

def swap(x, y):
    print 'Before swap:{},{}'.format(x, y)
    x = x + y
    y = x - y
    x = x - y
    print 'After swap:{},{}'.format(x, y)


swap(4,2)

#6. Write a program to check if a number is positive,negative or zero.

def check_positive_nagative_zero(number):
    if number >= 0:
        if number == 0:
            print 'Given number is zero'
        else:
            print '{} is a positive number'.format(number)
    else:
        print '{} is a negative number'.format(number)

check_positive_nagative_zero(-1)


#7. Write a program to check leap year
def leap_year(year):
    if year%4 == 0:
        print '{} is a leap year'.format(year)
    else:
        print '{} is not a leap year'.format(year)

leap_year(2000)

#8. Write a program to insert elements in list. (Take empty list, and use for loop to add
# elements into list and elements should be taken from user at runtime using raw_input
# function)

def insert_list():
    print 'enter the value, it will iterate each character in given input  '
    a = raw_input()
    list = []
    for i in a:
        list.append(i)
    print list

insert_list()
#9. Write a program to calculate GCD of two numbers
import fractions
print fractions.gcd(12,5) # we built-in function to find gcd


# 10 Write a program to count the occurence of given character in list.
list = [1, 2, 1, 4, 5, 1, 'a', 'a', 'a']

given_charactor = 1
given_charactor1 = 'a'
print list.count(given_charactor)
print list.count(given_charactor1)

# 11. Write a Python program to multiplies all the items in a list.
def multiply(list):
    total = 1
    for i in list:
        total *= i
    print total

multiply([1, 2, 4, 6])

# 12. Write a Python program to remove duplicates from a list.

def remove_dups(list):
    print 'Before removing duplication {}'.format(list)
    for i in list:
        if (list.count(i))>1:
            #list.pop(i) # This will delete only integers
            list.remove(i)
            print '{} might be duplicate'.format(i)
    print 'After removing duplication {}'.format(list)



remove_dups([1, 8, 9, 9])


# 13. Write a Python program to check a list is empty or not
def is_empty(list):
    if list.__len__() == 0:
        print '{} is empty'.format(list)
    else:
        print '{} is not empty'.format(list)

is_empty([9])
# 14. Write a Python script to merge two Python dictionaries.

dict_1 = {'0':1,'1': 2}
dict_2 = {'2':3, '3': 4}


dict_3 =  dict_1.copy()
dict_3.update(dict_2)
print dict_3
# 15. Write a Python program to sum all the items in a dictionary

dict_0 = {'1':9, '2':1}
print sum(dict_0.values())