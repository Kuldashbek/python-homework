# Create and Access List Elements
fruits = ["apple", "banana", "orange", "mango", "kiwi"]
print(fruits[2])

#Concatenate Two Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#Extract First, Middle, Last Elements
nums = [10, 20, 30, 40, 50]
new_list = [nums[0], nums[len(nums)//2], nums[-1]]
print(new_list)

#Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "Matrix", "Interstellar"]
movies_tuple = tuple(movies)
print(movies_tuple)

#Check "Paris" in List
cities = ["London", "Tokyo", "Paris", "Dubai"]
print("Paris" in cities)

#Duplicate List (No Loop)
numbers = [1, 2, 3]
dup = numbers * 2
print(dup)

#Swap First and Last Elements
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

#Slice Tuple (index 3 to 7)
t = (1,2,3,4,5,6,7,8,9,10)
print(t[3:8])

#Count "blue" in List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))

#Find Index of "lion"
animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))

#Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

#Length of List and Tuple
my_list = [10, 20, 30]
my_tuple = (100, 200, 300, 400)
print(len(my_list))
print(len(my_tuple))

#Convert Tuple to List
nums = (5, 10, 15, 20, 25)
nums_list = list(nums)
print(nums_list)

#Max and Min in Tuple
t = (4, 9, 2, 7, 1, 5)
print(max(t))
print(min(t))

#Reverse a Tuple
words = ("hello", "world", "python")
print(words[::-1])


