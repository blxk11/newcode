# i = 10
# while i > 0:
#     print(i)
#     i = i - 1

# i = 123
# result = 0
# while i > 0:
#     n = i % 10
#     result = result + n
#     i = i // 10
    
# print(result)

# i = 456
# result = 0

# while i > 0:
#     n = i % 10
#     result = result * 10 + n
#     i = i // 10

# print(result)

# num = 555
# original = num
# result = 0

# while num > 0:
#     n = num % 10
#     result = result * 10 + n
#     num = num // 10

# if original == result:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# login = "vaishnav"
# password = 54321
# while True:
#     login1 = input("Enter username : ")
#     password1 = int(input("Enter password : "))
#     if login == login1 and password == password1:
#         print("true")
#         break
#     else:
#         print("false")
    
# nums = 1234457234
# count = 0

# while nums > 0:
#     nums = nums // 10
#     count = count + 1

# print(count)

# number = 4563896
# largest = 0
# while number > 0:
#     digit = number % 10
#     if digit > largest:
#         largest = digit
#     number = number // 10
# print(largest)

n = 7
a = 0
b = 1
count = 0

while count < n:
    print(a)

    c = a + b
    a = b
    b = c

    count += 1