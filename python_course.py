#!/usr/bin/env python
# coding: utf-8

# #                              ************python_course************

# # comment:

# In[1]:


#single line comment
print('polash')


# In[2]:


"""This
is
multiline comment"""
print("polash")


# In[3]:


'''This
is
multiline comment'''
print("polash")


# # variable:

# In[4]:


#Variables are containers for storing data values.
roll=3
name="polash"
print(roll)
print(name)
# python use dynamic typing:
a=3
print(a)
a="polash"
print(a)


# In[1]:


#Variable Names:
'''
*A variable name can only contain alpha-numeric characters
and underscores (A-z, 0-9, and _ ).
*A variable name cannot start with a number.
*Variable names are case-sensitive.
*Variable names can never contain spaces.
*Variable names may not be a reserved word in Python.
'''
# Find out reserved word in Python:
import keyword
print("List of reserved word:\n ",keyword.kwlist)


# In[2]:


name="Polash"
NAME="Touhid"
Name="Prince"
_name="Asad"
na_me="Mehedi"
name_="Raju"
nam2e="Saju"
name2="Shakib"

print(name)
print(NAME)
print(Name)
print(_name)
print(na_me)
print(name_)
print(nam2e)
print(name2)


# In[1]:


#Multiwords variable name:

#Cammel case:
myVariableName="Polash"
#Pascal case:
MyVariableName="Prince"
#Snake case:
my_variable_name="Asad"


print(myVariableName)
print(MyVariableName)
print(my_variable_name)


# In[5]:


#Multiple variable:

#Many value to multiple variable:
print("Many value to multiple variable:")
a,b,c,d=5,6,7,8   
print(a)
print(b)
print(c)
print(d)

#one value to multiple variable:
print("one value to multiple variable:")
a=b=c=d=5
print(a)
print(b)
print(c)
print(d)


# In[13]:


#Unpack a Collection:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("\n")
fruits = {"apple", "banana", "cherry"}
x, y, z = fruits
print(x)
print(y)
print(z)

print("\n")
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)


# In[14]:


#Global Variables & local Variables:

x = "awesome" #Global Variables

def myfunc():
  x = "fantastic" #local Variables
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[2]:


#Memory management for python variable:

a = 2
b=2
print('id(2) =', id(2))
print('id(a) =', id(a))
print('id(b) =', id(b))

#Here, both refer to the same object 2,so they have the same id().


# In[4]:


#Escape Sequence:

txt = 'It\'s alright.'  #Single Quote
print(txt) 

txt = "We are the so-called \"Vikings\" from the north." #double Quote
print(txt)

txt = "This will insert one \\ (backslash)." #Backslash
print(txt) 

txt = "Hello\nWorld!"  #New Line
print(txt) 

#create a new line
txt="c:\docs\nahid"
print(txt)

#without new line
txt=r"c:\docs\nahid"
print(txt)

txt = "Hello\tWorld!"  #Tab
print(txt) 


txt = "Hello \bWorld!" # Backspace 
print(txt) 

txt = "\110\145\154\154\157" #Octal value
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f" #Hex value
print(txt) 

txt = "\U0001F970"  #unicode for imoji
print(txt)

txt = "\U0001F60B"  #unicode for imoji
print(txt)


# # Data Types:

# In[21]:


x=None
print(x)
print(type(x))

a="polash"
print (a)
print(type(a))

b=3
print(b)
print(type(b))

c=5.55533
print(c)
print(type(c))

y=5.4545
print(f"{y:.2f}")# after (.) 2 value
print(type(y))

d=7j
print(d)
print(type(d))

e=True
print(e)
print(type(e))

f=range(5)
print(f)
print(type(f))

g=["Asad","Polash"]
print(g)
print(type(g))

h=("Asad","Polash")
print(h)
print(type(h))

i={"Asad","Polash"}
print(i)
print(type(i))

j={"Name":"Polash","Age":25}
print(j)
print(type(j))


# In[20]:


'''
Type Conversion:The process of converting the value of one data type 
to another data type is called type conversion. 
Python has two types of type conversion.

1.Implicit Type Conversion:Python automatically converts one data type to another data type.
2.Explicit Type Conversion:This type of conversion is also called typecasting 
because the user changes the data type of the objects.
'''
#Implicit Type Conversion:
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


print("\n")
#Explicit Type Conversion:
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))


# # Output formatting

# In[3]:


