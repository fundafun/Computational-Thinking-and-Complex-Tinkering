'''
Computational Thinking + Complex Tinkering

Coding Exercise #3: 
Prompt the user to enter 2 integer values.  Using a boolean variable, return True if one of the integers was 10 or the sum of the integers is 10. 

Example: 
9, 10 --> True
8, 2  --> True
4, 7  --> False
'''

number1 = input("pick one number")
number2 = input("pick another number")

if number1 or number2 == 10:
    print("true")
if number1 + number2 ==10:
    print("true")



dog_age = int(input("Input a dog's age in human years: "))

if dog_age < 0:
    print("Age must be a positive number.")
    exit()

human_age = dog_age * 7

print("The dog's age in human years is", human_age) 

'''
Prompt the user to enter an integer, n. Return the absolute difference
between n and the number 21.  BUT, if n is larger than 21, return double the absolute differnce. 

Example:
n = 12 --> 9
n = 21 --> 0
n = 30 --> 18    (9 * 2)
'''

n = input("Pick a number")

if n<0:
    n = n * -1

absolute_difference = n - 21

if n>21:
    print (absolute_difference * 2)

# Exercise 1: Create variables to store your name, age, and names/ages of members in your family

first_name= ("aryaa")
last_name = ("mutha")
age = 16 
location = ("westwood, ma")
family_members = ["punam", "rahul", "arushi", "pramila", "ashok", "jyostna"]


# Exercise 2: Print today's date
print("july 3 2024")

# Exercise 3: Using the age variable created above, make a loop to print numbers 0 to your age
for i in age:
    print(i)


# Exercise 3.1: Make a loop that prints numbers from 0 to your age
for i in range(age + 1):
    print(i)


# Exercise 4: Create a variable to hold the current temperature.  Print a statement based on the following conditions: 
# - Temps above 80F, print "It is hot today"
# - Temps above 55F, print "The weather is mild"
# - All other temps, print "It is cold today"

temp = input("What is the temperature today?")
if temp > 80:
    print("It is hot outside")
if temp > 55:
    print("The weather is mild")
else:
    print ("It is cold today")


# Exercise 5: (Challenge) Ask the user for basic information such as first name, last name, age, if they own a car (boolean) and their height as a decimal.  Store these values in one list and then print the values, from the list directly, in the following format: 
# Name: 
# Age: 
# Owns a car: 
# Height:

name = input("what is your full name?")
age = int(input("how old are you?"))
car = input("do you own a car?")
height = input("how tall are you?")
total = (name   , age   , car   , height   )
