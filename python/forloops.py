#task1
for i in range(101):
    if i % 2 == 0:
        print(i)

#task2
n = 5
count = 0
for i in range(1,11):
    count = n * i
    print(f"{n} x {i} = {count}")
    
#task3
j = 5
count = 1
for i in range(1,j + 1):
    count = count * i
    print(count)
    


# TASK 4: Print all odd numbers between two given numbers

start = 1
end = 20

for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)


# TASK 5: Print the squares of numbers from 1 to 10

for i in range(1, 11):
    print(i, "=", i * i)


# TASK 6: Count how many times a specific character appears in a string

word = "programming"
character = "m"
count = 0

for i in word:
    if i == character:
        count += 1

print("Character count:", count)


# TASK 7: Find the sum of all elements in a list

numbers = [10, 20, 30, 40, 50]
total = 0

for i in numbers:
    total = total + i

print("Sum:", total)


# TASK 8: Print Floyd's Triangle

rows = 5
number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()


# TASK 9: Right-Aligned Number Triangle

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + str(i) * i)


# TASK 10: Pyramid Pattern

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()