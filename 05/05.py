file = open("05/input.txt")

stack = [[0]]*10

stack[1] = ['B', 'W', 'N']
stack[2] = ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B']
stack[3] = ['Q', 'H', 'Z', 'W', 'R']
stack[4] = ['W', 'D', 'V', 'J', 'Z', 'R']
stack[5] = ['S', 'H', 'M', 'B']
stack[6] = ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B']
stack[7] = ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S']
stack[8] = ['W', 'S', 'F', 'J', 'G', 'Q', 'B']
stack[9] = ['Z', 'W', 'M', 'S', 'C', 'D', 'J']

lines = file.read().split("\n")

for line in lines:
    instr = [int(s) for s in line.split() if s.isdigit()]
    imove, ifrom, ito = instr[0], instr[1], instr[2]
    
    for i in range(imove):
        stack[ito].append(stack[ifrom].pop())

output = ""
for i in range(1, 10):
    output += stack[i].pop()
    
print("Part One: {}".format(output))

stack[1] = ['B', 'W', 'N']
stack[2] = ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B']
stack[3] = ['Q', 'H', 'Z', 'W', 'R']
stack[4] = ['W', 'D', 'V', 'J', 'Z', 'R']
stack[5] = ['S', 'H', 'M', 'B']
stack[6] = ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B']
stack[7] = ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S']
stack[8] = ['W', 'S', 'F', 'J', 'G', 'Q', 'B']
stack[9] = ['Z', 'W', 'M', 'S', 'C', 'D', 'J']

for line in lines:
    instr = [int(s) for s in line.split() if s.isdigit()]
    imove, ifrom, ito = instr[0], instr[1], instr[2]
    
    temp = []
    for i in range(imove):
        temp.append(stack[ifrom].pop())
    for i in range(imove):
        stack[ito].append(temp.pop())

output = ""
for i in range(1, 10):
    output += stack[i].pop()
    
print("Part Two: {}".format(output))