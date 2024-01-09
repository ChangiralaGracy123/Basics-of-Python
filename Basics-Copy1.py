#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import keyword
import operator
from datetime import datetime
import os


# In[2]:


print(keyword.kwlist)  # List all Python Keywords


# In[3]:


len(keyword.kwlist)  # Python contains 35 keywords


# In[4]:


1var = 10 #Identifier can't start with a digit


# In[5]:


val2@ = 35 # Identifier can't use special symbols 


# In[6]:


1var = 10 #Identifier can't start with a digit


# In[8]:


"""
Correct way of defining an identifier 
(Identifiers can be a combination of letters in lowercase (a to z) or uppercase (
"""
val2 = 10


# In[9]:


val_ = 99


# In[10]:


# Single line comment
val1 = 10


# In[11]:


# Multiple 
# line 
# comment
val1 = 10


# In[12]:


'''
Multiple 
line 
comment
'''
val1 = 10


# In[13]:


"""
Multiple 
line 
comment
"""
val1 = 10


# In[14]:


# Single line statement
p1 = 10 + 20
p1


# In[15]:


# Single line statement
p2 = ['a' , 'b' , 'c' , 'd']
p2


# In[16]:


# Multiple line statement
p1 = 20 + 30 \
 + 40 + 50 +\
 + 70 + 80
p1


# In[17]:


# Multiple line statement
p2 = ['a' , 
 'b' , 
 'c' , 
 'd'
 ]
p2


# In[18]:


p = 10
if p == 10:
 print ('P is equal to 10') # correct indentation


# In[19]:


# if indentation is skipped we will encounter "IndentationError: expected an inde
p = 10
if p == 10:
print ('P is equal to 10')


# In[20]:


for i in range(0,5):
 print(i) # correct indentation


# In[21]:


# if indentation is skipped we will encounter "IndentationError: expected an inde
for i in range(0,5):
print(i)


# In[22]:


for i in range(0,5): print(i) # correct indentation but less readable


# In[23]:


j=20
for i in range(0,5):
 print(i) # inside the for loop
print(j) # outside the for loop


# In[24]:


def square(num):
 '''Square Function :- This function will return the square of a number'''
 return num**2


# In[25]:


square(2)


# In[26]:


square.__doc__ # We can access the Docstring using __doc__ method


# In[33]:


def evenodd(num):
    '''evenodd Function :- This function will test whether a number is Even or Odd'''
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


# In[34]:


evenodd(3)


# In[35]:


evenodd(2)


# In[36]:


evenodd.__doc__


# In[37]:


p = 30


# In[38]:


'''
id() function returns the “identity” of the object. 
The identity of an object - Is an integer
 - Guaranteed to be unique
 - Constant for this object during its lifetime. 
'''
id(p)


# In[39]:


hex(id(p)) # Memory address of the variable


# In[40]:


p = 20  # Creates an integer object with value 20 and assigns the variable p to it
q = 20  # Creates a new reference q which will point to the value 20. p & q will point to the same object.
r = q   # Variable r will also point to the same location where p & q are pointing


# In[41]:


(20, int, '0x7fff6d71a3f0')


# In[42]:


q , type(q), hex(id(q)) 


# In[43]:


r , type(r), hex(id(r)) 


# In[44]:


p = 20
p = p + 10 # Variable Overwriting
p


# In[45]:


intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable
print(intvar)
print(floatvar)
print(strvar)


# In[46]:


intvar , floatvar , strvar = 10,2.57,"Python Language" # Using commas to separate
print(intvar)
print(floatvar)
print(strvar)


# In[47]:


p1 = p2 = p3 = p4 = 44 # All variables pointing to same value
print(p1,p2,p3,p4)


# In[48]:


val1 = 10  # Integer data type
print(val1)  # Output: 10
print(type(val1))  # Output: <class 'int'>
print(sys.getsizeof(val1))  # Output: 28 (the size of an integer object in bytes may vary depending on the platform)
print(val1, " is Integer?", isinstance(val1, int))  # Output: 10 is Integer? True


# In[51]:


val2 = 92.78  # Float data type
print(val2)
print(type(val2))  # type of object
print(sys.getsizeof(val2))  # size of float object in bytes
print(val2, " is float?", isinstance(val2, float))  # val2 is an instance of float


# In[52]:


val3 = 25 + 10j  # Complex data type
print(val3)
print(type(val3))  # type of object
print(sys.getsizeof(val3))  # size of complex object in bytes
print(val3, " is complex?", isinstance(val3, complex))  # val3 is an instance of complex


# In[53]:


sys.getsizeof(int()) # size of integer object in bytes 


# In[54]:


sys.getsizeof(float()) # size of float object in bytes


# In[55]:


sys.getsizeof(complex()) # size of complex object in bytes


# In[56]:


bool1 = True


# In[57]:


bool2 = False


# In[58]:


print(type(bool1))


# In[59]:


isinstance(bool1, bool)


# In[60]:


bool(0)


# In[61]:


bool(1)


# In[62]:


bool(None)


# In[63]:


bool (False)


# In[64]:


str1 = "HELLO PYTHON"
print(str1)


# In[65]:


mystr = 'Hello World' # Define string using single quotes
print(mystr)


# In[66]:


mystr = "Hello World" # Define string using double quotes
print(mystr)


# In[67]:


mystr = '''Hello 
 World ''' # Define string using triple quotes
print(mystr)


# In[68]:


mystr = """Hello
 World""" # Define string using triple quotes
print(mystr)


# In[69]:


mystr = ('Happy '
 'Monday '
 'Everyone')
print(mystr)


# In[70]:


mystr2 = 'Woohoo '
mystr2 = mystr2*5
mystr2


# In[71]:


len(mystr2) # Length of string


# In[72]:


str1


# In[73]:


str1[0] # First character in string "str1"


# In[74]:


str1[len(str1)-1] # Last character in string using len function


# In[75]:


str1[-1] # Last character in string


# In[76]:


str1[6] #Fetch 7th element of the string 


# In[77]:


str1[5]


# In[78]:


str1[0:5] # String slicing 


# In[79]:


str1[6:12] # String slicing 


# In[80]:


str1[-4:]  # Retreive last four characters of the strin


# In[81]:


str1[-6:]  # Retreive last six characters of the string


# In[82]:


str1[:4] # Retreive first four characters of the string


# In[83]:


str1[:6] # Retreive first six characters of the string


# In[84]:


str1


# In[85]:


#Strings are immutable which means elements of a string cannot be changed once th
str1[0:5] = 'HOLAA'


# In[86]:


del str1 # Delete a string
print(srt1)


# In[87]:


# String concatenation
s1 = "Hello"
s2 = "Asif"
s3 = s1 + s2
print(s3)


# In[88]:


# String concatenation
s1 = "Hello"
s2 = "Asif"
s3 = s1 + " " + s2
print(s3)


# In[89]:


mystr1 = "Hello Everyone"


# In[90]:


# Iteration 
for i in mystr1:
 print(i)


# In[91]:


for i in enumerate(mystr1):
 print(i)


# In[92]:


list(enumerate(mystr1)) 


# In[93]:


# String membership
mystr1 = "Hello Everyone"

# Check whether substring "Hello" is present in the string
print('Hello' in mystr1)

# Check whether substring "Everyone" is present in the string
print('Everyone' in mystr1)

# Check whether substring "Hi" is present in the string
print('Hi' in mystr1)


# In[96]:


"""
The partition("and") method will split the string into three parts using the separator "and". The result is a tuple where:

The first element contains the part before the first occurrence of "and".
The second element contains the "and" itself.
The third element contains the part after the first occurrence of "and".
"""
str5 = "Natural language processing with Python and R and Java"
L = str5.partition("and") 
print(L)


# In[97]:


mystr2 = " Hello Everyone "
mystr2


# In[98]:


mystr2.strip() # Removes white space from begining & end


# In[99]:


mystr2.rstrip() # Removes all whitespaces at the end of the string


# In[100]:


mystr2.lstrip() # Removes all whitespaces at the begining of the string


# In[101]:


mystr2 = "*********Hello Everyone***********All the Best**********"
mystr2


# In[102]:


mystr2.strip('*') # Removes all '*' characters from begining & end of the string


# In[103]:


mystr2.rstrip('*') # Removes all '*' characters at the end of the string


# In[104]:


mystr2.lstrip('*') # Removes all '*' characters at the begining of the string


# In[105]:


mystr2 = " Hello Everyone "


# In[106]:


