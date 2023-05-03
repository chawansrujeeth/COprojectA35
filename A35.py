def opcode(c):
    if c == 'add':
        return '00000'
    elif c == 'sub':
        return '00001'
    elif c == 'mov1':
        return '00010'
    elif c == 'mov2':
        return '00011'
    elif c == 'ld':
        return '00100'
    elif c =='st':
        return '00101'
    elif c == 'mul':
        return '00110'
    elif c == 'div':
        return '00111'
    elif c == 'rs':
        return '01000'
    elif c == 'ls':
        return '01001'
    elif c == 'xor':
        return '01010'
    elif c == 'or':
        return '01011'
    elif c == 'and':
        return '01100'
    elif c == 'not':
        return '01101'
    elif c == 'cmp':
        return '01110'
    elif c == 'jmp':
        return '01111'
    elif c == 'addf':
        return '10000'
    elif c == 'subf':
        return '10001'
    elif c == 'jlt':
        return '11100'
    elif c == 'jgt':
        return '11101'
    elif c == 'je':
        return '11111'
    elif c == 'hlt':
        return '11010'
def reg_code(c):
    if c == 'R0':
        return '000'
    elif c == 'R1':
        return '001'
    elif c == 'R2':
        return '010'
    elif c == 'R3':
        return '011'
    elif c == 'R4':
        return '100'
    elif c == 'R5':
        return '101'
    elif c == 'R6':
        return '110'
    elif c == 'flag':
        return '111'
#code to convert inst to array
with open('instructions', 'r') as f:
    lines = f.readlines()
for i in range(0,len(lines) - 1):
    lines[i] = lines[i][0:-1]
for i  in range(0,len(lines)):
    lines[i] = lines[i].split(' ')
print(lines)
num = 0
solutions = []
variables = []

while 1:
    code = ''
    if lines[num][0] == 'hlt':
        code += opcode('hlt')
        code += '0' * 11
        solutions.append(code)
        break
    elif lines[num][0] == 'var':
        variables.append(lines[num][1])
    elif lines[num][0] == 'add' or lines[num][0] == 'sub' :
        code += opcode(lines[num][0])
        code += '00'
        code += reg_code(lines[num][1])
        code += reg_code(lines[num][2])
        code += reg_code(lines[num][3])
        solutions.append(code)
    num += 1

print(solutions)
