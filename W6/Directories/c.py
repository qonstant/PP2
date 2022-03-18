import os

pth = input()

if os.path.exists(pth):
	print("Exists")
	print(os.path.basename(pth))
	print(os.path.dirname(pth))
else:
    print("Not exists")