import math
def dist(point):
    return math.sqrt((point[0]-x)**2 + (point[1]-y)**2)
x, y =  map(int, input().split())
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
points.sort(key = dist)
for i in range(n):
    for j in range(2):
        print(points[i][j], end = ' ')
    print()