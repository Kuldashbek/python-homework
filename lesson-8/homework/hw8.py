#Обработка исключений — игра
#Ошибка нулевого деления
try:
    x = float(input("Введите число: "))
    y = float(input("Введите делитель: "))
    print(x / y)
except ZeroDivisionError:
    print("Ошибка: деление на ноль запрещено.")

#ValueError при нечисловом вводе целого
try:
    n = int(input("Введите целое число: "))
    print("OK:", n)
except ValueError:
    print("Ошибка: нужно ввести целое число.")

#Ошибка FileNotFound
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден.")

#TypeError при нечисловом вводе двух чисел
try:
    a = input("a: ")
    b = input("b: ")
    a = float(a); b = float(b)
    print("Сумма:", a + b)
except ValueError:
    raise TypeError("Оба значения должны быть числами.")

#Ошибка разрешения
try:
    with open("/root/protected.txt", "w", encoding="utf-8") as f:  # пример пути без прав
        f.write("test")
except PermissionError:
    print("Нет прав для записи в файл.")

#IndexError (операция со списком вне наушников)
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Индекс вне диапазона списка.")

#KeyboardInterrupt (отмена ввода пользователем: Ctrl+C)
try:
    x = input("Введите число (Ctrl+C для отмены): ")
    print("Вы ввели:", x)
except KeyboardInterrupt:
    print("\nВвод отменён пользователем.")

#ArithmeticError (базовый класс арифм. ошибок)
try:
    x = 10
    y = 0
    print(x / y)
except ArithmeticError:
    print("Арифметическая ошибка (например, деление на ноль).")

#UnicodeDecodeError (ошибка декодирования)
filename = "text_unknown_encoding.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Ошибка кодировки. Пробуем другую кодировку...")
    with open(filename, "r", encoding="latin-1", errors="replace") as f:
        print(f.read())

#AttributeError (несуществующий атрибут)
try:
    lst = [1, 2, 3]
    lst.push(4)  # у list нет метода push
except AttributeError:
    print("Атрибут/метод не существует для данного объекта.")

#Файловый ввод-вывод — рисунок
#Во всех примерах используйте стандартный вариант with open(..., encoding="utf-8").
#Прочитать весь файл
with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

#Прочитать первые n строк
n = 3
with open("file.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        if i > n: break
        print(line.rstrip("\n"))

#Дописать текст в файл и показать требования
text = "Новая строка\n"
with open("file.txt", "a", encoding="utf-8") as f:
    f.write(text)

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

#Прочитать последние n строк (простой способ)
n = 3
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("".join(lines[-n:]))

#Читать построчно и сохранить в списке.
with open("file.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]
print(lines)

#Читать построчно и сохранить в переменной (одной строке)
with open("file.txt", "r", encoding="utf-8") as f:
    data = f.read()
print(data)

#Читать построчно и сохранить в массиве символов (буквально «массив» символов)
chars = []
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        chars.extend(list(line))
print(chars)

#Найти самые длинные слова
import re

with open("file.txt", "r", encoding="utf-8") as f:
    words = re.findall(r"\w+", f.read(), flags=re.UNICODE)

max_len = max(map(len, words)) if words else 0
longest = [w for w in words if len(w) == max_len]
print(longest)

#Посчитать количество строк
with open("file.txt", "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
print("Строк:", count)

#Частота слов в файле
import re
from collections import Counter

with open("file.txt", "r", encoding="utf-8") as f:
    tokens = re.findall(r"\w+", f.read().lower(), flags=re.UNICODE)
freq = Counter(tokens)
print(freq)

#Размер файла в байтах
import os
size = os.path.getsize("file.txt")
print(size, "bytes")

#Записать список в файл (по строке элемента)
items = ["apple", "banana", "cherry"]
with open("out.txt", "w", encoding="utf-8") as f:
    for x in items:
        f.write(str(x) + "\n")

#Скопировать классический файл в другой
src, dst = "file.txt", "copy.txt"
with open(src, "r", encoding="utf-8") as fsrc, open(dst, "w", encoding="utf-8") as fdst:
    for line in fsrc:
        fdst.write(line)

#Объединить строки двух файлов по соответствию строк.
from itertools import zip_longest

with open("a.txt", "r", encoding="utf-8") as f1, open("b.txt", "r", encoding="utf-8") as f2, open("merged.txt", "w", encoding="utf-8") as out:
    for l1, l2 in zip_longest(f1, f2, fillvalue=""):
        out.write((l1.rstrip("\n") + " " + l2).rstrip("\n") + "\n")

#Прочитать случайный текст из файла.
import random

with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
if lines:
    print(random.choice(lines))

#Посмотреть, закрыть ли файл
f = open("file.txt", "r", encoding="utf-8")
print("Закрыт?", f.closed)
f.close()
print("Закрыт теперь?", f.closed)

#Удалить символы перевода при чтении.
with open("file.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]
print(lines)

#Посчитать количество слов в файле (учитывая запятые без пробела)
import re

with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()
words = re.findall(r"\w+", text, flags=re.UNICODE)
print("Слов:", len(words))

#Использовать символы из разных текстовых файлов в списке.
import glob

chars = []
for path in glob.glob("*.txt"):
    with open(path, "r", encoding="utf-8") as f:
        chars.extend(list(f.read()))
print(chars)

#Сгенерировать файлы A.txt… Z.txt
import string

for ch in string.ascii_uppercase:
    with open(f"{ch}.txt", "w", encoding="utf-8") as f:
        f.write(f"Файл {ch}.txt\n")

#Создать файл, где алфавит разбит по N буквам в строке.
import string

N = 5  # букв на строку
alphabet = string.ascii_lowercase
with open("alphabet_blocked.txt", "w", encoding="utf-8") as f:
    for i in range(0, len(alphabet), N):
        f.write(alphabet[i:i+N] + "\n")


