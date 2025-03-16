# Task 5 - Lambda function
#
# 1. Created a dictionary with a set of names and their age, used lambda filter
# to filter out people below 18 years and printed the list of people above 18 in a list

dictionary = [
    {"Name": "Diana", "Age": 25},
    {"Name": "Alice", "Age": 10},
    {"Name": "Dora", "Age": 15},
    {"Name": "Cindrella", "Age": 30}
]

filtered_people = list(map(lambda p: p if p["Age"] > 18 else None, dictionary))
filtered_people = [p for p in filtered_people if p is not None]

print(f"People above 18 years:",(filtered_people))


# 2. Using Reduce and Lambda function to find the product of all numbers in a list

from functools import reduce

a = [5, 2, 3, 10]
b = reduce(lambda x, y: x * y, a)
print(b)


# 3. Lambda function to check if even numbers from a list and square the even numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the list:")
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
doubled = list(map(lambda x: x*2, even_nums))
print("\nSquare of the even numbers from the list:")
print(doubled)


# 4. Lambda function to check if given string is a number

is_num = lambda q: q.replace('.', '', 1).isdigit()

print(is_num('26587'))
print(is_num('green'))


# 5. Lambda function to extract year, month and day from datetime object
import datetime

now = datetime.datetime.now()
print(now)

# Define a lambda function to extract 'year', 'month' and 'day' from a given datetime object 'x'
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day

# Print the year, month and day extracted from the current datetime object 'now'
print(f"Year:",year(now))
print(f"Month:", month(now))
print(f"Day:",day(now))

# 6. Lambda function to generate a Fibonacci series upto 12 terms

def fibonacci(count):
   listFBS = [0, 1]

   any(map(lambda _:listFBS.append(sum(listFBS[-2:])),
         range(2, count)))

   return listFBS[:count]

print(fibonacci(12))

