import numpy as np

x1 = np.zeros(4)

print(x1)

print(x1.dtype)

y1 = np.ones(4)

print(y1)

print(y1.dtype)

x2 = np.zeros((2,3,4),dtype=np.int)

print(x2)

y2 = np.ones((3,2))

print(y2)

x = np.full((2,3),10.0)

print(x)

print(x.dtype)

y = 10.0 * np.ones((2,3))

z = 10.0 + np.ones((2,3))

print(y)

print(z)

a = np.empty((2,2))

print(a)

a.fill(3)

print(a)

x = np.eye(4)

print(x)

y = np.eye(5,4)

print(y)

z = np.eye(6,k=1)

print(z)

print()

t = np.eye(6,k=-2)

print(t)

print()

e = np.identity(5)

print(e)

print()

ö = np.diag([4,7,11,3])

print(ö)

print()