mystr2.lower() # Return whole string in lowercase 


# In[107]:


mystr2.upper() # Return whole string in uppercase 


# In[108]:


mystr2.replace("He" , "Ho") #Replace substring "He" with "Ho"


# In[109]:


mystr2.replace(" " , "") # Remove all whitespaces using replace function


# In[110]:


mystr5 = "one two Three one two two three"


# In[111]:


mystr5.count("one") # Number of times substring "one" occurred in string.


# In[112]:


mystr5.count("two") # Number of times substring "two" occurred in string.


# In[113]:


mystr5.startswith("one") # Return boolean value True if string starts with "one"


# In[114]:


mystr5.endswith("three") # Return boolean value True if string ends with "three"


# In[118]:


mystr4 = "one two three four one two two three five five six seven six seven one one one ten eight ten nine eleven ten ten nine"


# In[119]:


mylist = mystr4.split() # Split String into substrings
mylist


# In[120]:


# Combining string & numbers using format method
item1 = 40
item2 = 55
item3 = 77
res = "Cost of item1 , item2 and item3 are {} , {} and {}"
print(res.format(item1,item2,item3))


# In[121]:


# Combining string & numbers using format method
item1 = 40
item2 = 55
item3 = 77
res = "Cost of item3 , item2 and item1 are {2} , {1} and {0}"
print(res.format(item1,item2,item3))


# In[122]:


str2 = " WELCOME EVERYONE "
str2 = str2.center(100) # center align the string using a specific character as t
print(str2)


# In[123]:


str2 = " WELCOME EVERYONE "
str2 = str2.center(100,'*') # center align the string using a specific character 
print(str2)


# In[125]:


str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50) # Right align the string using a specific character as the 
print(str2)


# In[126]:


str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50,'*') # Right align the string using a specific character ('*
print(str2)


# In[127]:


str4 = "one two three four five six seven"
loc = str4.find("five") # Find the location of word 'five' in the string "str4"
print(loc)


# In[128]:


str4 = "one two three four five six seven"
loc = str4.index("five") # Find the location of word 'five' in the string "str4"
print(loc)


# In[129]:


mystr6 = '123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are letter
print(mystr6.isalnum()) # returns True if a string contains only letters or number
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


# In[130]:


mystr6 = 'abcde'
print(mystr6.isalpha()) # returns True if all the characters in the text are letter
print(mystr6.isalnum()) # returns True if a string contains only letters or number
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


# In[131]:


mystr6 = 'abc12309'
print(mystr6.isalpha()) # returns True if all the characters in the text are letter
print(mystr6.isalnum()) # returns True if a string contains only letters or number
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


# In[132]:


mystr7 = 'ABCDEF'
print(mystr7.isupper()) # Returns True if all the characters are in upper case
print(mystr7.islower()) # Returns True if all the characters are in lower case


# In[133]:


mystr8 = 'abcdef'
print(mystr8.isupper()) # Returns True if all the characters are in upper case
print(mystr8.islower()) # Returns True if all the characters are in lower case


# In[137]:


str6 = "one two three four one two two three five five six one ten eight ten nine"
loc = str6.rfind("one") # last occurrence of word 'one' in string "str6"
print(loc)


# In[138]:


loc = str6.rindex("one") # last occurrence of word 'one' in string "str6"
print(loc)


# In[139]:


txt = " abc def ghi "
txt.rstrip()


# In[140]:


txt = " abc def ghi "
txt.lstrip()


# In[142]:


'abc def ghi '


# In[143]:


txt = " abc def ghi "
txt.strip()


# In[144]:


#Using double quotes in the string is not allowed.
mystr = "My favourite TV Series is "Game of Thrones""


# In[145]:


#Using escape character to allow illegal characters
mystr = "My favourite series is \"Game of Thrones\""
print(mystr)


# In[146]:


list1 = [] # Empty List


# In[147]:


print(type(list1))


# In[148]:


list2 = [10,30,60] # List of integers numbers


# In[149]:


list3 = [10.77,30.66,60.89] # List of float numbers


# In[150]:


list4 = ['one','two' , "three"] # List of strings


# In[151]:


list5 = ['Asif', 25 ,[50, 100],[150, 90]] # Nested Lists


# In[152]:


list6 = [100, 'Asif', 17.765] # List of mixed data types


# In[153]:


list7 = ['Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'}]


# In[154]:


len(list6) #Length of list


# In[155]:


list2[0] # Retreive first element of the list


# In[156]:


list4[0] # Retreive first element of the list


# In[157]:


list4[0][0] # Nested indexing - Access the first character of the first list element


# In[158]:


list4[-1] # Last item of the list


# In[159]:


list5[-1] # Last item of the list


# In[161]:


mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']


# In[162]:


mylist[0:3] # Return all items from 0th to 3rd index location excluding the item 


# In[163]:


mylist[2:5] # List all items from 2nd to 5th index location excluding the item at


# In[164]:


mylist[:3] # Return first three items


# In[165]:


mylist[:2] # Return first two items


# In[166]:


mylist[-3:] # Return last three items


# In[167]:


mylist[-2:] # Return last two items


# In[168]:


mylist[-1] # Return last item of the list


# In[169]:


mylist[:] # Return whole list


# In[170]:


mylist


# In[171]:


mylist.append('nine') # Add an item to the end of the list 
mylist


# In[172]:


mylist.insert(9,'ten') # Add item at index location 9
mylist


# In[173]:


mylist.insert(1,'ONE') # Add item at index location 1
mylist


# In[174]:


mylist.remove('ONE') # Remove item "ONE"
mylist


# In[175]:


mylist.pop() # Remove last item of the list
mylist


# In[176]:


mylist.pop(8) # Remove item at index location 8
mylist


# In[177]:


del mylist[7] # Remove item at index location 7
mylist


# In[178]:


# Change value of the string
mylist[0] = 1
mylist[1] = 2
mylist[2] = 3
mylist


# In[179]:


mylist.clear() # Empty List / Delete all items in the list
mylist


# In[180]:


del mylist # Delete the whole list
mylist


# In[181]:


mylist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']


# In[182]:


mylist1 = mylist # Create a new reference "mylist1" 


# In[183]:


id(mylist) , id(mylist1) # The address of both mylist & mylist1 will be the same


# In[184]:


mylist2 = mylist.copy() # Create a copy of the list


# In[185]:


id(mylist2) # The address of mylist2 will be different from mylist because mylist


# In[186]:


mylist[0] = 1


# In[187]:


mylist


# In[188]:


mylist1 # mylist1 will be also impacted as it is pointing to the same list


# In[189]:


mylist2 # Copy of list won't be impacted due to changes made on the original list


# In[190]:


list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']


# In[191]:


list3 = list1 + list2 # Join two lists by '+' operator
list3


# In[192]:


list1.extend(list2) #Append list2 with list1
list1


# In[193]:


list1


# In[194]:


'one' in list1 # Check if 'one' exist in the list


# In[195]:


'ten' in list1 # Check if 'ten' exist in the list


# In[196]:


if 'three' in list1: # Check if 'three' exist in the list
 print('Three is present in the list')
else:
 print('Three is not present in the list')


# In[197]:


if 'eleven' in list1: # Check if 'eleven' exist in the list
 print('eleven is present in the list')
else:
 print('eleven is not present in the list')


# In[198]:


list1


# In[199]:


list1.reverse() # Reverse the list
list1


# In[200]:


list1 = list1[::-1] # Reverse the list
list1


# In[201]:


mylist3 = [9,5,2,99,12,88,34]
mylist3.sort() # Sort list in ascending order
mylist3


# In[202]:


mylist3 = [9,5,2,99,12,88,34]
mylist3.sort(reverse=True) # Sort list in descending order
mylist3


# In[203]:


mylist4 = [88,65,33,21,11,98]
sorted(mylist4) 


# In[204]:


mylist4


# In[205]:


list1


# In[206]:


for i in list1:
 print(i)


# In[207]:


for i in enumerate(list1):
 print(i)


# In[208]:


list10 =['one', 'two', 'three', 'four', 'one', 'one', 'two', 'three']


# In[209]:


list10.count('one') # Number of times item "one" occurred in the list.


# In[210]:


list10.count('two') # Occurence of item 'two' in the list


# In[211]:


list10.count('four') #Occurence of item 'four' in the list


# In[212]:


L1 = [1,2,3,4,0]


# In[213]:


all(L1) # Will Return false as one value is false (Value 0)


# In[214]:


any(L1) # Will Return True as we have items in the list with True value


