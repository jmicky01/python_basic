# 1. Write a program to show usage of class and object.
# 2. Write a program to show usage of inheritance.
# 4. Write a program to show usage of constructor.
#7. Write a python script which has class having two below methods and access
# those methods in another class:
class Employee:
    """ We have a Employee class which have two methods 'full_name', apply_rise"""

    raise_amount = 1.04 # General Employee has rise_ammount = 1.04
    def __init__(self, first, last, salary):
        """ It is a Employee class constructor and each and every when create instance of Employee
        it accepts mimum three arguments
        """
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first +'.' + last +"@gmail.com"

    def full_name(self):
        """
        This method prints full name of employee

        """
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self, dob):
        """
        This method gives if any employee has increment.

        """
        self.pay = int(self.salary * self.raise_amount)

    def get_string(self):
        print " Enter a valid string here: "
        a = raw_input()
        return a

    def print_string_upper_case(self):

        print 'Changed input to upper {}'.format(self.get_string().upper())


class Developer(Employee):

    """
    This class it inherited from Employye calls but we pass one more argument programing_lanuage
    """
    raise_amount = 1.10 # Developer has raise _amount = 1.10

    def __init__(self, first, last, salary, pro_lang):
        Employee.__init__(self, first, last, salary)
        self.program_lang = pro_lang

class Manager(Employee):
    """
    This is a Manager class it will inherited by Employee calss and it has some powefull
    methods to add developers and remove developers from his list.
    """

    def __init__(self, first, last, salary, employees=None):
        Employee.__init__(self, first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """ This method will add developers to list if input developer not already in the list"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """ If developer completed his project, this method will use to remove pariculer deatls
        from the list
        """
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """ This method will print all present employees in the list."""
        for emp in self.employees:
            print ('--->', emp.full_name())




#
dev_1 = Developer('kim', 'roy', 60000, 'python')

dev_2 = Developer('jaipal', 'kondreddy', 60002, 'java')
dev_3 = Developer('Gill', 'toti', 60002, 'java')
magr_1 = Manager('smith', 'tom', 90000, [dev_1])
magr_2 = Manager('Konch', 'aby', 90000, [dev_2])



# print dev_1.program_lang
# dev_1.get_string() # Accessing base class method in subclass instance Developer
# dev_1.print_string_upper_case() # Accessing base class method in subclass instance Develope
# print dev_2.program_lang
# print dev_3.program_lang




print magr_1.email
magr_1.get_string()# Accessing base class method in subclass instance Developer
magr_1.print_string_upper_case()# Accessing base class method in subclass instance Developer

magr_2.get_string()# Accessing base class method in subclass instance Developer
magr_2.print_string_upper_case()# Accessing base class method in subclass instance Developer

magr_1.add_emp(dev_3)
magr_1.print_emps()
magr_2.print_emps()

# 5.Write a program to find greatest element from list.
# 9.Write a program to sort the following intergers in list

list_1 = [1, 4, 5, 7, 9, 6, 10, 12, 16, 18, 11]
print list_1
a = list_1.sort() # sort the list_1 using sort method

print 'sorted list {}'.format(list_1)  # Now print list_1
print 'Gratest number in list is {}'.format(list_1[-1]) # Now print last index for greatest number.



# 6. Write a program to find all numbers divisible by 5 between (2000 and 3000)
# and insert those elements in a list and then print them.


print [i for i in range(2000, 3000) if i%5 == 0]


# 8. What will be the output of following code :
#word = 'abcdefghij'
#print word[:3] + word[3:]

word = 'abcdefghij'

print word[:3] + word[3:]

