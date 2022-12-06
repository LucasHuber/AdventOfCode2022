file = open("04/input.txt")

lines = file.readlines()
count1 = 0
count2 = 0

for line in lines:
    abcd = line.split(",")
    ab = abcd[0].split("-")
    s1 = int(ab[0])
    e1 = int(ab[1])
    cd = abcd[1].split("-")
    s2 = int(cd[0])
    e2 = int(cd[1])
    
    if ((s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)):
        count1 += 1
    
    if (not (e1 < s2 or e2 < s1)):
        count2 += 1

print("Part One: {}".format(count1))
print("Part Two: {}".format(count2))