# In[215]:


L2 = [1,2,3,4,True,False]


# In[216]:


all(L2) # Returns false as one value is false


# In[217]:


any(L2) # Will Return True as we have items in the list with True value


# In[218]:


L3 = [1,2,3,True]


# In[219]:


all(L3) # Will return True as all items in the list are True


# In[220]:


any(L3) # Will Return True as we have items in the list with True value


# In[221]:


mystring = "WELCOME"
mylist = [ i for i in mystring ] # Iterating through a string Using List Comprehe
mylist


# In[222]:


mylist1 = [ i for i in range(40) if i % 2 == 0] # Display all even numbers betwee
mylist1


# In[223]:


mylist2 = [ i for i in range(40) if i % 2 == 1] # Display all odd numbers between
mylist2


# In[224]:


mylist3 = [num**2 for num in range(10)] # calculate square of all numbers between
mylist3


# In[225]:


# Multiple whole list by 10
list1 = [2,3,4,5,6,7,8]
list1 = [i*10 for i in list1]
list1


# In[226]:


#List all numbers divisible by 3 , 9 & 12 using nested "if" with List Comprehensi
mylist4 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0]
mylist4


# In[230]:


# Odd even test
l1 = [print("{} is Even Number".format(i)) if i % 2 == 0 else print("{} is Odd Number".format(i)) for i in range(1, 11)]


# In[231]:


# Extract numbers from a string
mystr = "One 1 two 2 three 3 four 4 five 5 six 6789"
numbers = [i for i in mystr if i.isdigit()]
numbers


# In[232]:


# Extract letters from a string
mystr = "One 1 two 2 three 3 four 4 five 5 six 6789"
numbers = [i for i in mystr if i.isalpha()]
numbers


# In[233]:


tup1 = () # Empty tuple


# In[234]:


tup2 = (10,30,60) # tuple of integers numbers


# In[235]:


tup3 = (10.77,30.66,60.89) # tuple of float numbers


# In[236]:


tup4 = ('one','two' , "three") # tuple of strings


# In[237]:


tup5 = ('Asif', 25 ,(50, 100),(150, 90)) # Nested tuples


# In[238]:


tup6 = (100, 'Asif', 17.765) # Tuple of mixed data types


# In[239]:


tup7 = ('Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'} , (99,22,33))


# In[240]:


len(tup7) #Length of list


# In[241]:


tup2[0] # Retreive first element of the tuple


# In[242]:


tup4[0] # Retreive first element of the tuple


# In[243]:


tup4[0][0] # Nested indexing - Access the first character of the first tuple elem


# In[244]:


tup4[-1] # Last item of the tupl


# In[245]:


tup5[-1] # Last item of the tuple


# In[315]:


mytuple = ('one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight')


# In[271]:


mytuple[0:3] # Return all items from 0th to 3rd index location excluding the item


# In[287]:


mytuple[2:5] # List all items from 2nd to 5th index location excluding the item a


# In[288]:


mytuple[:3] # Return first three items


# In[289]:


mytuple[:2] # Return first two items


# In[275]:


mytuple[-3:] # Return last three items


# In[290]:


mytuple[-2:] # Return last two items


# In[291]:


mytuple[-1] # Return last item of the tuple


# In[292]:


mytuple[:] # Return whole tuple


# In[303]:


mytuple


# In[304]:


for i in mytuple:
 print(i)


# In[305]:


for i in enumerate(mytuple):
 print(i)


# In[306]:


del mytuple # Deleting entire tuple object is possible


# In[307]:


mytuple1 =('one', 'two', 'three', 'four', 'one', 'one', 'two', 'three')


# In[308]:


mytuple1.count('one') # Number of times item "one" occurred in the tuple.


# In[309]:


mytuple1.count('two') # Occurence of item 'two' in the tuple


# In[310]:


mytuple1.count('four') #Occurence of item 'four' in the tuple


# In[311]:


del mytuple[0] # Tuples are immutable which means we can't DELETE tuple items


# In[312]:


mytuple[0] = 1 # Tuples are immutable which means we can't CHANGE tuple items


# In[313]:


del mytuple # Deleting entire tuple object is possible


# In[316]:


mytuple


# In[317]:


'one' in mytuple # Check if 'one' exist in the list


# In[318]:


'ten' in mytuple # Check if 'ten' exist in the list


# In[319]:


if 'three' in mytuple: # Check if 'three' exist in the list
 print('Three is present in the tuple')
else:
 print('Three is not present in the tuple')


# In[320]:


if 'eleven' in mytuple: # Check if 'eleven' exist in the list
 print('eleven is present in the tuple')
else:
 print('eleven is not present in the tuple')


# In[321]:


mytuple


# In[322]:


mytuple.index('one') # Index of first element equal to 'one'


# In[323]:


mytuple.index('five') # Index of first element equal to 'five'


# In[324]:


mytuple1


# In[325]:


mytuple1.index('one') # Index of first element equal to 'one'


# In[326]:


mytuple2 = (43,67,99,12,6,90,67)


# In[327]:


sorted(mytuple2) # Returns a new sorted list and doesn't change original tuple


# In[328]:


sorted(mytuple2, reverse=True) # Sort in descending order


# In[329]:


myset = {1,2,3,4,5} # Set of numbers
myset


# In[330]:


len(myset) #Length of the set


# In[331]:


my_set = {1,1,2,2,3,4,5,5}
my_set 


# In[332]:


myset1 = {1.79,2.08,3.99,4.56,5.45} # Set of float numbers
myset1


# In[333]:


myset2 = {'Asif' , 'John' , 'Tyrion'} # Set of Strings
myset2


# In[334]:


myset3 = {10,20, "Hola", (11, 22, 32)} # Mixed datatypes
myset3


# In[335]:


myset3 = {10,20, "Hola", [11, 22, 32]} # set doesn't allow mutable items like lis
myset3


# In[336]:


myset4 = set() # Create an empty set
print(type(myset4))


# In[337]:


my_set1 = set(('one' , 'two' , 'three' , 'four'))
my_set1


# In[338]:


myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
for i in myset:
 print(i)


# In[339]:


for i in enumerate(myset):
 print(i)


# In[340]:


myset


# In[341]:


'one' in myset # Check if 'one' exist in the set


# In[342]:


'ten' in myset # Check if 'ten' exist in the set


# In[343]:


if 'three' in myset: # Check if 'three' exist in the set
 print('Three is present in the set')
else:
 print('Three is not present in the set')


# In[344]:


if 'eleven' in myset: # Check if 'eleven' exist in the list
 print('eleven is present in the set')
else:
 print('eleven is not present in the set')


# In[345]:


myset


# In[346]:


myset.add('NINE') # Add item to a set using add() method
myset


# In[347]:


myset.update(['TEN' , 'ELEVEN' , 'TWELVE']) # Add multiple item to a set using u
myset


# In[348]:


myset.remove('NINE') # remove item in a set using remove() method
myset


# In[349]:


myset.discard('TEN') # remove item from a set using discard() method
myset


# In[350]:


myset.clear() # Delete all items in a set
myset


# In[351]:


del myset # Delete the set object
myset


# In[352]:


myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
myset


# In[353]:


myset1 = myset # Create a new reference "myset1" 
myset1


# In[354]:


id(myset) , id(myset1) # The address of both myset & myset1 will be the same as


# In[355]:


my_set = myset.copy() # Create a copy of the list
my_set


# In[356]:


id(my_set) # The address of my_set will be different from myset because my_set is


# In[357]:


myset.add('nine')
myset


# In[358]:


myset1 # myset1 will be also impacted as it is pointing to the same Set


# In[359]:


myset1 # myset1 will be also impacted as it is pointing to the same Set


# In[360]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {8,9,10}


# In[361]:


A | B # Union of A and B (All elements from both sets. NO DUPLICATES)


# In[362]:


A.union(B) # Union of A and B


# In[363]:


A.union(B, C) # Union of A, B and C


# In[364]:


"""
Updates the set calling the update() method with union of A , B & C. 
For below example Set A will be updated with union of A,B & C.
"""
A.update(B,C)
A


# In[366]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}


# In[367]:


A & B # Intersection of A and B (Common items in both sets)


# In[368]:


A.intersection(B) Intersection of A and B


# In[369]:


"""
Updates the set calling the intersection_update() method with the intersection of
For below example Set A will be updated with the intersection of A & B.
"""
A.intersection_update(B)
A


# In[370]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}


# In[371]:


