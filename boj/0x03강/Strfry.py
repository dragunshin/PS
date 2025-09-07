case = int(input())

for _ in range(case):
    first, second = map(str, input().split())
    first = sorted(first)
    second = sorted(second)
    if len(first) != len(second):
        print("Impossible")
        continue
    else: # now same length
        if first == second:
            print("Possible")
        else:
            print("Impossible")