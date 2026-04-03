# 1
x = lambda a, b:a if a > b else b
print(x(8, 4))

# 2
x = lambda a: a if a >= 0 else -a
print(x(-5))

# 3
x = lambda a, b, c: a + b + c
print(x(3, 4, 5))

# 4
x = lambda a, b: a % b
print(x(17, 5))

# 5
x = lambda c: c * 9/5 + 32

print(x(100))

# 6
kichik = lambda a, b: a if a < b else (b if b < a else 0)

print(kichik(5, 3))

# 7
x = lambda a: a if a % 2 == 0 else "toq son"
print(x(4))

# 8
x = lambda a, b: a * b

print(x(6, 9))

# 9
x = lambda a, b, c: max(a, b, c)
print(x(4, 17, 9))

# 10
x = lambda son: len(str(son))
print(x(2435435))

# 11
bolinadimi = lambda a, b: a % b == 0

print(bolinadimi(20, 4))

# 12
x = lambda r: 3.14 * r**2

print(x(7))

# 13
x = lambda a, b: (a - b) ** 2
print(x(12, 6))

# 15
x = lambda a, b, c: "teng tomonli" if a == b and b == c else "teng yonli" if a == b or a == c or b == c else "oddiy"

res = x(1, 1, 1)
print(res)
