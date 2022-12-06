file = open("01/input.txt")

lines = file.readlines()
sum = 0
sums = []

for line in lines:
    if(line != "\n"):
        sum += int(line)
    else: 
        sums.append(sum)
        sum = 0
      
sums.sort(reverse=True)

print("Part One: {}".format(int(sums[0])))
print("Part Two: {}".format(int(sums[0]) + int(sums[1]) + int(sums[2])))