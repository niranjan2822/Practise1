'''
def func():
    print("python")


func()


def func():
    return sum([1, 2, 3, 4, 5])


print(func())
print(10 + func())
print(func() + func())


def func():
    return [1, 2, 3, 4, 5]


print(func())
print([10] + func())
print(func() + func())
list_1 = func()
list_1.reverse()
print(list_1)

'''

'''
def func():
    return [1, 2, 3, 4, 5]


list_1 = func()
list_1.reverse()
print(list_1)

'''
'''
def sum1():
    num1 , num2, num3 = 3 , 6 , 8
    print(num1+num2+num3)

sum1()

'''

'''
def sum2():
    num1, num2, num3 = 3, 6, 9
    return num1 + num2 + num3


print(sum2())

'''

'''
def sum3(num1, num2, num3):
    return num1 + num2 + num3


print(sum3(4, 5, 9))
print(sum3(14, 15, 19))
'''


def sum3(num1, num2, num3=34):
    return num1 + num2 + num3


print(sum3(4, 5))
print(sum3(4, 5, 19))

'''
def give_country_name(country='India'):
    print(country)

give_country_name()
give_country_name("USA")
'''
'''
def give_country_name(country='India'):
    print(country)

give_country_name("USA")

'''

'''
def sum_many_numbers(*args):  # arbitary arguments  we will give any name with *
    sum = 0
    for i in args:
        sum += i
    print(sum)


sum_many_numbers(1, 2, 3, 4)
sum_many_numbers(1)
sum_many_numbers()
sum_many_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''
'''
def sum_3_nums(n1, n2, n3):
    print(n1 + n2 + n3)


list_3 = [1, 3, 5]
sum_3_nums(*list_3)

'''

def sum1():
    num1, num2, num3 = 3, 6, 8
    print(num1+num2+num3)


sum1()

def sum2(num2,num3,num1):
    print(num3+num2+num1)

sum2(3, 7, 35)
sum2(467, 87 , 100)

def sum3(num2,num3,num1=50):
    print(num1+num2+num3)

sum3(3, 7)
sum3(467, 87 , 100)

def sum4(num2,num3,num1):
    return num1+num2+num3

print(sum4(3, 7, 20))
print(sum4(467, 87 , 100)-sum4(20,10,13))

def sum5(*args):
    sum = 0
    for i in args:
       sum +=i
    return sum

print(sum5(3))
print(sum5())
print(sum5(2,4))
print(sum5(4,5,6,7,8,9,10))

def full_name(lname,fname):
    return fname+lname

print(full_name('gandhi','mohandas'))
print(full_name(fname="raj",lname="kamal"))

def fullname2(**names):
    print(names['fname']+names['lname'])

fullname2(fname='Arjun',lname='arjya')

def fullname3(**names):
    name = ""
    for v in names.values():
        name += v
    print(name)

fullname3(fname='Arjitt',lname='arjya')


def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

def table_things1(name, *args, **kwargs):
    dinner = ""
    for key, value in kwargs.items():
        dinner += ( '{0}'.format(key, value))

    print (args[0]+name,"who is of age" , args[1], "has these items for dinner", dinner)

table_things1('kamal','raj',36, apple = 'fruit', cabbage = 'vegetable')


def sum3(list_dummy):
    print('line no 80')
    result = sum(list_dummy)
    print('inside sum3',result)
    return result


def calc():
    print('line no 87')
    list_1 = [10,34,56,70]
    sum3(list_1)



print('line no 91')
print('ia m calling calc()',calc())


#Sir code --

def sum1():
    num1, num2, num3 = 3, 6, 8
    print(num1+num2+num3)


sum1()

def sum2(num2,num3,num1):
    print(num3+num2+num1)

sum2(3, 7, 35)
sum2(467, 87 , 100)

def sum3(num2,num3,num1=50):
    print(num1+num2+num3)

sum3(3, 7)
sum3(467, 87 , 100)

def sum4(num2,num3,num1):
    return num1+num2+num3

print(sum4(3, 7, 20))
print(sum4(467, 87 , 100)-sum4(20,10,13))

def sum5(*args):
    sum = 0
    for i in args:
       sum +=i
    return sum

print(sum5(3))
print(sum5())
print(sum5(2,4))
print(sum5(4,5,6,7,8,9,10))

def full_name(lname,fname):
    return fname+lname

print(full_name('gandhi','mohandas'))
print(full_name(fname="raj",lname="kamal"))

def fullname2(**names):
    print(names['fname']+names['lname'])

fullname2(fname='Arjun',lname='arjya')

def fullname3(**names):
    name = ""
    for v in names.values():
        name += v
    print(name)

fullname3(fname='Arjitt',lname='arjya')


def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

def table_things1(name, *args, **kwargs):
    dinner = ""
    for key, value in kwargs.items():
        dinner += ( '{0}'.format(key, value))

    print (args[0]+name,"who is of age" , args[1], "has these items for dinner", dinner)

table_things1('kamal','raj',36, apple = 'fruit', cabbage = 'vegetable')


def sum3(list_dummy):
    print('line no 80')
    result = sum(list_dummy)
    print('inside sum3',result)
    return result


def calc():
    print('line no 87')
    list_1 = [10,34,56,70]
    sum3(list_1)



print('line no 91')
print('ia m calling calc()',calc())