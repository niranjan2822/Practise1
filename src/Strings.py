'''a = "hello , world"
print(a[1])

a = "helloworld"
print(a[8])

b = "Bangalore!"
print(b[2:6])

b = "Helloworld!"
print(b[2:5])
'''

c = "Bangalore!"  # will ask to sir
print(c[-2:-4])
print(c[-4:-2])

b = "Hello, World!"
print(b[-5:-2])

b = "Kolkata!!"
print(len(b))

b = "Hello, World!"
print(len(b))

c = "      Bengaluru , Kolkata!"  # will ask to sir
print(c.strip())

b = "  Hello , World! "  # will ask to sir
print(b.strip())

# lower methiod
a = "Hello, World!"
print(a.lower())

# replace method
a = "Hello, World!"
print(a.replace("H", "J"))

a = "I'm python devloper "
print(a.replace("o", "sss"))

# Split method

a = "Hello, World!"
b = a.split(",")
print(b)

a = "Bangalore, kolkata"  # will ask to sir
b = a.split(",")
print(b)

a = "bangalore"
b = a.split('----')
print(b)

# in command

txt = "instrument is piano"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

#Format()  method

age = 45
txt= "My name is niranjan , and I am {}"
print(txt.format(age))

name = "c0imbat0re"

#['c','o','i','m','b','a','t','o','r','e']
#  0   1   2   3   4   5   6   7  8   9
# -10                  -5  -4  -3 -2 -1

# varibale[start_index:length:step=1] 10
print(name[0:10])
print(name[-10:])
print(name[::])
print(name[0:10:1])
print(name[::-1])

#length/size -- 10 ---> indexing 0 to 9

val = 'o'
'''
print(name.capitalize())
print(name.upper())
print(name.count(val))
print(name.endswith('re'))
#print(name.index('o'))
print(len(name.strip()))
print(name.strip().isnumeric())
number = "23242"
print(number.isnumeric())
name = 'kamal'
age = 34
sal = 1000.00
sentence = 'my name is {0}. i am {1}. i have {2}'
print(sentence.format(name,age,sal))
print(sentence.format('anna',38,2300.00))
senetence = 'my name is '+name+'. i am '+str(age)+'. i have '+str(sal)
print(senetence)
'''

name = 'kamal'
age = 34
sal = 1000.00

sentence = 'my name is {0}. i am {1}. i have {2}'
print(sentence.format(name,age,sal))
print(sentence.format("Naren",39,2000.00))
#                       0     1     2
sentence = 'my name is {name}. i am {age}. i have {sal}'
print(sentence.format(name = "Kamal", age = 35, sal = 1000.0))
print(sentence.format(name = "raj", age = 25, sal = 7000.0))

a = "Hello, World!"
print(a.replace("ll", "11"))


list_of_fruits = "apple, orange, guava,pear"
print(list_of_fruits.split(","))


text = "There is an apple in the table"

print("le" in text)
print("orange" not in text)


val1 = "apple"
val2 = "orange"
val3 = "pear"

print(val1+" "+val2)
print(val1,val2)
print(val1,val2,val3,sep=", ")

print(val1 == val2)

print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))

x = "300"
print(isinstance(x, str))



