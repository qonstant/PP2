def solve(numhead, numleg):
    chicken =  numleg//2 - numhead
    return (chicken, (numhead - chicken))
heads, legs = map(int, input().split())
print(*solve(heads, legs), end = ' ')