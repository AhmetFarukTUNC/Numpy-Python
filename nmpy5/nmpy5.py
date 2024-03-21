import numpy as np

# np.arange()

# x = np.arange(10)

# print(x)

# print()

# y = np.arange(4,9)

# print(y)

# print()

# z = np.arange(3,22,4)

# print(z)

# print()  

# np.linspace()

a = np.linspace(0,15,10)

print(a)

print()

b = np.linspace(0,15) # N = 50

print(b)

print()

c = np.linspace(0,15,endpoint=False) # N = 50

print(c)

print()

d = np.arange(20)

print(d)

print()

e = np.reshape(d,(4,5))

print(e)

print()

t=np.arange(32)

f = np.reshape(t,(2,4,4))

print(f)

print()

g = np.linspace(0,19,20)

print(g)

print()

h = np.reshape(g,(2,10))

print(h)

print()

j = np.linspace(0,19,20).reshape(2,10)

print(j)

print()

# random.random() => [0,1)

k = np.random.random((2,3))

print(k)

print()

l = np.random.randint(3,12,size=(3,2))

print(l)

print()




