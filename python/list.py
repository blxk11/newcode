#task1
print("---Task1---")
task1 = [2,2,4,6,5,3]
result = []
for i in task1:
    if i not in result:
        result.append(i)
print(result)

#Task2
print("---Task2---")
numbers = [2, 4, 3, 5, 7]
target = 7

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            
#Task3
print("--Task3--")
task3 = [[1, 2], [3, 4], [5]]
result1 = []

for i in task3:
    for item in i:
        result1.append(item)

print(result1)

            
#Task4
print("---Task4---")
task4 = [1, 2, 8, 4, 6, 7]
largest = 0
second = 0
for i in task4:
    if i > largest:
        largest = i
    elif i > second and i != largest:
        second = i
print(second)

    
#task5
print("---Task5---")
list1 = [1,2,3]
list2 = [2,3,4]
re = []
for i in list1:
    for k in list2:
        if i == k :
            if i not in re:
                re.append(i)
print(re)


  
#Task6  
print("---Task6---")        
num = [-2,3,4,-5,2]
result6 = []
for i in num:
    if i < 0 :
        result6.append(0)
    else :
        result6.append(i)
print(result6)


#Task7
print("---Task7---")
sep = [2, 3, 4, 5, 6, 7, 7, 0, 3, 2, 0]

odd = 0
even = 0
zero = 0

for i in sep:
    if i == 0:
        zero += 1
    elif i % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd)
print(even)
print(zero)

#task8
print("--Task8--")
list10 = ['a', 'b', 'c']
list11 = [1, 2, 3, 4]

result8 = []

for i in range(len(list10)):
    result8.append(list10[i])
    result8.append(list11[i])

for i in range(len(list10), len(list11)):
    result8.append(list11[i])

print(result8)

#task9
print("--task9--")
nums = [1, 2, 2, 3, 4, 4, 5]
result9 = []

for i in nums:
    count = 0

    for j in nums:
        if i == j:
            count += 1

    if count == 1:
        result9.append(i)

print(result9)

#task10
print("--task10--")
words = ['apple', 'banana', 'cherry', 'kiwi']

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)

#task11
print("--task11--")
task11 = [4, 5, 6, 7, 8, 5, 6]

for i in task11:
    count = 0

    for j in task11:
        if i == j:
            count += 1

    if count == 1:
        print(i)
        break
    
#task12
print("---Task12---")
task12 = [1, 2, 3, 2, 3, 3, 1]

for i in task12:
    count = 0

    for k in task12:
        if i == k:
            count += 1

    if count % 2 != 0:
        print(i)
        break

