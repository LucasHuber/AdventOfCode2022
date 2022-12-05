def get_value(char: str) -> int:
    if char >= 'a' and char <= 'z':
        return ord(char) - 96
    elif char >= 'A' and char <= 'Z':
        return ord(char) - 38

file = open("03/input.txt")

lines = file.readlines()
sum = 0

# for line in lines:
#     line = line.replace("\n", "")
#     string1, string2 = line[:len(line)//2], line[len(line)//2:]
    
#     common = "".join(set(string1).intersection(string2))
    
#     sum += get_value(common)

i = 0
while i < len(lines):
    string1 = lines[i].replace("\n", "")
    string2 = lines[i+1].replace("\n", "")
    string3 = lines[i+2].replace("\n", "")
    
    first_common = "".join(set(string1).intersection(string2))
    
    real_common = "".join(set(first_common).intersection(string3))
    
    sum += get_value(real_common)
    
    i += 3
   
    
print(sum)

