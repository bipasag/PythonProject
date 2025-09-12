
'''# Ask the user for a number

number = float(input("Enter a number: "))

# Check whether it's negative, positive, or zero
if number < 0:
    print("negative")
elif number > 0:
    print("positive")
elif number == 0:
    print("zero")
elif number >= 1000:
        print("very large integer")
else number <= -1000:
        print("very small integer")'''
from importlib.metadata import FreezableDefaultDict

'''
number = int(input("Enter an integer: "))

# Check only for very large or very small
if number >= 1000:
    print("very large integer")
elif number <= -1000:
    print("very small integer")'''
'''
# Ask the user for a number
number = int(input("Enter an integer: "))

# Check the conditions
if number >= 1000:
    print("very large integer")
elif number <= -1000:
    print("very small integer")
else:
    print("normal integer")'''

'''if -1000 < number > 0:
    print('negative')'''

'''# Ask the user for a number
number = int(input("Enter an integer: "))'''

'''# Check all conditions
if number >= 1000:
    print("very large integer")
elif number <= -1000:
    print("very small integer")
elif number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")'''

'''# Ask the user for the hour (24-hour format)
hour = int(input("Enter the hour (0-23): "))

# Check the time ranges
if hour >= 5 and hour <= 11:
    print("Good morning")
elif hour >= 12 and hour <= 17:
    print("Good afternoon")
elif hour >= 18 and hour <= 21:
    print("Good evening")
elif (hour >= 22 and hour <= 23) or (hour >= 0 and hour <= 4):
    print("Good night")'''

'''# Ask the user for the hour (24-hour format)
hour = int(input("Enter the hour (0-23): "))

# Check the time ranges
if hour >= 5 and hour <= 11:
    print("Good morning")
elif hour >= 12 and hour <= 17:
    print("Good afternoon")
elif hour >= 18 and hour <= 21:
    print("Good evening")
elif (hour >= 22 and hour <= 23) or (hour >= 0 and hour <= 4):
    print("Good night")'''

'''age = int(input("Enter your age: "))
if age>=65:
    print("You are retired.")
elif age>=18:
    print("You are working-age.")
elif age>=7:
    print("You are in school.")
else:
    print("You are a small child.")'''

'''# Ask for the person's age
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket price: Free")
elif age >= 5 and age <= 17:
    print("Ticket price: $7")
elif age >= 18 and age <= 59:
    print("Ticket price: $12")
elif age >= 60:
    print("Ticket price: $8")'''

'''i = 1
numbers = []

while i <= 10:
    numbers.append(i)
    i += 1

print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

'''
i = 1
numbers = ""

while i <= 10:
    numbers += str(i) + " "
    i += 1

print(numbers)'''

'''#from 1 to to
counter=1
while counter <=10:
    print (counter)
counter =counter+1
'''

'''number = int(input("Enter a starting number: "))

print("Countdown starting...")


while number >= 0:
    print(number)
    number -= 1

print("Kaboom!")
'''


'''number = int(input("Enter a starting number: "))

print("Countdown starting")

while number >= 0:
    if number % 2 == 0:
        print(number)
    number -= 1

print("Counter is decreasing")'''


'''
password = "james"

user_password = input("What's the password? ")

while user_password != password:
    user_password = input("Wrong password, try again: ")

print("Access granted!")'''

'''secretrum = 3
while secretrum ==7:
    secretrum = input("Enter number:")
print("Execution Stopped")
'''


'''password = "bond"

user_password = input("Enter the password: ")

while user_password != password:
    user_password = input("Wrong password, try again: ")

print("Access granted!")'''


'''names = ['Alice', 'Bob', 'Carmen', 'David', 'Eve', 'Fred' , 'Gorge', 'Harry']
print(names[-3:-7:-1])
'''

#range(start, stop, step) works with for loop
'''for number in range(1,10,1):
    print (number)'''

'''for number in range(1,20):
    print (number)'''

'''for number in range (100,-2,-2):
    print (number)'''

'''
list=[1,4,6, 'Alice', [5,9,-10,19],1.2, True]
print(list[4][2],list[5], list[2])'''


'''names = ['Alice', 'Bob', 'Carmen', 'David', 'Eve', 'Fred' , 'Gorge', 'Harry', 'Alice']

names.append('John')
names.remove('Alice')
names.insert('2','John')
print(names)

ind = names.index('Bob')
print(ind)'''

'''numbers = [4, 1, -5, 9, -1, 12, -3]
ascending = sorted(numbers)
print (ascending)

numbers=[4, 1, -5, 9, -1, 12, -3]
descending = sorted(numbers, reverse= True)
print (descending)'''

'''lists=[1, 2, 3, 4, 5]

for item in lists:
    print(item)
'''

'''list = []

for i in range(1, 6):
    list.append(i)
    print("Insert list:",list)'''

'''list = []

for number in numbers:
    list.append(2*number)
    print(list)'''

'''numbers = [1, 2, 4, 5, -10, 7, 10, 15, 18]

if 7 in numbers:
    print("Number 7 exists in the list.")
else:
    print("Number 7 does not exist in the list.")'''

'''numbers = [35, 8, 95, 22, 18, 62, 9, 14, 29]
even_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print("Even numbers:", even_numbers)'''

'''numbers = [1, 3, 5, 7, 9]
squares = []

for n in numbers:
    squares.append(n**2)

print("Squares:", squares)
'''

'''for item in range(6, 0, -1):
    print("Hello!")'''
'''obj = range(5)
print(obj)
'''
'''tup = (1,2,3,5,8,9,15)
print(tup[0::2])'''

'''mytup = (1,2,3,4)
mytup = (1,2,3,4)

mytup=(1,2,3,4,5)
mylist.append(5)'''


'''mylists = [4, 5, 6, 5, 6, 1, 3, 8, 9, 3, 6, 7]
numsix = mylists.count(6)
print("Number 6 appears", numsix, "times.")'''

'''mylists = [4, 5, 6, 5, 6, 1, 3, 8, 9, 3, 6, 7]

count_six = 0
for num in mylists:
    if num == 6:
        count_six += 1

print("Number 6 appears", count_six, "times.")'''

'''mytuple = ('a', 'b', 'c', 'd')
print("Number of elements in the tuple:", len(mytuple))
'''

'''a = (1, 2, 3)
b = (4, 5, 6)

result = tuple(a[i] + b[i] for i in range(len(a)))
print(result)
'''

'''a = (1, 2, 3)
b = (4, 5, 6)

result = ()

for item in range(len(a)):
    result += (a[item] + b[item],)

print(result)
'''

'''a = (1,2,3)
b = (4,5,6)
res = []
for i in range(len(a)):
    res.append(a[i] + b[i])

res = tuple(res)
print(res)'''

mylists = [3, 5, 6, 8, 3, 1, 9, 3, 5, 6]
myset = set(mylists)
print(myset)
'''newlist = []

for item in mylists:
    if item not in newlist:
        newlist.append(item)

print("List without duplicates:", newlist)
'''