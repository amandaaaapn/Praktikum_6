import math
def a(x):
    return x**2
    a = lambda x : x ** 2
print(2)\

def b(x,y):
    return math.sqrt(x*2 + y*2)
    b = lambda x,y : x * 2 + y * 2
print(2 , 2)

def c(*args):
    return sum(args)/len(args)
    c = lambda *args : sun(args)/len(args)
print(5, -6, 7, 8)

def d(s):
    return "".join(set(s))
d = lambda s: "".join(set(s))
print("AMANDA PUSPA NEGARA")