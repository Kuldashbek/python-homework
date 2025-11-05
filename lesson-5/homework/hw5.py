#Функция is_leap(year)
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Conditional Statements Exercise ("Weird / Not Weird")
n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#Найти чётные числа между a и b (включительно), без цикла
#Solution 1 (с if-else)
a = 3
b = 12

if a % 2 == 0:
    first = a
else:
    first = a + 1

evens = list(range(first, b + 1, 2))
print(evens)

#Solution 2 (без if-else)
a = 3
b = 12

evens = list(range(a + (a % 2), b + 1, 2))
print(evens)


