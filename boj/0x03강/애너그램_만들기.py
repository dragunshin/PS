# first = str(input())
# second = str(input())
# first = sorted(first)
# second = sorted(second)

# cnt = 0

# for ch in first:
#     if ch not in second:
#         # first.remove(ch)
#         del ch
#         cnt += 1
# for ch in second:
#     if ch not in first:
#         # second.remove(ch)
#         del ch
#         cnt += 1
        
# print(cnt)

from collections import Counter
first = input()
second = input()

first_counter = Counter(first)
second_counter = Counter(second)

diff = first_counter - second_counter
diff += second_counter - first_counter
print(sum(diff.values()))