A - B # set of elements that are only in A but not in B


# In[372]:


A.difference(B) # Difference of sets


# In[373]:


B- A # set of elements that are only in B but not in A


# In[374]:


B.difference(A)


# In[375]:


"""
Updates the set calling the difference_update() method with the difference of set
For below example Set B will be updated with the difference of B & A.
"""
B.difference_update(A)
B


# In[3]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}


# In[4]:


A ^ B # Symmetric difference (Set of elements in A and B but not in both. 


# In[5]:


A.symmetric_difference(B) # Symmetric difference of sets


# In[6]:


"""
Updates the set calling the symmetric_difference_update() method with the symmetr
For below example Set A will be updated with the symmetric difference of A & B.
"""
A.symmetric_difference_update(B)
A


# In[7]:


A = {1,2,3,4,5,6,7,8,9}
B = {3,4,5,6,7,8}
C = {10,20,30,40}


# In[8]:


B.issubset(A) # Set B is said to be the subset of set A if all elements of B are 


# In[9]:


A.issuperset(B) # Set A is said to be the superset of set B if all elements of B


# In[10]:


C.isdisjoint(A) # Two sets are said to be disjoint sets if they have no common element


# In[11]:


B.isdisjoint(A)


# In[12]:


A


# In[13]:


sum(A)


# In[14]:


max(A)


# In[16]:


min(A)


# In[17]:


len(A)


# In[18]:


list(enumerate(A))


# In[19]:


D= sorted(A,reverse=True)
D


# In[20]:


sorted(D)


# In[21]:


mydict = dict() # empty dictionary
mydict


# In[22]:


mydict = {1:'one' , 2:'two' , 3:'three'} # dictionary with integer keys
mydict


# In[23]:


mydict = dict({1:'one' , 2:'two' , 3:'three'}) # Create dictionary using dict()
mydict


# In[24]:


mydict = {'A':'one' , 'B':'two' , 'C':'three'} # dictionary with character keys
mydict


# In[25]:


mydict = {1:'one' , 'A':'two' , 3:'three'} # dictionary with mixed keys
mydict


# In[26]:


mydict.keys() # Return Dictionary Keys using keys() method


# In[27]:


mydict.values() # Return Dictionary Values using values() method


# In[28]:


mydict.items() # Access each key-value pair within a dictionary 


# In[29]:


mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']} # dictionary with 
mydict


# In[31]:


mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria'], 'B':('Bat' , 'cat', 'hat')}
mydict


# In[32]:


mydict = {1:'one' , 2:'two' , 'A':{'Name':'asif' , 'Age' :20}, 'B':('Bat' , 'cat', 'hat')}
mydict


# In[33]:


keys = {'a' , 'b' , 'c' , 'd'}
mydict3 = dict.fromkeys(keys) # Create a dictionary from a sequence of keys
mydict3


# In[34]:


keys = {'a' , 'b' , 'c' , 'd'}
value = 10
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of k
mydict3


# In[35]:


keys = {'a' , 'b' , 'c' , 'd'}
value = [10,20,30]
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of k
mydict3


# In[36]:


value.append(40)
mydict3


# In[37]:


mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
mydict


# In[38]:


mydict[1] # Access item using key


# In[39]:


mydict.get(1) # Access item using get() method


# In[40]:


mydict1 = {'Name':'Asif' , 'ID': 74123 , 'DOB': 1991 , 'job' :'Analyst'}
mydict1


# In[41]:


mydict1['Name'] # Access item using key


# In[42]:


mydict1.get('job') # Access item using get() method


# In[43]:


mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}
mydict1


# In[44]:


mydict1['DOB'] = 1992 # Changing Dictionary Items
mydict1['Address'] = 'Delhi'
mydict1


# In[45]:


dict1 = {'DOB':1995}
mydict1.update(dict1)
mydict1


# In[46]:


mydict1['Job'] = 'Analyst' # Adding items in the dictionary
mydict1


# In[47]:


mydict1.pop('Job') # Removing items in the dictionary using Pop method
mydict1


# In[48]:


mydict1.popitem() # A random item is removed


# In[49]:


mydict1


# In[50]:


del[mydict1['ID']] # Removing item using del method
mydict1


# In[51]:


mydict1.clear() # Delete all items of the dictionary using clear method
mydict1


# In[52]:


del mydict1 # Delete the dictionary object
mydict1


# In[53]:


mydict = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}
mydict


# In[54]:


mydict1 = mydict # Create a new reference "mydict1" 


# In[55]:


id(mydict) , id(mydict1) # The address of both mydict & mydict1 will be the same 


# In[56]:


mydict2 = mydict.copy() # Create a copy of the dictionary


# In[57]:


id(mydict2) # The address of mydict2 will be different from mydict because mydict


# In[58]:


mydict['Address'] = 'Mumbai'


# In[59]:


mydict


# In[60]:


mydict1 # mydict1 will be also impacted as it is pointing to the same dictionary


# In[61]:


mydict2 # Copy of list won't be impacted due to the changes made in the original 


# In[64]:


mydict1 = {'Name': 'Asif', 'ID': 12345, 'DOB': 1991, 'Address': 'Hilsinki', 'Occupation': 'Analyst'}
mydict1


# In[65]:


for i in mydict1:
 print(i , ':' , mydict1[i]) # Key & value pair


# In[66]:


for i in mydict1:
 print(mydict1[i]) # Dictionary items


# In[67]:


mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Job': 'Analyst'}
mydict1


# In[68]:


'Name' in mydict1 # Test if a key is in a dictionary or not


# In[69]:


'Asif' in mydict1 # Membership test can be only done for keys


# In[70]:


'ID' in mydict1


# In[71]:


'Address' in mydict1


# In[72]:


mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Job': 'Analyst'}
mydict1


# In[73]:


all(mydict1) # Will Return false as one value is false (Value 0)


# In[74]:


any(mydict1) # Will Return True as we have items in the dictionary with True value


# In[75]:


mydict1[0] = 'test1'
mydict1


# In[76]:


all(mydict1) # Returns false as one value is false


# In[77]:


any(mydict1) # Will Return True as we have items in the dictionary with True value


# In[78]:


double = {i:i*2 for i in range(10)} #double each value using dict comprehension
double


# In[79]:


square = {i:i**2 for i in range(10)}
square


# In[80]:


key = ['one' , 'two' , 'three' , 'four' , 'five']
value = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(key,value)} # using dict comprehension to create d
mydict


# In[81]:


mydict1 = {'a':10 , 'b':20 , 'c':30 , 'd':40 , 'e':50}
mydict1 = {k:v/10 for (k,v) in mydict1.items()} # Divide all values in a dictiona
mydict1


# In[82]:


str1 = "Natural Language Processing"
mydict2 = {k:v for (k,v) in enumerate(str1)} # Store enumerated values in a dictinary
mydict2


# In[83]:


str1 = "abcdefghijklmnopqrstuvwxyz"
mydict3 = {i:i.upper() for i in str1} # Lower to Upper Case
mydict3


# In[88]:


mystr4 = "one two three four one two two three five five six seven six seven one one one ten eight ten nine eleven ten ten nine" 


# In[89]:


mylist = mystr4.split() # Split String into substrings
mylist


# In[90]:


mylist1 = set(mylist) # Unique values in a list
mylist1 = list (mylist1)
mylist1


# In[97]:


# Calculate frequenct of each word
count1 = [0] * len(mylist1)
mydict5 = dict()
for i in range(len(mylist1)):
    for j in range(len(mylist)):
        if mylist1[i] == mylist[j]:
            count1[i] += 1
    mydict5[mylist1[i]] = count1[i]
print(mydict5)


# In[100]:


a = 5
b = 2

x = 'Asif'
y = 'Bhat'

# Addition
c = a + b
print('Addition of {} and {} will give :- {}\n'.format(a,b,c))

#Concatenate string using plus operator
z = x+y
print ('Concatenate string \'x\' and \'y\' using \'+\' operaotr :- {}\n'.format(z,x,y))
 
# Subtraction
c = a - b
print('Subtracting {} from {} will give :- {}\n'.format(b,a,c))
 
# Multiplication
c = a * b 
print('Multiplying {} and {} will give :- {}\n'.format(a,b,c))
 
# Division
c = a / b
print('Dividing {} by {} will give :- {}\n'.format(a,b,c))
 
# Modulo of both number 
c = a % b
print('Modulo of {} , {} will give :- {}\n'.format(a,b,c))
 
