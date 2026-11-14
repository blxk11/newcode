#task1
print("--task1--")
a = {1,2,3}
b = {3,4,5}
c = set()
for i in a:
    c.add(i)
    for j in b:
      c.add(j)
print(c)

#task2
print("--task2--")
d = {1,2,3}
e = {3,4,5}
f = set()
for k in d:
    if k in e:
        f.add(k)
print(f)

#task3
print("--task3--")

nums = [1,2,3,4,4]
sets = set()
for i in nums:
    sets.add(i)
print(sets)

#task4
print("--task4--")
num = [1,1,2,2,3,4,4]
sett = set()
for i in num:
    if i not in sett:
        sett.add(i)
print(len(sett))

#task5
print("--task5--")
l = {1, 2, 3}
m = {2, 3, 4}
n = {3, 2, 5}
lo = set()
for i in l:
    for j in m:
        for k in n:
            if i == j and j == k:
                lo.add(i)
print(lo)