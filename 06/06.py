file = open("06/input.txt")

line = file.read().replace("\n", "")
numb = 0

for i in range(4, len(line)):
    if (len(set(line[i-4:i])) == 4):
        numb = i
        break
    
print("First Part: {}".format(numb))

for i in range(14, len(line)):
    if (len(set(line[i-14:i])) == 14):
        numb = i
        break
    
print("Second Part: {}".format(numb))