# Power 
c = a ** b
print('{} raised to the power {} will give :- {}\n'.format(a,b,c))
                                                                                
# Division(floor)
c = a // b
print('Floor division of {} by {} will give :- {}\n'.format(a,b,c))


# In[101]:


x = 20
y = 30
print('Is x greater than y :- ',x>y)
print('\nIs x less than y :- ',x<y)
print('\nIs x equal to y :- ',x==y)
print('\nIs x not equal to y :- ',x!=y)
print('\nIs x greater than or equal to y :- ',x>=y)
print('\nIs x less than or equal to y :- ',x<=y)


# In[102]:


a = 'Asif'
b = 'Bhat'
c = 'Asif'
a == b , a ==c , a != b # Comparison operators on string


# In[103]:


x = True
y = False
print('Logical AND operation :- ',x and y) # True if both values are true
print('Logical OR operation :- ',x or y) # True if either of the values is true
print('NOT operation :- ',not x ) # True if operand is false


# In[104]:


x = 18 # binary form 10010
y = 6 # binary form 00110
print('Bitwise AND operation - {}'.format(x&y))
print('Bitwise OR operation - {}'.format(x|y))
print('Bitwise XOR operation - {}'.format(x^y))
print('Bitwise NOT operation - {}'.format(~x))
print('Bitwise right shift operation - {}'.format(x>>2))
print('Bitwise left shift operation - {}'.format(x<<2))


# In[107]:


x = 10
print('Initialize x with value 10 (x=10)) :- ',x)
x+=20 # x = x+20
print ('Add 20 to x :- ',x)
x-=20 # x = x-20
print ('subtract 20 from x :- ',x)
x/=10 # x = x/10
print ('Divide x by 10 :- ',x)
x*=10 # x = x/10
print ('Multiply x by 10 :- ',x)
x = int(x)
x**=2 # x = x/10
print ('x raised to the power 2 :- ',x)
x%=2
print ('Modulo Division :- ',x)
x = 20
x//=3
print ('Floor Division :- ',x)
x&=2
print('Bitwise AND :- ',x)
x|=2
print('Bitwise OR :- ',x)
x^=2
print('Bitwise XOR :- ',x)
x = 10
x<<=2
print('Bitwise left shift operation',x)
x>>=2


# In[108]:


mystr = 'Asif Ali Bhat'
'Asif' in mystr , 'John' in mystr


# In[109]:


mystr = 'Asif Ali Bhat'
'Asif' not in mystr , 'John' not in mystr


# In[110]:


def myfunc():
 print("Hello Python Lovers")
myfunc()


# In[111]:


def details(name,userid,country): # Function to print User details
 print('Name :- ', name)
 print('User ID is :- ', userid)
 print('Country :- ',country)
 
details('Asif' , 'asif123' , 'India')


# In[112]:


def square (n): #function to find square of a number
 n= n*n
 return n
square (10)


# In[134]:


def even_odd (num): #Even odd test
   """ This function will check whether a number is even or odd"""
    if num % 2 ==0:
        print (num, ' is even number')
    else:
        print (num, ' is odd number')
even_odd(3)
even_odd(4)
print(even_odd.__doc__) # Print function documentation string


# In[135]:


def even_odd(num):
    """This function will check whether a number is even or odd"""
    if num % 2 == 0:
        return '{} is even number'.format(num)
    else:
        return '{} is odd number'.format(num)

result1 = even_odd(3)
result2 = even_odd(4)

print(result1)
print(result2)

print(even_odd.__doc__)  # Print function documentation string


# In[136]:


def fullname (firstname , middlename ,lastname): #Concatenate Strings
 fullname = "{} {} {}".format(firstname,middlename,lastname)
 print (fullname)
fullname('Asif' , 'Ali' , 'Bhat')


# In[137]:


def fullname (firstname , middlename ,lastname): #Concatenate Strings
 fullname = "{} {} {}".format(firstname,middlename,lastname)
 print (fullname)
fullname(lastname = 'Bhat' , middlename='Ali' , firstname='Asif') # Keyword Argument


# In[138]:


fullname ('Asif') # This will throw error as function is expecting 3 arguments.


# In[139]:


def myfunc(city = 'Mumbai'):
 print('Most Populous City :- ', city)
 
myfunc() # When a function is called without an argument it will use default value


# In[140]:


var1 = 100 # Variable with Global scope.
def myfunc():
 print(var1) # Value 100 will be displayed due to global scope of var1
 
myfunc()
print(var1)


# In[141]:


def myfunc1():
 var2 = 10 # Variable with Local scope
 print(var2)
def myfunc2():
 print(var2) # This will throw error because var2 has a local scope. Var2 is o
myfunc1()
myfunc2()


# In[142]:


var1 = 100 # Variable with Global scope.
def myfunc():
 var1 = 99 # Local scope
 print(var1)
 
myfunc() 
print(var1) # The original value of var1 (100) will be retained due to global scope


# In[143]:


list1 = [11,22,33,44,55]
def myfunc(list1):
 list1.append(100)
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the function)
print('"List1" after calling the function:- ',list1)


# In[144]:


list1 = [11,22,33,44,55]
def myfunc(list1):
 list1 = [10,100,1000,10000] # link of 'list1' with previous object is broken 
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the function
print('"List1" after calling the function:- ',list1)


# In[145]:


def swap(a,b):
 temp = a
 a = b # link of 'a' with previous object is broken now as new object is 
 b = temp # link of 'b' with previous object is broken now as new object is 
a = 10
b = 20
swap(a,b)
a,b


# In[151]:


def factorial(num): # Calculate factorial of a number using recursive function c
    if num <=1 :
        return 1
    else:
        return num * factorial(num-1)
factorial(4)


# In[153]:


def add(num): # Sum of first n natural numbers
    if num == 0:
        return 0
    else:
        return num + add(num-1)
add(5) # Sum of first five natural numbers (1,2,3,4,5)


# In[155]:


def fiboacci(num):
    if num <= 1:
        return num
    if num == 2:
        return 1
    else: 
        return(fiboacci(num-1) + fiboacci(num-2)) 
nums = int(input("How many fibonacci numbers you want to generate -"))


for i in range(nums):
     print(fiboacci(i)) # Generate Fibonacci series


# In[156]:


def add(a,b,c):
 return a+b+c
 
print(add(10,20,30)) # Sum of two numbers


# In[161]:


print(add(1,2,3,4)) '''This will throw below error as this function will only take.
If we want to make argument list dynamic then *args wil come in picture'''


# In[163]:


def some_args(arg_1, arg_2, arg_3):
 print("arg_1:", arg_1)
 print("arg_2:", arg_2)
 print("arg_3:", arg_3)
my_list = [2, 3]
some_args(1, *my_list)


# In[168]:


def add1(*args):
    return sum(args)

print(add1(1, 2, 3))
print(add1(1, 2, 3, 4))  # *args will take a dynamic argument list.
print(add1(1, 2, 3, 4, 5))
print(add1(1, 2, 3, 4, 5, 6))
print(add1(1, 2, 3, 4, 5, 6, 7))


# In[169]:


list1 = [1,2,3,4,5,6,7]
tuple1 = (1,2,3,4,5,6,7)
add1(*list1) , add1(*tuple1) #tuple & list items will be passed as argument list


# In[170]:


list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4,5,6,7]
list3 = [1,2,3,4,5,6,7]
list4 = [1,2,3,4,5,6,7]
add1(*list1 , *list2 , *list3 , *list4 ) #All four lists are unpacked and each in


# In[171]:


def UserDetails(*args):
 print(args)
UserDetails('Asif' , 7412 , 41102 , 33 , 'India' , 'Hindi')
''' For the above example we have no idea about the parameters passed e.g 7412 , 
 In such cases we can take help of Keyworded arguments (**kwargs) '''


# In[173]:


def UserDetails(**kwargs):
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India', Language= 'Hindi') 


# In[175]:


mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India', 'Language': 'Hindi'} 
UserDetails(**mydict)


# In[177]:


def UserDetails(licenseNo, *args , phoneNo=0 , **kwargs): # Using all four argum
    print('License No :- ', licenseNo)
    j=''
    for i in args:
        j = j+i
    print('Full Name :-',j)
    print('Phone Number:- ',phoneNo)
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))
 
 
name = ['Asif' , ' ' , 'Ali' , ' ','Bhat']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India', 'Language': 'Hindi'}
UserDetails('BHT145' , *name , phoneNo=1234567890,**mydict )


# In[179]:


