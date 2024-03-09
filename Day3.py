import math
import random

# 1. Check if a given number is a multiple of 5
def is_multiple_of_5(number):
    return number % 5 == 0

# 2. Determine if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 3. Find the maximum of three numbers
def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

# 4. Calculate the area of a rectangle using user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)

# 5. Check if a character entered by the user is a vowel or consonant
char = input("Enter a character: ")
if char.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 6. Calculate the factorial of a number using a loop
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# 7. Find the sum of all even numbers from 1 to 100
sum_even = sum(range(2, 101, 2))
print("Sum of even numbers from 1 to 100:", sum_even)

# 8. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 9. Check if a given string is a palindrome
def is_palindrome(input_str):
    return input_str == input_str[::-1]

# 10. Find the roots of a quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Root:", root)
else:
    print("Complex roots")

# 11. Generate a random number and have the user guess it
random_number = random.randint(1, 10)
user_guess = int(input("Guess the number between 1 and 10: "))
if user_guess == random_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, the correct number was:", random_number)

# 12. Calculate the area of a circle using the math library
radius_circle = float(input("Enter the radius of the circle: "))
area_circle = math.pi * (radius_circle**2)
print("Area of the circle:", area_circle)

# 13. Print the first 10 Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers[:n]

print("First 10 Fibonacci numbers:", generate_fibonacci(10))

# 14. Find the smallest element in a list
numbers_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
smallest_element = min(numbers_list)
print("Smallest element in the list:", smallest_element)

# 15. Check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# 16. Calculate the sum of digits in a given number
number_to_sum = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(number_to_sum))
print("Sum of digits:", sum_digits)

# 17. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)

# 18. Convert a decimal number to binary
decimal_number = int(input("Enter a decimal number: "))
binary_representation = bin(decimal_number)[2:]
print("Binary representation:", binary_representation)

# 19. Reverse a given string
input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)

import math
import random

# 20. Find the average of a list of numbers
numbers_list_avg = [float(x) for x in input("Enter a list of numbers separated by space: ").split()]
average = sum(numbers_list_avg) / len(numbers_list_avg)
print("Average of the numbers:", average)

# 21. Calculate compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate per period: "))
time = float(input("Enter the number of periods: "))
compound_interest = principal * (1 + rate)**time - principal
print("Compound Interest:", compound_interest)

# 22. Implement a simple calculator
num1_calc = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2_calc = float(input("Enter the second number: "))
if operator == '+':
    result_calc = num1_calc + num2_calc
elif operator == '-':
    result_calc = num1_calc - num2_calc
elif operator == '*':
    result_calc = num1_calc * num2_calc
elif operator == '/':
    result_calc = num1_calc / num2_calc
else:
    result_calc = "Invalid operator"
print("Result:", result_calc)

# 23. Generate the multiplication table for a given number
number_for_table = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number_for_table} x {i} = {number_for_table * i}")

# 24. Find the GCD of two numbers
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

num1_gcd = int(input("Enter the first number: "))
num2_gcd = int(input("Enter the second number: "))
gcd = find_gcd(num1_gcd, num2_gcd)
print("GCD of", num1_gcd, "and", num2_gcd, "is", gcd)

# 25. Check if a matrix is symmetric
def is_symmetric(matrix):
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix[0])))

# Example matrix
matrix_symmetric = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix_symmetric):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")

# 26. Find the LCM of two numbers
def find_lcm(x, y):
    return abs(x*y) // math.gcd(x, y)

num1_lcm = int(input("Enter the first number: "))
num2_lcm = int(input("Enter the second number: "))
lcm = find_lcm(num1_lcm, num2_lcm)
print("LCM of", num1_lcm, "and", num2_lcm, "is", lcm)

# 27. Simulate a dice rolling game
dice_roll = random.randint(1, 6)
print("You rolled:", dice_roll)

# 28. Count the occurrences of each character in a string
input_string_occurrences = input("Enter a string: ")
char_occurrences = {}
for char in input_string_occurrences:
    char_occurrences[char] = char_occurrences.get(char, 0) + 1
print("Occurrences of each character:", char_occurrences)

# 29. Find the square of a number without using the ** operator
number_to_square = float(input("Enter a number: "))
square_without_operator = number_to_square * number_to_square
print("Square of", number_to_square, "without using ** operator:", square_without_operator)

# 30. Check if a given number is an Armstrong number
def is_armstrong_number(number):
    num_digits = len(str(number))
    sum_of_digits = sum(int(digit)**num_digits for digit in str(number))
    return number == sum_of_digits

number_armstrong = int(input("Enter a number: "))
if is_armstrong_number(number_armstrong):
    print(number_armstrong, "is an Armstrong number.")
else:
    print(number_armstrong, "is not an Armstrong number.")
