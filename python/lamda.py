# TASK 1: Filter even and odd numbers using Lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even)
print("Odd numbers:", odd)


# TASK 2: Check if a string starts with a given character using Lambda

word = "Python"
character = "P"

check = lambda x: x.startswith(character)

print(check(word))


#TASK3:

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = list(filter(lambda x: x in list2, list1))

print("Intersection:", intersection)


#TASK 4

numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Numbers divisible by 19 or 13:", result)