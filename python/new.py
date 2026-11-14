#Task1
word = "hello"
print(word[::-1])

#Task2
word1 = "python"
count = 0
for i in word1:
    if i in "aeiou":
        count = count + 1
        
print(count)

#Task3
word2 = "madam"
print ("True" if word2 == word2[::-1] else "False")

#Task4
word3 = "python is fun"
print(word3.replace(" ",""))

#Task5
word5 = "PyThOn"
print(word5.swapcase())

#Task6
word6 = "hello"
count = ""
for i in word6:
    if i in "aeiou":
        count += "*"
    else:
        count += i
print(count)

#Task7
word7 = "Hello World"
print(word7[:5][::-1] + " " + word7[6:][::-1])

#Task8
word8 = "The quick brown word"
longest = ""
for i in word8.split():
    if len(i) > len(longest):
        longest = i
print(longest)

#Task9
word = "This is is a test test"
result = ""

for i in word.split():
    if i not in result.split():
        result += i + " "

print(result.strip())
    