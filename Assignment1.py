
# coding: utf-8

# In[19]:


#Task 1
str1= "Twinkle, twinkle, little star,"
str2="\tHow I wonder what you are!"
print(str1)
print(str2)
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print(str1)
print(str2)


# In[13]:


#Task 2
import sys
print(sys.version)


# In[12]:


#Task 3
import datetime
curr_dtime = datetime.datetime.now()
print("Current Date: ")
print(curr_dtime.strftime("%d-%m-%Y "))
print("Current Time: ")
print(curr_dtime.strftime("%H:%M:%S "))


# In[35]:


#Task 4
print("Enter radius of the circle to calculate its area:")
radius = int(input())
pi = 3.142
area = 2*radius*pi
print("Area of the circle is :")
print(area)


# In[40]:


#Task 5
print("Enter your first name:")
fname=input()

print("Enter your last name:")
lname=input()
print(lname," ",fname)


# In[42]:


#Task 6
print("Enter any number:")
num1 = int(input())
print("Enter again any number:")
num2 = int(input())
print("Total sum is:",num1+num2)
print(num1+num2)

