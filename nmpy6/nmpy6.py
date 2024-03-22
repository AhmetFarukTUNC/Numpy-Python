import numpy as np

# np.arange()

x = np.arange(5)

print(x)

print(x[0])

print(x[2])

print(x[5-2])

print(x[-1])

print(x[-2])

print(x[-5])

x[2] = 200

print()

print(x)

print(x[2])

y = np.arange(12).reshape(3,4)

print(y)

print(y[0,0])

print(y[1,2])

y[0,0] = 100

print(y)

a = np.arange(6)

print(a)

y = np.delete(a,[0,1])

print(y)

print(a)

c= np.arange(16).reshape(4,4)

print(c)

c = np.delete(c,1,axis=0)

print()

print(c)

