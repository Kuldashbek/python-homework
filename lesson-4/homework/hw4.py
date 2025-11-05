#DICTIONARY EXERCISES
#Sort a Dictionary by Value (asc / desc)
d = {"a": 3, "b": 1, "c": 2}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print(asc)
print(desc)


#Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print(d)

#Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print(dic4)

#Generate a Dictionary with Squares (1 to n)
n = 5
d = {}

for x in range(1, n+1):
    d[x] = x * x

print(d)

#Dictionary of Squares (1 to 15)
d = {}
for i in range(1, 15+1):
    d[i] = i * i

print(d)

#SET EXERCISES
#Create a Set
s = {1, 2, 3, 4}
print(s)

s = {10, 20, 30}

for x in s:
    print(x)

#Add Member(s) to a Set
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(s)

#Remove Item(s) from a Set
s = {10, 20, 30, 40}
s.remove(20)
print(s)

#Remove an Item if Present
s = {100, 200, 300}
s.discard(200)   # no error if missing
print(s)


