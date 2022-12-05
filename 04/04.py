file = open("04/input.txt")

lines = file.readlines()
count = 0

for line in lines:
    abcd = line.split(",")
    ab = abcd[0].split("-")
    s1 = int(ab[0])
    e1 = int(ab[1])
    cd = abcd[1].split("-")
    s2 = int(cd[0])
    e2 = int(cd[1])
    
    print("{} {} {} {}".format(s1, e1, s2, e2))
    
    # if ((int(s1) <= int(s2) and e1 >= e2) or (s2 <= s1 and e2 >= e1)):
    #     count += 1
    #     print("counted")
    
    if (not (e1 < s2 or e2 < s1)):
        count += 1
        print("counted")
        
print(count)