name="polash"
age=25
print(f"I am {name} and i am {age} years old.")


# In[1]:


a = 5
print('The value of a is', a)
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*') 
print(1, 2, 3, 4, sep='#', end='&')


# # User Input

# In[16]:



num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
print ("type of number", type(num))
print ("type of name", type(name1))
# user input always string type. we can change it type by type casting.


name=input("What is your name:")
birth_year=input("Write your birth year:")
age=2021-int(birth_year)
print(f"Hi {name} you are {age}")

'''
Python stops executing when it comes to the input() function,
and continues when the user has given some input.
'''
print("\n")


# # Operators:
# **Arithmetic operators**:

# In[5]:


x = 6
y = 4


print('x + y =',x+y)   #Addition

print('x - y =',x-y)   #Subtraction

print('x * y =',x*y)   #Multiplication

print('x / y =',x/y)   #Division

print('x // y =',x//y) #Floor division

print('x % y =',x%y)   #Modulus

print('x ** y =',x**y) #Exponentiation


# **Comparison operators**/**Relation operator**:

# In[7]:


x = 10
y = 12


print('x > y is',x>y)   #Greater than


print('x < y is',x<y)   #Less than


print('x == y is',x==y) #Equal to


print('x != y is',x!=y) #Not equal to


print('x >= y is',x>=y) #Greater than or equal to


print('x <= y is',x<=y) #Less than or equal to


# ***Bitwise operators***:

# In[4]:


'''In Python, bitwise operators are used to performing bitwise calculations on integers.
The integers are first converted into binary and then operations are performed on bit by bit,
hence the name bitwise operators. Then the result is returned in decimal format.

Note: Python bitwise operators work only on integers.
OPERATOR	DESCRIPTION	    SYNTAX
&	:Bitwise AND            x & y
|	:Bitwise OR             x | y
~	:Bitwise NOT            ~x
^	:Bitwise XOR            x ^ y
>>	:Bitwise right shift    x>>
<<	:Bitwise left shift	    x<<
'''
#Bitwise AND operator: Returns 1 if both the bits are 1 else 0.
'''
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a & b = 1010
         &
        0100
      = 0000
      = 0 (Decimal)
'''
#Bitwise or operator: Returns 1 if either of the bit is 1 else 0.
'''
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a | b = 1010
         |
        0100
      = 1110
      = 14 (Decimal)
      '''
#Bitwise not operator: Returns one’s complement of the number.
'''
a = 10 = 1010 (Binary)

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal)
'''
#Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
'''
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a ^ b = 1010            *1 true 1 false=1 else=0
         ^
        0100
      = 1110
      = 14 (Decimal)
'''
#Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left
'''
a = 10 = 0000 1010 (Binary)
a >> 1 = 0000 0101 = 5
'''
#Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as 
#                    a result
'''
a = 10 = 0000 1010 (Binary)
a << 1 = 0001 0100 = 20
 
'''

# bitwise operators

a = 10
b = 4


print("a & b =", a & b)

print("a | b =", a | b)

print("~a =", ~a)

print("a ^ b =", a ^ b)

print("a >> 1 =", a >> 1)

print("a << 1 =", a << 1)


# ***Assignment operators***:

# In[5]:


x = 5
print(x)


x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)


x = 5
x *= 3
print(x)


x = 5
x /= 3
print(x)


x = 5
x%=3
print(x)


x = 5
x//=3
print(x)


x = 5
x **= 3
print(x)


x = 5
x &= 3
print(x)


x = 5
x |= 3
print(x)


x = 5
x ^= 3
print(x)


x = 5
x >>= 3
print(x)


x = 5
x <<= 3
print(x)




# ***Logical Operators***:

# In[1]:


x = True
y = False

print('x and y :',x and y) # and:True if both the operands are true

print('x or y :',x or y)   #or:True if either of the operands is true

print('not x :',not x)     #not:True if operand is false 


# **Membership operators**:

# In[3]:


#in:True if value/variable is found in the sequence.
#not in:True if value/variable is not found in the sequence.
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x)

print('hello' not in x)

print(1 in y)

print('a' in y)

'''Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive).
Similarly, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False'''
print("\n")


# **Identity operators**:

# In[6]:


#Identity operators works under the memory location.

#is:True if the operands are identical.
#is not:True if the operands are not identical
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]


print(x1 is not y1)

print(x2 is y2)

print(x3 is y3)

