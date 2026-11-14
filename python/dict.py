#task1
print("--task1--")
data = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}

for i in data:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#task2
print("--task2--")
dict = {'a': 1,"b": 2,"c": 3}
result  = {}
for i in dict:
    result[dict[i]] = i
print(result)

#task3
print("--task3--")
scores = {'Alice': 88, 'Bob': 95, 'Charlie': 70}
score = 0
for i in scores:
    if scores[i] > score:
        score = scores[i]
print(score)

#task4
print("--task4--")
sort =  {'apple': 5, 'banana': 2, 'cherry': 7}
names = ""
m = 0
for i in sort:
    if sort[i] > m:
        m = sort[i]
        names = i
print(names, m)
    