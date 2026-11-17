# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

# n = 5
# total = 1
# for i in range(1,11):
#     total = n * i
#     print(f"{n} x {i} = {total}")

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
#     print(fact)

# n1 = int(input("Enter a number :"))
# n2 = int(input("Enter b number :"))
# for i in range(n1, n2):
#     if i % 2 != 0:
#         print(i)


# for i in range(1,11):
#     square = i * i 
#     print(square)
    
# word = input("Enter a word :")
# word1 = input("enter b word :")
# count = 0
# for i in word:
#     if i == word1:
#         count =count + 1
# print(count)
    
    
# numbers = [10, 20, 30, 40, 50]
# count = 0
# for i in numbers:
#     count = count + i
# print(count)

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()