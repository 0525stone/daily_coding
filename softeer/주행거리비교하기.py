import sys

input = sys.stdin.readline()
numbers = [int(i) for i in input.split()]

if numbers[0]>numbers[1]:
    answer = "A"
elif numbers[0]<numbers[1]:
    answer = "B"
else:
    answer = "same"
print(answer)