def UserDetails(licenseNo, *args , phoneNo=0, **kwargs): # Using all four argumen
     print('Nothing')


# In[186]:


def UserDetails(licenseNo, **kwargs , *args): # This will fail. *args MUST come before **kwargs in the argument list
    print('Nothing')


# In[183]:


#The below function will fail. Default argument/positional argument (licenseNo) M
def UserDetails(ID = 1, licenseNo, *args):
     print('Nothing')


# In[187]:


addition = lambda a : a + 10 # This lambda function adds value 10 to an argument
print(addition(5))


# In[188]:


product = lambda a, b : a * b #This lambda function takes two arguments (a,b) and
print(product(5, 6))


# In[189]:


addition = lambda a, b, c : a + b + c #This lambda function takes three argument
print(addition(5, 6, 2))


# In[190]:


res = (lambda *args: sum(args)) # This lambda function can take any number of ar
res(10,20) , res(10,20,30,40) , res(10,20,30,40,50,60,70)


# In[191]:


res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take an
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)


# In[192]:


res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take an
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)


# In[199]:


# User-defined function to find the product of numbers
def product(nums): 
    total = 1
    for i in nums:
        total *= i 
    return total

# Lambda function to take any number of arguments and return their product
res1 = lambda *args: product(args)

result1 = res1(10, 20, 30)
result2 = res1(10, 20, 30, 40, 50)

print(result1)  # This will print the product of 10, 20, and 30
print(result2)  # This will print the product of 10, 20, 30, 40, and 50


# In[200]:


def myfunc(n):
 return lambda a : a + n
add10 = myfunc(10)
add20 = myfunc(20)
add30 = myfunc(30)
print(add10(5))
print(add20(5))
print(add30(5))


# In[201]:


list1 = [1,2,3,4,5,6,7,8,9]
def odd(n):
 if n%2 ==1: return True
 else: return False
 
odd_num = list(filter(odd,list1)) # This Filter function filters list1 and passes
odd_num


# In[202]:


list1 = [1,2,3,4,5,6,7,8,9]
# The below Filter function filters "list1" and passes all odd numbers using lamb
odd_num = list(filter(lambda n: n%2 ==1 ,list1)) 
odd_num


# In[203]:


def twice(n):
 return n*2
 
doubles = list(map(twice,odd_num)) # The map function will apply user defined "tw
doubles


# In[204]:


doubles = list(map(lambda n:n*2,odd_num)) # This map function will double all ite
doubles


# In[205]:


from functools import reduce
def add(a,b):
 return a+b
 
sum_all = reduce(add,doubles) # This reduce function will perform sum of all item
sum_all


# In[209]:


#The below reduce() function will perform sum of all items in the list using lamb
sum_all = reduce(lambda a,b : a+b,doubles)
sum_all


# In[212]:


# Putting it all together
sum_all = reduce(lambda a, b: a + b,list(map(lambda n: n * 2,list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5])))))

sum_all


# In[213]:


# More examples on Map , Filter , Reduce 


# In[214]:


list1 = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n: n%2 ==0 ,list1)) # Filter even numbers from the list
odd = list(filter(lambda n: n%2 !=0 ,list1)) # Filter odd numbers from the lis
print('--------')
print(even)
print(odd)
print('--------')
list2 = ['one' , 'TWO' , 'three' , 'FOUR']
upper = list(filter(lambda x: x.isupper() , list2)) # filter uppercase strings fr
lower = list(filter(lambda x: x.islower() , list2)) # filter lowercase strings fr
print(upper)
print(lower)
print('--------')
list3 = ['one' , 'two2' , 'three3' ,'88' , '99' , '102']
numeric = list(filter(lambda x:x.isnumeric(), list3)) # filter numbers from the 
alpha = list(filter(lambda x:x.isalpha(), list3)) # filter character strings
alphanum = list(filter(lambda x:x.isalnum(), list3)) # filtr numbers & character 
print(alpha)
print(numeric)
print(alphanum)
print('--------')
#Vowel Test


# In[215]:


list1 = [1,2,3,4]
list2 = [5,6,7,8]
def double(x):
 return x+x
def add(x,y):
 return x+y
def square(x):
 return x*x
print('---------------')
print(list(map(double, list1))) # Double each number using map & User defined fun
print(list(map(add, list1, list2))) # add two items using map & User defined fun
print(list(map(square, list1))) #Square numbers using map & User defined function
print('---------------')
print(list(map(lambda x: x + x, list1))) # Double each number using map & lambda
print(list(map(lambda x, y: x + y, list1, list2))) # add two items using map & l
print(list(map(lambda x: x*x, list1))) #Square numbers using map & lambda
print('---------------')


# In[224]:


import operator
from functools import reduce
list2 = [1, 2, 3, 4]

product = reduce (operator.mul,list2) # Product of all numbers in a list

add = reduce(operator.add,list2) # Add all numbers in the list

concat_str = reduce(operator.add, ['Python', ' ', 'Rocks']) # Concatenate strings

prod = reduce(operator.mul, ['Hello ', 3]) # Repeat a string multiple times

min_num = reduce(lambda a, b: a if a < b else b, list2) # Minimum number in the list

max_num = reduce(lambda a, b: a if a > b else b, list2) # Maximum number in the list

print(product)
print(add)
print(concat_str)
print(prod)
print(min_num)
print(max_num)


# In[225]:


def min_func(a, b):
 return a if a < b else b
def max_func(a, b):
 return a if a > b else b
min_num = reduce(min_func, list2) # Minimum number in the list using reduce () & 
max_num = reduce(max_func, list2) # Maximum number in the list using reduce () & 
min_num , max_num


# In[226]:


print('------')
print(reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0])) # Returns True if all 
print(reduce(lambda a, b: bool(a and b), [2, 3, 1, 5, 6])) # Returns True if all 
print(reduce(lambda a, b: bool(a and b), [8, 9, 1, 0, 9])) # Returns True if all 
print('------')
print(reduce(lambda a, b: bool(a or b), [0, 0, 0, 0, 0])) # Returns True if any 
print(reduce(lambda a, b: bool(a or b), [2, 3, 1, 5, 6])) # Returns True if any 
print(reduce(lambda a, b: bool(a or b), [8, 9, 1, 0, 9])) # Returns True if any 
print('------')


# In[227]:


# Create a class with property "var1"
class myclass:
 var1 = 10
 
obj1 = myclass() # Create an object of class "myclass()"
print(obj1.var1)


# In[229]:


# Create an employee class
class Employee:
 def __init__(self, name, empid): # __init__() function is used to assign values
    self.name = name
    self.empid = empid
 def greet(self): # Class Method
    print("Thanks for joining ABC Company {}!!".format(self.name))
emp1 = Employee("Asif", 34163) # Create an employee object

print('Name :- ',emp1.name)
print('Employee ID :- ',emp1.empid)
emp1.greet()


# In[230]:


emp1.name = 'Basit' # Modify Object Properties
emp1.name


# In[231]:


del emp1.empid # Delete Object Properties
emp1.empid


# In[232]:


del emp1 # Delete the object
emp1


# In[233]:


emp2 = Employee("Michael", 34162) # Create an employee object
print('Name :- ',emp2.name)
print('Employee ID :- ',emp2.empid)
emp2.greet()


# In[234]:


emp2.country = 'India' #instance variable can be created manually
emp2.country


# In[244]:


class person:  # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))


