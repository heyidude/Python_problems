
#1. Write a Python program to implement a generator that generates random numbers within a given range
import random

for i in range(1, 10):
	x = random.randrange(9)
	print(x)

#2. Write a Python program that creates a generator that generates all prime factors of a given number
def abc(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_factors_generator(n):
    if n <= 1:
        return
    while n % 2 == 0:
        yield 2
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0 and abc(i):
            yield i
            n //= i
    if n > 2 and abc(n):
        yield n
num = int(input("Enter a number: "))
print(f"Prime factors of {num} is:")
for prime_factor in prime_factors_generator(num):
    print(prime_factor)

#.3 Write a Python program to create a generator that generates all possible permutations of a string.
from itertools import permutations

def generate(input):
    strings = permutations(input)
    for x in strings:
        yield ''.join(x)
input = input("Enter a string: ")
for string in generate(input):
    print(string)

#4. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
def process_string(input_str):
    uppercase_str = ''.join(map(str.upper, input_str))
    lowercase_str = ''.join(map(str.lower, input_str))
    return uppercase_str, lowercase_str

sequence = input("Enter a sequence : ")
uppercase, lowercase= process_string(sequence)

OUTPUT=( set(uppercase)),(set(lowercase))
print(OUTPUT)

#5.Write a Python program to find the ratio of positive numbers, negative numbers and zeroes in an array of integers. (using map)
def calculate_ratios(arr):
    total_count = len(arr)
    positive_count = sum(map(lambda x: x > 0, arr))
    negative_count = sum(map(lambda x: x < 0, arr))
    zero_count = sum(map(lambda x: x == 0, arr))
    positive_ratio = positive_count / total_count
    negative_ratio = negative_count / total_count
    zero_ratio = zero_count / total_count
    return positive_ratio, negative_ratio, zero_ratio
input_string = input("Enter a list of integers: ")
input_list = list(map(int, input_string.split()))
positive_ratio, negative_ratio, zero_ratio = calculate_ratios(input_list)
print("Ratio of positive numbers:", positive_ratio)
print("Ratio of negative numbers:", negative_ratio)
print("Ratio of zeroes:", zero_ratio)

#6. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.
def output(arr):
    return sum(arr)
input_number= input("Enter a list of integers separated by spaces: ")
i = list(map(int, input_number.split()))
result = output(i)
print("Sum =:", result)

#7.Write a Python program that matches a string that has an a followed by zero or more b's. (regex)
import re

pattern = r'a*b*'
input_string = input("Enter a string: ")
if re.match(pattern, input_string):
    print("Match found!")
else:
    print("No match found.")

#8. Write a Python program to find sequences of lowercase letters joined by an underscore.(regex)
import re
pattern = r'[a-z]+_[a-z]+'
input_string = input("Enter a string: ")
matches = re.findall(pattern, input_string)
if matches:
    print("Matched sequences:")
    for match in matches:
        print(match)
else:
    print("No matching sequences found.")