'''Here, we see that x1 and y1 are integers of the same values, 
so they are equal as well as identical. Same is the case with x2 and y2 (strings).

But x3 and y3 are lists. They are equal but not identical.
It is because the interpreter locates them separately in memory although they are equal.'''
print("\n")


# ***Ternary Operator***:

# In[3]:


#Ternary Operator:it's must be one line condition.
num=int(input("Enter number to check :"))
msg=str(num)+" is an even number" if num%2==0 else str(num)+"is an odd number"
print(msg)


# ***math funtion***:

# In[20]:


from math import *


# In[15]:


math.ceil(23.5)


# In[12]:


math.floor(23.5)


# In[13]:


math.sqrt(25)


# In[16]:


math.pow(2,3)


# In[22]:


max(55,60,70)


# In[23]:


min(55,60,40)


# In[35]:


abs(-4)


# In[28]:


round(4.44)


# In[29]:


round(4.88)


# In[30]:


round(4.55)


# In[31]:


round(4.4444,1)


# In[32]:


round(4.4444,2)


# In[33]:


round(4.4444,3)


# In[ ]:





# # If ... Else:

# In[4]:


#Simple if:
n = 10
if n % 2 == 0:
   print("n is an even number")


# In[2]:


#if-else:
n = 5
if n % 2 == 0:
   print("n is even")
else:
   print("n is odd")


# In[5]:


#nested if:
a = 5
b = 10
c = 15
if a > b:
   if a > c:
      print("a value is big")
   else:
       print("c value is big")
elif b > c:
    print("b value is big")
else:
     print("c is big")


# In[6]:


#if-elif-else:
x = 15
y = 12
if x == y:
   print("Both are Equal")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")


# # Loops:

# In[10]:


# for loop:
for x in "banana":
  print(x)


# In[11]:


#Break statement with for loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# In[12]:


#continue statement with for loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# In[13]:


#while loop:
i = 1
while i < 6:
  print(i)
  i += 1


# In[14]:


#Break statement with while loop:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[15]:


#continue statement with while loop:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# # Strings:

# In[24]:


#string:sequence of character
#single line string:
name='polash'
print(name)
subject="Computer Science and Engineering"
print(subject)


# In[29]:


#multiline string:
s='''This is
multiline string'''
print(s,"\n")

introduce="""Hi this is polash.
I study at Dhaka International University of Computer Science Engineering.
I am currently 25 years old"""
print(introduce)


# In[31]:


#String Length:
name = "polash"
print(len(name))


# In[35]:


#Check String:
name_list = "polash,asad,prince"
if "asad" in name_list:
  print("Yes, 'asad' is present.")

name_list = "polash,asad,prince"
if "Raju" not in name_list:
  print("No, 'Raju' is not present.")


# In[33]:


#Looping Through a String:
for x in "polash":
  print(x)


# ***Slicing Strings:***:

# In[37]:


a = "Polash"
print(a[4]) #indexing string


# In[42]:


a = "Polash"
print(a[-1]) #indexing string


# In[43]:


b = "Polash"
print(b[:3])


# In[44]:


b = "Polash"
print(b[2:])


# In[45]:


b = "Polash"
print(b[2:5])


# In[46]:


b = "Polash"
print(b[:-1])


# In[49]:


b = "Polash"
print(b[-4:])


# In[50]:


b = "Polash"
print(b[-5:-2])


# In[51]:


b = "Polash"
print(b[:])


# In[52]:


b = "Polash"
print(b[::2])


# In[53]:


b = "Polash"
print(b[::3])


# In[37]:


b = "Polash"
print(b[:4:3])


# In[38]:


b = "Polash"
print(b[2::3])


# In[40]:


b = "Polash"
print(b[1:4:3])


# In[10]:


my_string = "0123456789"
print(my_string[-2: -6: -2])


# ***String Methods***:

# In[1]:


#capitalize:
a="THIS IS POLASH"
print(a.capitalize())


# In[59]:


#Upper Case:
a = "Polash mia"
print(a.upper())


# In[60]:


#Lower Case:
a = "Polash mia"
print(a.lower())


# In[61]:


#Title:
a = "Polash mia"  #Make the first letter in each word upper case:
print(a.title())


# In[64]:


#Remove Whitespace:
a = "     Polash mia    "  #removes any whitespace from the beginning or the end
print(a.strip())


# In[65]:


#Replace String:
a = a = "Polash mia" 
print(a.replace("m", "e"))


