#Q1Write a python script to remove the last digit from a given number. (for example, if
           # user enters 2534 then your output should be 253)

a=int(input("Enter Number"))
x=a//10
print(x)



#Q2 Write a python script to get the last digit from a given number. (for example, if user
        #enters 2089 then your output should be 9)

a=int(input("Enter Number"))
x=a%10
print(x)



#Q3 Write a python script to swap data of two variables

a,b=int(input("")),int(input(""))
x,z=b,a
print(x,z)


#Q4 Write a python script to find x power y, where values of x and y are given by user

print("Enter Two Number ")
x,y=int(input("")),int(input(""))
power=x**y
print("{} power of {} is".format(x,y),power)



#Q5 Write a python script which takes a three digit number from the user and displays
   #only its first digit.

x=int(input("Enter Three digit number: "))
a=x//100
print(a)



#Q6Write a python script which takes a three digit number from the user and displays
   #only its middle digit.

x=int(input("Enter Three digit number: "))
a=x//10
b=a%10
print(b)


#Q7 Write a python script which takes a three digit number from the user and displays
    #only its last digit.

x=int(input("Enter Three digit number: "))
b=x%10
print(b)


#Q8 Write a python script to use IN operator to display the data present in the list
a='madhav'
print('m' in a)


#Q9 Write a python script to use NOT IN operator to display the data not present in list

a='abhishek'
print('m' not in a)


#Q10 Write a python script to use IS operator to display if both variables are the same object or not?

a=345
b=567
print(a is b)















