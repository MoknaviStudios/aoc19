import math
sum = 0
input = open("input.txt", "r")

for line in input:
    line = int(line)
    line = math.floor(line / 3) - 2
    sum += line

print(sum)

input.close()