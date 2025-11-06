#Teoriya: map() va filter() — qisqa tushuntirish
#map(function, iterable)
#ro‘yxatdagi har bir elementga funksiya qo‘llanadi
#natija yangi list (yoki boshqa iterable)
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)   # [1, 4, 9, 16]

#filter(function, iterable)
#ro‘yxatdan shartga mos kelgan elementlargina qoladi
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6]

#map = "hammasini o‘zgartir"
#filter = "faqat moslarini qoldir"
#is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Tekshirish:
print(is_prime(4))   # False
print(is_prime(7))   # True

#digit_sum(k) funksiyasi
def digit_sum(k):
    s = 0
    for digit in str(k):
        s += int(digit)
    return s

#Test:
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

#N dan oshmaydigan 2 ning darajalari
def powers_of_two(N):
    x = 1
    while x * 2 <= N:
        x *= 2
        print(x, end=" ")

#Test:
Input: 10
Output: 2 4 8

#Qo‘shimcha: Shu vazifani map/filter bilan ham ishlatish mumkinmi?
#digit_sum uchun:
print(sum(map(int, str(502))))   # 7

#Tub sonlarni filter orqali topish:
nums = list(range(1, 30))
prime_nums = list(filter(is_prime, nums))
print(prime_nums)

#2 ning darajalari (list-comp usuli):
N = 50
print([2**k for k in range(10) if 2**k <= N])