class student(person):  # Child Class
    def __init__(self, name, age, gender, studentid, fees):
        person.__init__(self, name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID: {}'.format(self.studentid))
        print('Fees: {}'.format(self.fees))


class teacher(person):  # Child Class
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def TeacherInfo(self):
        print('Employee ID: {}'.format(self.empid))
        print('Salary: {}'.format(self.salary))


stud1 = student('Asif', 24, 'Male', 123, 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo()
stud1.StudentInfo()
print()

teacher1 = teacher('Basit', 36, 'Male', 456, 80000)
print('Employee Details')
print('---------------')
teacher1.PersonInfo()
teacher1.TeacherInfo()


# In[246]:


class person:  # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))


class student(person):  # Child Class
    def __init__(self, name, age, gender, studentid, fees):
        person.__init__(self, name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID: {}'.format(self.studentid))
        print('Fees: {}'.format(self.fees))


stud1 = student('Asif', 24, 'Male', 123, 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo()
stud1.StudentInfo()
print()


# In[248]:


class person:  # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))


class student(person):  # Child Class
    def __init__(self, name, age, gender, studentid, fees):
        super().__init__(name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        super().PersonInfo()
        print('Student ID: {}'.format(self.studentid))
        print('Fees: {}'.format(self.fees))


stud = student('Asif', 24, 'Male', 123, 1200)
print('Student Details')
print('---------------')
stud.StudentInfo()


# In[249]:


class person:  # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))


class employee(person):  # Child Class
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        print('Employee ID: {}'.format(self.empid))
        print('Salary: {}'.format(self.salary))


class fulltime(employee):  # Grandchild Class
    def __init__(self, name, age, gender, empid, salary, WorkExperience):
        employee.__init__(self, name, age, gender, empid, salary)
        self.WorkExperience = WorkExperience

    def FulltimeInfo(self):
        print('Work Experience: {}'.format(self.WorkExperience))


class contractual(employee):  # Grandchild Class
    def __init__(self, name, age, gender, empid, salary, ContractExpiry):
        employee.__init__(self, name, age, gender, empid, salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print('Contract Expiry: {}'.format(self.ContractExpiry))


print('Contractual Employee Details')
print('****************************')
contract1 = contractual('Basit', 36, 'Male', 456, 80000, '21-12-2021')
contract1.PersonInfo()
contract1.employeeInfo()
contract1.ContractInfo()
print('\n \n')

print('Fulltime Employee Details')
print('****************************')
fulltime1 = fulltime('Asif', 22, 'Male', 567, 70000, 12)
fulltime1.PersonInfo()
fulltime1.employeeInfo()
fulltime1.FulltimeInfo()


# In[251]:


# Super Class
class Father:
    def __init__(self):
        self.fathername = str()
 
# Super Class
class Mother:
    def __init__(self):
        self.mothername = str()
 
 
# Sub Class
class Son(Father, Mother):
    name = str()
    def show(self):
        print('My Name :- ',self.name)
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.name = 'Bill'
s1.fathername = "John"
s1.mothername = "Kristen"
s1.show()


# In[255]:


class Date:
    def __init__(self, date):
        self.date = date

class Time:
    def __init__(self, time):
        self.time = time

class Timestamp(Date, Time):
    def __init__(self, date, time):
        Date.__init__(self, date)
        Time.__init__(self, time)
        DateTime = self.date + ' ' + self.time
        print(DateTime)

datetime1 = Timestamp('2020-08-09', '23:48:55')


# In[256]:


class person: # Parent Class
 def __init__(self, name , age , gender):
 self.name = name
 self.age = age
 self.gender = gender
 
 def greet(self):
 print("Hello Person")
 
 
 
class student(person): # Child Class
 def __init__(self,name,age,gender,studentid,fees):
 person.__init__(self,name,age,gender)
 self.studentid = studentid
 self.fees = fees
 def greet(self):
 print("Hello Student")
 
 
stud = student('Gabriel' , 56 , 'Male' , 45 , 345678)
stud.greet() # greet() method defined in subclass will be triggered as "stud" is 
person1 = person('Gabriel' , 56 , 'Male')
person1.greet() # greet() method defined in superclass will be triggered becau


# In[257]:


class Date:
    def __init__(self, date):
        self.date = date

class Time:
    def __init__(self, time):
        self.time = time

class Timestamp(Date, Time):
    def __init__(self, date, time):
        Date.__init__(self, date)
        Time.__init__(self, time)
        DateTime = self.date + ' ' + self.time
        print(DateTime)

datetime1 = Timestamp('2020-08-09', '23:48:55')


# In[258]:


class person:  # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print("Hello Person")


class student(person):  # Child Class
    def __init__(self, name, age, gender, studentid, fees):
        person.__init__(self, name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def greet(self):
        print("Hello Student")


stud = student('Gabriel', 56, 'Male', 45, 345678)
stud.greet()  # greet() method defined in subclass will be triggered as "stud" is an instance of the student class

person1 = person('Gabriel', 56, 'Male')
person1.greet()  # greet() method defined in superclass will be triggered because "person1" is an instance of the person class


# In[259]:


list1 = ['asif' , 'john' , 'Michael' , 'Basit']
'asif' in list1 # Membership check using 'in' operator


# In[260]:


list1 = ['asif' , 'john' , 'Michael' , 'Basit']
'asif' in list1 # Membership check using 'in' operator


# In[261]:


assert 'john' in list1 # If the condition returns true the program does nothing


# In[262]:


assert 'john' in list1 # If the condition returns true the program does nothing


# In[263]:


mydict = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}
mydict


# In[264]:


'Asif' in mydict # Dictionary membership will always check the keys


# In[265]:


'Name' in mydict # Dictionary membership will always check the keys


# In[266]:


'DOB' in mydict


# In[267]:


mystr = 'asifbhat'
'as' in mystr # Check if substring is present


# In[268]:


mylist = ['Asif' , 'Basit' , 'John' , 'Michael']
list_iter = iter(mylist) # Create an iterator object using iter()
print(next(list_iter)) # return first element in the iterator stream
print(next(list_iter)) # return next element in the iterator stream
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))


# In[269]:


mylist = ['Asif' , 'Basit' , 'John' , 'Michael']
list_iter = iter(mylist) # Create an iterator object using iter()
print(list_iter.__next__()) # return first element in the iterator stream
print(list_iter.__next__()) # return next element in the iterator stream
print(list_iter.__next__())
print(list_iter.__next__())


# In[270]:


mylist = ['Asif' , 'Basit' , 'John' , 'Michael']
list_iter = iter(mylist) # Create an iterator object using iter()
for i in list_iter:
 print(i)


# In[271]:


# Looping Through an Iterable (list) using for loop
mylist = ['Asif' , 'Basit' , 'John' , 'Michael']
for i in mylist:
 print(i)


# In[272]:


# Looping Through an Iterable (tuple) using for loop
mytuple = ('Asif' , 'Basit' , 'John' , 'Michael')
for i in mytuple:
 print(i)


# In[273]:


# Looping Through an Iterable (string) using for loop
mystr = "Hello Python"
for i in mystr:
 print(i)


# In[276]:


class myiter:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

# Creating an instance of the iterator
mynum = myiter()

# Obtaining an iterator object
iter1 = iter(mynum)

# Iterating over the values and printing them
for i in iter1:
    print(i)


# In[277]:


class myiter:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 20:
            val = self.num
            self.num += 2
            return val
        else:
            raise StopIteration

# Creating an instance of the iterator
myodd = myiter()

# Obtaining an iterator object
iter1 = iter(myodd)

# Iterating over the values and printing them
for i in iter1:
    print(i)


# In[278]:


class myfibonacci:
    def __init__(self):
        self.prev = 0
        self.cur = 0

    def __iter__(self):
        self.prev = 0
        self.cur = 1
        return self

    def __next__(self):
        if self.cur <= 50:
            val = self.cur
            self.cur += self.prev
            self.prev = val
            return val
        else:
            raise StopIteration

# Creating an instance of the iterator
myfibo = myfibonacci()

# Obtaining an iterator object
iter1 = iter(myfibo)

# Iterating over the values and printing them
for i in iter1:
    print(i)


# In[280]:


def mygen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n
    n += 1
    yield n
    n += 1
    yield n

mygen1 = mygen()
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))  # Function will terminate here as all 5 values have been returned
# print(next(mygen1))  # Uncommenting this line would raise StopIteration

def mygen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n
    n += 1
    yield n
    n += 1
    yield n

mygen1 = mygen()
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))  # Function will terminate here as all 5 values have been returned
# print(next(mygen1))  # Uncommenting this line would raise StopIteration



# In[284]:


# Simple generator function that will generate natural numbers from 1 to 20.
def mygen():
    for i in range(1, 21):
        yield i

# Creating an instance of the generator
mygen1 = mygen()

# Iterating over the values and printing them
for i in mygen1:
    print(i)


# In[285]:


num = list(mygen()) # Store all values generated by generator function in a list
num


# In[289]:


# Simple generator function that will generate even numbers from 1 to 20.
def mygen():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i

# Creating an instance of the generator
mygen1 = mygen()

# Iterating over the values and printing them
for i in mygen1:
    print(i)



# In[290]:


# This Generator function will generate ten numbers of Fibonacci series.
def myfibo():
    num1, num2 = 0, 1
    count = 0
    while count < 10:
        yield num1
        num1, num2 = num2, num1 + num2
        count += 1

# Creating an instance of the generator
fibo = myfibo()

# Iterating over the values and printing them
for i in fibo:
    print(i)


# In[291]:


