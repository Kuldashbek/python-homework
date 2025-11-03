# Калькулятор возраста

#Пользователь вводит имя и год рождения — программа выводит возраст.
name = input("Enter your name: ")
year = int(input("Enter your birth year: "))

age = 2025 - year
print(name, "is", age, "years old.")

#Извлечение названий автомобилей
txt = 'LMaasleitbtui'
car1 = txt[0:4]      # Lamb
car2 = txt[4:9]      # aslei -> Tesla (перемешано)
car3 = txt[9:12]     # tbu -> BMW (почти)
car4 = txt[2] + txt[6] + txt[10] + txt[11]  # Audi (примерно)

print(car1, car2, car3, car4)

#Но, скорей всего, необходимо вытянуть чётные или нечётные буквы :
txt = 'LMaasleitbtui'
result = txt[::2]
print(result)

#Извлечение названий автомобилей (2)
txt = 'MsaatmiazD'
print(txt[::2])   # MamiaD (Mazda)


#Извлечение жилой зоны
txt = "I'am John. I am from London"
part = txt.split("from ")[1]
print(part)


#Обратная струна
text = input("Enter text: ")
print(text[::-1])


#Считайте гласные
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)


#Найдите максимальное значение
numbers = [3, 11, 7, 25, 9]
print(max(numbers))

#(или через ввод)
nums = input("Enter numbers separated by space: ")
nums = list(map(int, nums.split()))
print(max(nums))

#Проверьте палиндром
word = input("Enter word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


#Извлечение домена электронной почты
email = input("Enter email: ")
domain = email.split("@")[1]
print(domain)

#Генерация случайного пароля

import random
import string

chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choice(chars) for i in range(10))
print(password)


