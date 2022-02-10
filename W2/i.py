n = int(input())
l1st = []
l2st = []
for i in range(n):
    arr = list(map(str, input().split()))
    if len(arr) == 2 and arr[0] == '1':
        l1st.insert(0, arr[1])
    elif len(arr) == 1 and arr[0] == '2':
        l2st.append(l1st[len(l1st)-1])
        l1st.pop()
print(*l2st)