list1 = list(myfibo()) # Store the fibonacci series in a list
list1


# In[292]:


list2 = [i**2 for i in range(10)] # List comprehension
list2


# In[293]:


gen2 = (i**2 for i in range(10)) # Generator expression
gen2


# In[294]:


print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


# In[295]:


gen2 = (i for i in range(40) if i%2 == 0) # Generator expression to generate even
gen2
for i in gen2:
 print(i)


# In[296]:


def subtract(num1 , num2):
 res = num1 - num2
 print('Result is :- ', res)
 
subtract(4,2)
subtract(2,4)


# In[298]:


def sub_decorator(func):
    def wrapper(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return func(num1, num2)
    return wrapper

@sub_decorator
def subtract(num1, num2):
    return num1 - num2

result = subtract(2, 4)
print(result)


# In[299]:


def accept_terms(func):
    def wrapper():
        print("Please accept terms & conditions")
        func()
    return wrapper

@accept_terms
def InstallLinux():
    print('Linux installation has started\n')

@accept_terms
def InstallWindows():
    print('Windows installation has started\n')

@accept_terms
def InstallMac():
    print('Mac installation has started\n')

InstallLinux()
InstallWindows()
InstallMac()


# In[303]:


def InstallDecorator1(func):
    def wrapper():
        print('Please accept terms & conditions...\n')
        func()
    return wrapper

def InstallDecorator2(func):
    def wrapper():
        print('Please enter correct license key...\n')
        return func()
    return wrapper

def InstallDecorator3(func):
    def wrapper():
        print('Please enter partitioning choice...\n')
        return func()
    return wrapper

@InstallDecorator1
@InstallDecorator2
@InstallDecorator3
def InstallLinux():
    print('Linux installation has started \n')

InstallLinux()


# In[36]:


fileobj = open('test1.txt') # Open file in read/text mode


# In[37]:


fileobj = open('test1.txt', 'r') # Open file in read mode


# In[38]:


fileobj = open('test1.txt', 'w') # Open file in write mode


# In[39]:


fileobj = open('test1.txt', 'a') # Open file in append mode


# In[31]:


fileobj.close()


# In[40]:


# Reopen the file for reading
fileobj = open('test1.txt')


# In[41]:


# Read the whole file
content = fileobj.read()
print(content)


# In[42]:


fileobj.read() #Read whole file


# In[43]:


fileobj.seek(0) # Bring file cursor to initial position.
fileobj.read() 


# In[25]:


fileobj.seek(0)
fileobj.read(16) # Return the first 16 characters of the file


# In[44]:


fileobj.seek(0)
print(fileobj.readline()) # Read first line of a file.
print(fileobj.readline()) # Read second line of a file.
print(fileobj.readline()) # Read third line of a file.


# In[45]:


fileobj.seek(0)
fileobj.readlines() # Read all lines of a file. 


# In[49]:


# Read first 5 lines of a file using readline()
fileobj.seek(0)

count = 0
for i in range(5):
    if (count < 5):
        print(fileobj.readline())
    else:
        break
    count+=1


# In[51]:


# Read first 5 lines of a file using readlines()
fileobj.seek(0)
count = 0
for i in fileobj.readlines():
    if (count < 5):
        print(i)
    else:
        break
    count+=1


# In[52]:


fileobj = open('test1.txt', 'a')
fileobj.write('THIS IS THE NEW CONTENT APPENDED IN THE FILE') # Append content to
fileobj.close()
fileobj = open('test1.txt')
fileobj.read()


# In[54]:


fileobj = open("test1.txt", "w")

fileobj.write("NEW CONTENT ADDED IN THE FILE. PREVIOUS CONTENT HAS BEEN OVERWRITTE")
fileobj.close()
fileobj = open('test1.txt')
fileobj.read()


# In[55]:


fileobj = open("test2.txt", "w") # Create a new file
fileobj.write("First Line\n") 
fileobj.write("Second Line\n")
fileobj.write("Third Line\n") 
fileobj.write("Fourth Line\n")
fileobj.write("Fifth Line\n")
fileobj.close()
fileobj = open('test2.txt')
fileobj.readlines()


# In[63]:


os.remove("test3.txt") # Delete file


# In[64]:


os.remove("test3.txt")


# In[65]:


os.rmdir('folder1/') # Delete folder


# In[66]:


os.rmdir('folder1/')


# In[67]:


os.rmdir('folder1/')


# In[70]:


import sys
try:
    print(100/0)  # ZeroDivisionError will be encountered here. So the control will move to the except block.
except ZeroDivisionError:
    print(sys.exc_info()[1], 'Exception occurred')  # This statement will be executed with information about the exception.
else:
    print('No exception occurred')  # This will be skipped as the code block inside the try block raised an exception.
finally:
    print('Run this block of code always')  # This will be always executed regardless of whether an exception occurred or not.


# In[71]:


try:
 print(x) # NameError exception will be encountered as variable x is not defi
except:
 print('Variable x is not defined')


# In[72]:


try:
 print(x) # NameError exception will be encountered as variable x is not defi
except:
 print('Variable x is not defined')


# In[73]:


try:
 os.remove("test3.txt") # FileNotFoundError will be encountered as "test3.txt"
 
except: # Below statement will be executed as exception occur
 print("BELOW EXCEPTION OCCURED") 
 print(sys.exc_info()[1])
 
else:
 print('\nNo exception occurred')
finally:
 print('\nRun this block of code always')


# In[74]:


# Handling specific exceptions
try:
 x = int(input('Enter first number :- '))
 y = int(input('Enter first number :- ')) # If input entered is non-zero the
 print(x/y)
 os.remove("test3.txt")
except NameError:
 print('NameError exception occurred')
except FileNotFoundError:
 print('FileNotFoundError exception occurred')
 
except ZeroDivisionError:
 print('ZeroDivisionError exception occurred') 


# In[75]:


# Handling specific exceptions
try:
 x = int(input('Enter first number :- '))
 y = int(input('Enter first number :- ')) # If the input entered is zero the 
 print(x/y)
 os.remove("test3.txt")
except NameError:
 print('NameError exception occurred')
except FileNotFoundError:
 print('FileNotFoundError exception occurred')
 
except ZeroDivisionError:
 print('ZeroDivisionError exception occurred') 


# In[77]:


try:
 x = int(input('Enter first number :- '))
 if x > 50:
        raise ValueError(x) # If value of x is greater than 50 ValueError excepti
except:
    print(sys.exc_info()[0])


# In[78]:


# OverflowError - This exception is raised when the result of a numeric calculati
try: 
 import math
 print(math.exp(1000))
except OverflowError: 
 print (sys.exc_info())
else: 
 print ("Success, no error!")


# In[79]:


# ZeroDivisionError - This exception is raised when the second operator in a divi
try:
 x = int(input('Enter first number :- '))
 y = int(input('Enter first number :- '))
 print(x/y)
 
except ZeroDivisionError:
 print('ZeroDivisionError exception occurred')


# In[80]:


# NameError - This exception is raised when a variable does not exist
try:
 print(x1)
except NameError:
 print('NameError exception occurred')


# In[81]:


# AssertionError - This exception is raised when an assert statement fails
try: 
 a = 50
 b = "Asif"
 assert a == b
except AssertionError: 
 print ("Assertion Exception Raised.")


# In[82]:


# ModuleNotFoundError - This exception is raised when an imported module does not
try:
 import MyModule
except ModuleNotFoundError: 
 print ("ModuleNotFoundError Exception Raised.")


# In[83]:


# KeyError - This exception is raised when key does not exist in a dictionary
try:
 mydict = {1:'Asif', 2:'Basit', 3:'Michael'}
 print (mydict[4])
except KeyError:
 print ("KeyError Exception Raised.")


# In[84]:


# IndexError - This exception is raised when an index of a sequence does not exis
try:
 mylist = [1,2,3,4,5,6]
 print (mylist[10])
except IndexError:
 print ("IndexError Exception Raised.")


# In[85]:


# TypeError - This exception is raised when two different datatypes are combined
try: 
 a = 50
 b = "Asif"
 c = a/b
except TypeError: 
 print ("TypeError Exception Raised.")


# In[86]:


# AttributeError: - This exception is raised when attribute reference or assignme
try: 
 a = 10
 b = a.upper()
 print(b)
except AttributeError: 
 print ("AttributeError Exception Raised.")


# In[87]:


try:
 x = input('Enter first number :- ')
 
except:
 print('ZeroDivisionError exception occurred')


# In[ ]:




