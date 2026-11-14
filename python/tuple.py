#task1
print("--Task1--")
num = (1,2,3,4)
num = num + (10,)
print(num)

#task2
print("--Task2--")
num1 = (1,2,3,4,5,6)
target = 7
for i in range (len(num1)):
    for j in range(i +1, len(num1)):
        if num1[i] + num1[j] == target:
            print(num1[i], num1[j])

#task3
print("--Task3--")
num2 = ((1, 'a'), (2, 'b'), (3, 'a'))
re = ()
for i in num2:
    if i[1] != "a":
        re += (i,)
print(re)

#task4
print("--Task4--")
nums = (10, 20, 30, 40, 50)
index = 2
result = ()

for i in range(len(nums)):
    if i != index:
        result += (nums[i],)

print(result)