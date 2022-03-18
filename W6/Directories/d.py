cnt = 0
with open('file.txt') as f:
	for i in f:
		cnt += 1
print(cnt)