# In[73]:


#Split String:
a = "Md Polash mia" 
print(a.split(" "))
print(a.split("s"))


# In[74]:


#String count:
a = "I love apples, apple are my favorite fruit"
x = a.count("apple")
print(x)


# In[77]:


#String Concatenation:
a = "Polash"
b = "Mia"
c = a + b
print(c)

a = "Polash"
b = "Mia"
c = a + " " + b
print(c)


# In[92]:


#String multiplication:
print("Polash "*3)
print(3*"Polash ")
print(3*("Polash "))
print(3*("Polash ","Mia"))
print(3*["Polash "])


# # List

# In[1]:


#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets and separated by commas.
#List items are ordered, changeable, and allow duplicate values.
friuts = ["apple", "banana", "cherry"]
print(friuts)


# In[2]:


# empty list
my_list = []
print(my_list)


# In[3]:


# list of integers
my_list = [1, 2, 3]
print(my_list)


# In[4]:


# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)


# In[5]:


# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list)


# ***List Index***:

# In[26]:


my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  
print(my_list[2])  
print(my_list[4]) 


# In[29]:


# Nested indexing
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])
print(n_list[1][3])


# In[30]:


# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])


# In[15]:


#change the value of a specific item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#change the value of items within a specific range:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[13]:


#List Length:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[4]:


#Membership:
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']


print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)


# ***list slice***:

# In[1]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[:3])


# In[2]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[2:])


# In[3]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[2:5])


# In[4]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[:-1])


# In[5]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[-4:])


# In[6]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[-5:-2])


# In[7]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[:])


# In[8]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[::2])


# In[9]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[::3])


# In[10]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[:7:3])


# In[11]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[2::3])


# In[12]:


b = ['p','r','o','g','r','a','m','i','z']
print(b[2:7:3])


# ***List Methods***:

# In[18]:


#index():Returns the index of the first element with the specified value
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8))

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)


# In[8]:


#append():Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# In[14]:


#insert():Adds an element at the specified position
fruits = ['apple','cherry', 'banana']
fruits.insert(1, "orange")
print(fruits)


# In[25]:


#extend():adds the specified list elements (or any iterable(list, set, tuple, etc.)) 
#         to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo'] # add list
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9) # add tuple
fruits.extend(points)
print(fruits)


# another way Join Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#or use  loop:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[16]:


#count():Returns the number of elements with the specified value
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.count(8))


# In[11]:


#copy():Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)


# In[12]:


#sort():Sorts the list
my_list = [3, 8, 1, 6, 0, 8, 4]
my_list.sort()
print(my_list)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)


# In[15]:


#reverse():Reverses the order of the list
my_list = [3, 8, 1, 6, 0, 8, 4]
my_list.reverse()
print(my_list)


fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


# In[20]:


#remove():removes the first occurrence of the element with the specified value.
fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("banana")
print(fruits)


# In[24]:


#pop():removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)


# In[19]:


#clear(): removes all the elements from a list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)


# # Tuple

# In[1]:


#Tuples are used to store multiple items in a single variable.
#Tuples are written with round brackets.
#A tuple is a collection which is ordered and unchangeable.

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


# ***Tuple Indexing***:

# In[2]:


# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   
print(my_tuple[5])  


# In[3]:


# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       
print(n_tuple[1][1])      


# In[4]:


# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[-1])
print(my_tuple[-6])


# ***Tuple Slicing***:

# In[1]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[:3])


# In[2]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[2:])


# In[3]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[2:5])


# In[4]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[:-1])


# In[5]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[-4:])


# In[6]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[-5:-2])


# In[7]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[:])


# In[8]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[::2])


# In[9]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[::3])


# In[10]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[:7:3])


# In[11]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[2::3])


# In[12]:


b = ('p','r','o','g','r','a','m','i','z')
print(b[2:7:3])


# ***Changing a Tuple***:

# In[13]:


#tuple cannot change, add, or remove items once the tuple is created.
#But,if the element is itself a mutable data type like a list,its nested items can be changed.
my_tuple = (4, 2, 3, [6, 5])
my_tuple[1] = 9


# In[18]:


my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    
print(my_tuple)


# In[23]:


#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)

print(x)


# In[24]:


#Add tuple to a tuple to be able to change it:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# In[25]:


#Using Asterisk*:If the number of variables is less than the number of values,
#                you can add an * to the variable name and the values will be assigned
#                to the variable as a list:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# In[20]:


