# TASK 1: Print even numbers between 1 and 50

def print_even():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)

print_even()


# TASK 2: Print the multiplication table of a number

def multiplication(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication(5)


# TASK 3: Calculate the sum of numbers from 1 to n

def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print("Sum:", calculate_sum(10))


# TASK 4: Count vowels and consonants in a string

def count_letters(word):
    vowels = 0
    consonants = 0

    for i in word.lower():
        if i in "aeiou":
            vowels += 1
        elif i.isalpha():
            consonants += 1

    return vowels, consonants

v, c = count_letters("Hello World")

print("Vowels:", v)
print("Consonants:", c)


# TASK 5: Check if a string is a palindrome using a loop

def palindrome(word):
    reverse = ""

    for i in word:
        reverse = i + reverse

    if word == reverse:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"

print(palindrome("madam"))


# TASK 6: Calculate addition and subtraction
# Return both results in a single return call

def calculation(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

add, sub = calculation(20, 10)

print("Addition:", add)
print("Subtraction:", sub)


# TASK 7: Recursive function to calculate sum from 0 to 10

def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)

print("Sum:", recursive_sum(10))


# TASK 8: Count uppercase and lowercase letters

def count_case(word):
    uppercase = 0
    lowercase = 0

    for i in word:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1

    return uppercase, lowercase

upper, lower = count_case("Hello PYTHON")

print("Uppercase:", upper)
print("Lowercase:", lower)


# TASK 9: Return a new list containing distinct elements

def distinct(numbers):
    result = []

    for i in numbers:
        if i not in result:
            result.append(i)

    return result

print("Distinct elements:", distinct([1, 2, 2, 3, 4, 4, 5]))


# TASK 10: Check whether a number is prime or not

def prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("Is prime?", prime(7))
print("Is prime?", prime(10))