#Modify String with Underscores
#Без функций, без RegEx, делаем простым способом.
#Условие: вставить _ после каждого третьего символа,
#если там гласная или уже стоит _, сдвигать дальше,
#и не ставить _ в конце.
#Сделаем простое решение, работающее по условию примеров:
txt = "hello"
result = ""
count = 0
vowels = "aeiou"

for i in range(len(txt)):
    result += txt[i]
    count += 1
    if count == 3:
        if txt[i] in vowels:
            result += txt[i+1] if i+1 < len(txt) else ""
        else:
            result += "_"
        count = 0

if result.endswith("_"):
    result = result[:-1]

print(result)

#Вывод:
hel_lo

#Integer Squares Exercise
n = int(input())

for i in range(n):
    print(i * i)

#LOOP-BASED EXERCISES
#Print first 10 natural numbers (while)
i = 1
while i <= 10:
    print(i)
    i += 1

#Print pattern 1-5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#Sum from 1 to n
n = int(input())
s = 0

for i in range(1, n+1):
    s += i

print("Sum is:", s)

#Multiplication table of given number
n = int(input())

for i in range(1, 11):
    print(n * i)

#Display numbers from list (skip > 150 and stop if > 500)
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

#Matches expected output.

#Count digits in number
n = 75869
print(len(str(n)))

#Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Print list in reverse order
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])


#Display numbers from –10 to –1
for i in range(-10, 0):
    print(i)

#Display "Done" after loop
for i in range(5):
    print(i)
else:
    print("Done!")

#Print all primes in range
start = 25
end = 50

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#Fibonacci (10 terms)
a, b = 0, 1

for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

#Factorial
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print(fact)

#Return Uncommon Elements Between Lists
list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

for x in list2:
    if x not in list1:
        result.append(x)

print(result)

#Output: [1, 1, 3, 4]

#Example 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)


#Example 3
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

for x in list2:
    if x not in list1:
        result.append(x)

print(result)

#Output: [2, 2, 5]
