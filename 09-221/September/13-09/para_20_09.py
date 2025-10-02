text = "кот собака кот попугай собака тигр"
words = text.split()
unique = {w for w in words if words.count(w) == 1}
print(unique)  # {'тигр', 'попугай'}



student = {"name": "Иван", "age": 20}

print(student["name"])  # Иван
print(student.get("group", "не указано"))

student["age"] = 21
student["group"] = "A1"
print(student)



from collections import defaultdict, Counter

# defaultdict
names = ["Анна","Алексей","Иван","Игорь"]
groups = defaultdict(list)
for n in names:
    groups[n[0]].append(n)
print(groups)

# Counter
cnt = Counter("banana")
print(cnt)  # Counter({'a':3,'n':2,'b':1})



from collections import Counter
words = text.split()
cnt = Counter(words)
print(cnt.most_common(3))
# [('кот', 3), ('собака', 2), ('попугай', 1)]


from collections import Counter

text = "кот собака кот попугай собака кот"
words = text.split()

cnt = Counter(words)

items = list(cnt.items())
items_sorted = sorted(items, key=lambda x: x[1], reverse=True)

# берем топ-3
top3 = items_sorted[:3]

print(top3)
# [('кот', 3), ('собака', 2), ('попугай', 1)]



def power_func(exp):
    def inner(x):
        return x ** exp
    return inner

square = power_func(2)
cube = power_func(3)

print(square(4))  # 16
print(cube(2))    # 8





import random, string

def password_maker(length=8, use_specials=True):
    chars = string.ascii_letters + string.digits
    if use_specials:
        chars += string.punctuation

    def make():
        return "".join(random.choice(chars) for _ in range(length))

    return make

# генератор на 8 символов со спецсимволами
gen8 = password_maker(8, use_specials=True)
print(gen8(), gen8())

# генератор на 12 символов без спецсимволов
gen12 = password_maker(12, use_specials=False)
print(gen12(), gen12())




def uppercase(fn):
    def wrapper(*a, **kw):
        result = fn(*a, **kw)
        return result.upper()
    return wrapper

@uppercase
def hello(name):
    return f"Привет, {name}"

print(hello("Иван"))  # ПРИВЕТ, ИВАН





def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fib()
for _ in range(7):
    print(next(g), end=" ")
# 0 1 1 2 3 5 8