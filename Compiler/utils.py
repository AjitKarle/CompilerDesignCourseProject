def isoperator(s: str):
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '/' or s[i] == '-' or s[i] == '*':
            return True
    return False


def isIfElse(s: str):
    for i in range(len(s)):
        if s[i] == '>' or s[i] == '<' or s[i] == '=' or s[i] == '!':
            return True

    return False


def checkIfElse(s: str, vars: dict):
    index = s.find("IF")
    index2 = s.find("THEN", index + 1)
    index3 = s.find("ELSE", index2 + 1)

    condition = s[index + 2: index2].strip()
    ifRes = s[index2 + 4:index3].strip()
    elseRes = s[index3 + 4:].strip()

    left = ''
    right = ''
    op = '>='

    ifRes = checkCalculation(ifRes, vars) if isoperator(ifRes) else vars[ifRes]
    elseRes = checkCalculation(elseRes, vars) if isoperator(elseRes) else vars[elseRes]

    index = condition.find(">=")
    if (index == -1):
        index = condition.find(">")
        op = '>'
    if (index == -1):
        index = condition.find('<=')
        op = '<='
    if (index == -1):
        index = condition.find('<')
        op = '<'
    if (index == -1):
        index = condition.find('==')
        op = '=='
    if index == -1:
        index = condition.find('!=')
        op = '!='

    if index != -1:
        left_side = condition[0:index].strip()
        right_side = condition[index + len(op):].strip()

        if left_side in vars:
            left = vars[left_side]

        elif isoperator(left_side):
            left = checkCalculation(left_side, vars)

        else:
            left = left_side

        if right_side in vars:
            right = vars[right_side]
        elif isoperator(right_side):
            right = checkCalculation(right_side, vars)
        else:
            right = right_side

        if op == ">":
            return ifRes if float(left) > float(right) else elseRes
        elif op == '<':
            return ifRes if float(left) < float(right) else elseRes
        elif op == '<=':
            return ifRes if float(left) <= float(right) else elseRes
        elif op == '>=':
            return ifRes if float(left) >= float(right) else elseRes
        elif op == '==':
            return ifRes if float(left) == float(right) else elseRes
        elif op == '!=':
            return ifRes if float(left) != float(right) else elseRes

    return ""


def Replace(s, index1: int, index2: int, r: str):
    k = 0
    temp = s[:index1]
    for i in range(index1, index1 + len(r)):
        s.replace(s[i], r[k], 1)
        k += 1
    return s


def checkCalculation(s: str, vars: dict):
    intCalc = False
    left = ''
    right = ''

    index = s.find('(')
    while index != -1:
        index2 = s.rfind(')')
        temp = s[:index]
        temp += checkCalculation(s[index + 1:index2], vars)
        temp += s[index2 + 1:]
        s = temp
        # s = Replace(s, index, index2 + 1, checkCalculation(s[index + 1:index2], vars))
        index = s.find(s, index + 1)

    op = '+'
    index = s.find("+")
    if (index == -1):
        index = s.find('-')
        op = '-'
    if (index == -1):
        index = s.find('/')
        op = '/'
    if (index == -1):
        index = s.find('*')
        op = '*'

    if index != -1:
        left_side = s[0:index].strip()
        right_side = s[index + 1:].strip()

        if left_side in vars:
            left = vars[left_side]
        elif isoperator(left_side):
            left = checkCalculation(left_side, vars)
        else:
            left = left_side

        if right_side in vars:
            right = vars[right_side]
        elif isoperator(right_side):
            right = checkCalculation(right_side, vars)
        else:
            right = right_side

        if left.find('.') == -1 and right.find('.') == -1:
            intCalc = True

        if (op == '+'):
            return str(int(left) + int(right) if intCalc else float(left) + float(right))
        elif op == '-':
            return str(int(left) - int(right) if intCalc else float(left) - float(right))
        elif op == '*':
            return str(int(left) * int(right) if intCalc else float(left) * float(right))
        elif op == '/':
            return str(int(left) // int(right) if intCalc else float(left) // float(right))

    return s.strip()


def CheckLoop(s: str, vars: dict, key: str):
    if key not in vars:
        vars[key] = '0'

    index = s.find("TIMES")
    left = s[0:index].strip()

    count = int(s[index + 5:].strip())

    for i in range(count):
        vars[key] = checkIfElse(left, vars) if s.find('IF') != -1 else checkCalculation(left, vars)

    return ""


def checkVariable(s: str, vars: dict):
    index = s.find('=')

    if (index != -1):
        loopind = s.find("LOOP")
        key = s[loopind + 4:index].strip() if loopind != -1 else s[0:index].strip()
        if loopind != -1:
            CheckLoop(s[index + 1:], vars, key)
        else:
            vars[key] = checkIfElse(s[index + 1:], vars) if s.find("IF") != -1 else checkCalculation(s[index + 1:],
                                                                                                     vars)


def checkOutput(s: str):
    return True if s.find("OUT") != -1 else False

#print(output)
# output = vars[s[s.find("OUT") + 3:].strip()]
# print(output)

def mainCompiler(input):    
    vars = {}
    s = ""
    #file = open(input, 'r')
    lines = []
    if(input == "example1"): 
        lines = ["A = 10", "B= 20", "C = A+B", "OUT C"]
    elif(input == "example2"): 
        lines = ["A = 35.92", "B = 10.48", "C = A+B", "OUT C"]
    elif(input == "example3"): 
        lines = ["A = 4", "B = 20", "C = B / A", "OUT C"]
    elif(input == "example4"): 
        lines = ["A = 6.28", "B=92812", "C = B / A", "OUT C"]
    elif(input == "example5"): 
        lines = ["A = 6", "B = 2", "C = A + B", "D = B * A * C - 12 + B * C", "OUT D"]
    elif(input == "example6"): 
        lines = ["A=1", "B=2", "C=A+B", "D = (A + B * B ) * C + B", "OUT D"]
    elif(input == "example7"): 
        lines = ["A1 = 1", "B1 = 2", "A2 = IF A1 <= B1 THEN A1 ELSE B1", "OUT A2"]
    elif(input == "example8"): 
        lines = ["A = 1", "B = 2", "C = IF ( A + B * 12 ) <= 3 THEN A ELSE B", "OUT C"]
    else: 
        lines = ["A = 2", "B = 3", "LOOP C = C + A + B * 2 TIMES 4", "D = C * 4", "OUT D"]
    for line in lines:
        s = line
        if (checkOutput(line)):
            break
        checkVariable(line, vars)

    #file.close()
    output = vars[s[s.find("OUT") + 3:].strip()]
    return output

