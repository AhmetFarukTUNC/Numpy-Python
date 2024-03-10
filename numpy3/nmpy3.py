import numpy as np

x = np.array([3,4,5],dtype=np.int_)

print(x)

print(x.dtype)

y = np.array([3,4,5], dtype=np.float_)

print(y)

print(y.dtype)


z = np.array([3,4,5], dtype=np.complex_)

print(z)

print(z.dtype)

# downcast

a = np.array([1.2,2.7,3.8],dtype=np.int_)

print(a)

print(a.dtype)

b = np.array([1,2,3,4],dtype=np.float_)

print(b)

print(b.dtype)

b = np.array(b,dtype=np.complex_)

print(b)

print(b.dtype)

x1 = np.array([1,2,3],dtype=np.int_)

x2 = np.array([5.2,2.8,4.5],dtype=np.float_)

print(x1 + x2)

print((x1 + x2).dtype)

x = np.sqrt(np.array([-1,9,4],dtype=np.complex_))

print(x)

print(x.dtype)

print(x.real)

print(x.imag)

#Save Operation In Python

c = np.array([5,9,3.2,16])

np.savetxt("ndarray_1",c)

d = np.load("ndarray_1.npy")

print(d)

print(d.shape) # eleman sayısını verir.