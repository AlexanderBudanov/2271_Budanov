def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def add(a, b):
    return a + b
add = toint(add)
print(add("10", "10"))
print(add(10.9, 10.1))

def mul(a, b):
    return a * b
mul = toint(mul)
print(mul("5", "5"))
print(mul(5.1, 5.9))

def total(*nums):
    return sum(nums)
total = toint(total)
print(total('1', '2', '3', '4', 5.1))