import os

pth = input()

f = os.access(pth, os.F_OK)
r = os.access(pth, os.R_OK)
w = os.access(pth, os.W_OK)
x = os.access(pth, os.X_OK)
print(f)
print(r)
print(w)
print(x)