from math import pi, sqrt
from datetime import date
from collections import deque

# 1) Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


# 2) Person Class
class Person:
    def __init__(self, name, country, year, month, day):
        self.name = name
        self.country = country
        self.dob = date(year, month, day)

    def age(self):
        today = date.today()
        years = today.year - self.dob.year
        # корректируем, если ДР ещё не был в этом году
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            years -= 1
        return years


# 3) Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): 
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b


# 4) Shape base + subclasses
class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError

class CircleShape(Shape):
    def __init__(self, r): self.r = r
    def area(self): return pi * self.r * self.r
    def perimeter(self): return 2 * pi * self.r

class Square(Shape):
    def __init__(self, a): self.a = a
    def area(self): return self.a * self.a
    def perimeter(self): return 4 * self.a

class Triangle(Shape):
    # по трём сторонам (a,b,c), площадь по Герону
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return sqrt(max(s*(s-self.a)*(s-self.b)*(s-self.c), 0))


# 5) Binary Search Tree (insert + search)
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = BSTNode(key)
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    cur.right = BSTNode(key)
                    return
                cur = cur.right
            else:
                return  # ключ уже есть

    def search(self, key):
        cur = self.root
        while cur:
            if key < cur.key: cur = cur.left
            elif key > cur.key: cur = cur.right
            else: return True
        return False


# 6) Stack (push/pop)
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


# 7) Singly Linked List (display / insert / delete)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def delete_value(self, val):
        prev, cur = None, self.head
        while cur:
            if cur.val == val:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def to_list(self):
        res, cur = [], self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


# 8) Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []  # элементы: {"name": str, "price": float, "qty": int}

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": float(price), "qty": int(qty)})

    def remove_item(self, name):
        self.items = [it for it in self.items if it["name"] != name]

    def total(self):
        return sum(it["price"] * it["qty"] for it in self.items)


# 9) Stack with display
class DisplayStack:
    def __init__(self):
        self.data = []

    def push(self, x): self.data.append(x)
    def pop(self):
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()
    def display(self):
        # сверху справа — просто печать списка
        print(self.data)


# 10) Queue (enqueue/dequeue)
class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x): self.q.append(x)
    def dequeue(self):
        if not self.q:
            raise IndexError("dequeue from empty queue")
        return self.q.popleft()
    def is_empty(self): return len(self.q) == 0


# 11) Bank
class Bank:
    def __init__(self):
        self.accounts = {}  # account_id -> balance

    def create_account(self, acc_id, initial=0.0):
        if acc_id in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[acc_id] = float(initial)

    def deposit(self, acc_id, amount):
        self._check(acc_id)
        if amount < 0: raise ValueError("Negative deposit")
        self.accounts[acc_id] += amount

    def withdraw(self, acc_id, amount):
        self._check(acc_id)
        if amount < 0: raise ValueError("Negative withdrawal")
        if self.accounts[acc_id] < amount:
            raise ValueError("Insufficient funds")
        self.accounts[acc_id] -= amount

    def transfer(self, src, dst, amount):
        self._check(src); self._check(dst)
        if amount < 0: raise ValueError("Negative transfer")
        if self.accounts[src] < amount:
            raise ValueError("Insufficient funds")
        self.accounts[src] -= amount
        self.accounts[dst] += amount

    def balance(self, acc_id):
        self._check(acc_id)
        return self.accounts[acc_id]

    def _check(self, acc_id):
        if acc_id not in self.accounts:
            raise KeyError("Account not found")


# --- Мини-демо (можно удалить перед сдачей) ---
if __name__ == "__main__":
    # 1) Circle
    c = Circle(3)
    print("Circle area:", round(c.area(), 2), "perimeter:", round(c.perimeter(), 2))

    # 2) Person
    p = Person("Ali", "UZ", 1995, 11, 1)
    print("Age:", p.age())

    # 3) Calculator
    calc = Calculator()
    print("2+3=", calc.add(2, 3))

    # 4) Shapes
    s1, s2, s3 = CircleShape(2), Square(4), Triangle(3, 4, 5)
    print("Square area:", s2.area(), "perimeter:", s2.perimeter())
    print("Triangle area:", s3.area(), "perimeter:", s3.perimeter())

    # 5) BST
    tree = BST()
    for k in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(k)
    print("BST search 4 ->", tree.search(4), "; 10 ->", tree.search(10))

    # 6) Stack
    st = Stack()
    st.push(10); st.push(20)
    print("Stack pop:", st.pop())

    # 7) LinkedList
    ll = LinkedList()
    for v in [1, 2, 3, 2]:
        ll.insert_end(v)
    ll.delete_value(2)
    print("LinkedList:", ll.to_list())

    # 8) ShoppingCart
    cart = ShoppingCart()
    cart.add_item("apple", 1.2, 3)
    cart.add_item("milk", 2.5, 1)
    print("Cart total:", cart.total())

    # 9) DisplayStack
    ds = DisplayStack()
    ds.push(1); ds.push(2); ds.display(); ds.pop(); ds.display()

    # 10) Queue
    q = Queue()
    q.enqueue(5); q.enqueue(6)
    print("Deq:", q.dequeue())

    # 11) Bank
    bank = Bank()
    bank.create_account("A", 100)
    bank.create_account("B", 50)
    bank.transfer("A", "B", 30)
    print("Balance A:", bank.balance("A"), "Balance B:", bank.balance("B"))

