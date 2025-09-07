# a,b,c = map(int, input().split())
a, b, c = [int(input()) for _ in range(3)]
num = [0] * 10
result = list(str(a*b*c))

for i in result:
    num[int(i)] += 1
for i in range(10):
    print(num[i])