#concatenation:We can use + operator to combine two tuples. This is called concatenation.
print((1, 2, 3) + (4, 5, 6))

#multiplication/repeat :We can also repeat the elements in a tuple 
#                       for a given number of times using the * operator.
print(("Repeat",) * 3)


# In[21]:


#Tuple Length:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# In[28]:


#Tuple Membership Test:

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print('a' in my_tuple)
print('b' in my_tuple)

print('g' not in my_tuple)


# In[29]:


#Iterating Through a Tuple:
for name in ('John', 'Kate'):
    print("Hello", name)


# In[32]:


#Deleting a Tuple:we cannot delete or remove items from a tuple
                
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
del my_tuple[3]


# In[33]:


#But Deleting a tuple entirely, however, is possible using the keyword del.
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
del my_tuple
print(my_tuple)


# ***Methods***:

# In[26]:


#count():returns the number of times a specified value appears in the tuple.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


# In[27]:


#index():finds the first occurrence of the specified value.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)


# # Sets

# In[44]:


#Sets are used to store multiple items in a single variable.
#Sets are written with curly brackets.
#Set items are unordered, unchangeable, and do not allow duplicate values,
#set cannot have mutable items

#string
set1 = {"apple", "banana", "cherry"}
print(set1)

#integer
set2 = {1, 5, 7, 9, 3}
print(set2)

#boolean
set3 = {True, False, False}
print(set3)

#A set can contain different data types:
set4 = {"abc", 34, True, 40,34, "male"} #unordered,do not allow duplicate values
print(set4)

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)


my_set = {1, 2, [3, 4]} #set cannot have mutable items
print(my_set)


# In[46]:


#We cannot access or change an element of a set using indexing or slicing
my_set = {1, 3}
print(my_set[0])


# In[47]:


#But you can loop through the set items using a for loop:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[48]:


# ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# In[6]:


#Length of a Set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# ***Set Operations***:

# In[2]:


#Set Union:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)


# In[3]:


#Set Intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)


# In[4]:


#Set Difference:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)


# In[5]:


#Set Symmetric Difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)


# # Set Methods

# In[7]:


#add():adds an element to the set.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[8]:


#clear():removes all elements in a set.
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)


# In[9]:


#copy():returns a shallow copy of the set.
numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)


# In[11]:


#union():Return a set that contains all items from both sets, duplicates are excluded
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))

print('A.union() =', A.union())


# In[14]:


#intersection():returns a new set with elements that are common to all sets.
A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))


# In[36]:


#intersection_update():Removes the items in this set that are not present 
#                      in other, specified set
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)


# In[10]:


#difference():The returned set contains items that exist only in the first set,
#             and not in both sets.

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivalent to A-B
print(A.difference(B))

# Equivalent to B-A
print(B.difference(A))


# In[12]:


#difference_update():Remove the items that exist in both sets
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)


# In[16]:


#discard():removes the specified item from the set.
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)


# In[17]:


#isdisjoint():returns True if two sets are disjoint sets. If not, it returns False.
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))


# In[19]:


#issubset():returns True if all elements of a set are present in another set 
#          (passed as an argument). If not, it returns False.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}


print(A.issubset(B))

print(B.issubset(A))

print(A.issubset(C))

print(C.issubset(B))


# In[ ]:


#issuperset():returns True if a set has every elements of another set (passed as an argument).
#             If not, it returns False.

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))


# In[31]:


#pop():Remove a random item from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)

#Return the removed element:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop() 
print(x)


# In[32]:


#remove():removes the specified element from the set.

languages = {'Python', 'Java', 'English'}
languages.remove('English')

print(languages)


# In[33]:


#symmetric_difference():The returned set contains a mix of items 
#                       that are not present in both sets.
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))


# In[34]:


#symmetric_difference_update():Remove the items that are present in both sets,
#                              AND insert the items that is not present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) 

print(x)


# In[35]:


#update():updates the current set, by adding items from another set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 

print(x)


# # Dictionaries

# In[9]:


#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
#access the items of a dictionary by referring to its key name, inside square brackets
print(thisdict["brand"])
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)


# In[5]:


#Change Values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


# In[8]:


# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)


# # Datetime

# In[1]:


import datetime

x = datetime.datetime.now()

print(x)


# In[11]:


x = 20
y = 5
result = (x + True) / (4 - y * False)
print(result)


# In[ ]:




