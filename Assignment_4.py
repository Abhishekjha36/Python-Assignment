#Q1 Write a python script to take your name as input from the user and then print it.

Name=input("Enter Name ")
print(Name)


#Q2 Write a python script to take input from the user. Input must be a number.

Number=int(input("Enter Some Number "))
print(Number)


#Q3 Write a python script which takes two numbers from the user, then calculate their sum and display the result.

print("Enter Two NUmber")
a,b=int(input("")),int(input(""))
sum=a+b
print('sum is' )


#Q4 Write a python script which takes the radius from the user and display area of a circle.

print("Enter Radius of circle")
radius=int(input(""))
area=3.14*radius**2
print('Area of a circle ',area)


#Q5 Write a python script to calculate the square of a number. Number is entered by the user.

print('Enter Number ')
Num=int(input(""))
Square=Num**2
print('Square is ',Square)


#Q6 Write a python script to calculate the area of Triangle. Number is entered by the user.

print("Enter Triangle Base and Height")
b,h=int(input("")),int(input(""))
Area=(b*h)/2
print("Area of triangle ",Area)


#Q7 Write a python script to calculate average of three numbers, entered by the user

print("Enter Three Number ")
a,b,c=int(input("")),int(input("")),int(input(""))
Average=(a+b+c)/3
print('Average is ',Average)


#Q8 Write a python script to calculate simple interest

p=int(input("Enter Principal Amount: "))
r=int(input("Enter Annual intrest rate(%): "))
t=int(input("Enter time in year: "))

SI=(p*r*t)/100
total=SI+p
print('Simple intrest: ',SI)
print('Total Amount: ',total)


#Q9 Write a python script to calculate the volume of a cuboid.

l=int(input("Enter Length: "))
w=int(input("Enter Width: "))
h=int(input("Enter Hight: "))

volume=l*w*h
print("Volume of Cuboid:",volume)

#Q10 Write a python script to calculate area of a rectangle

l=int(input("Enter Length: "))
w=int(input("Enter Width: "))

area=l*w
print("Area of Rectangle: ",area)










