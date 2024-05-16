import modules.ifmodule
import modules.timemodule

def interpret_line(line,production_index):
    i = 0
    global code
    global pointer_indexes
    global production_lines
    pointer_index = pointer_indexes[production_index]
    production_line = production_lines[production_index]
    while i < len(line):
        cmd = line[i]
        if cmd == ">":
            pointer_index += 1
            if pointer_index > len(production_line)-1:
                production_line.append(0)
        elif cmd == "<":
            pointer_index -= 1
        elif cmd == "+":
            production_line[pointer_index] += 1
        elif cmd == "-":
            production_line[pointer_index] -= 1
        elif cmd == "*":
            production_line[pointer_index] *= production_line[pointer_index+1]
        elif cmd == "/":
            production_line[pointer_index] /= production_line[pointer_index+1]
        elif cmd == "?":
            if line[i+1] == "n":
                print(str(production_line[pointer_index]),end="")
            elif line[i+1] == "c":
                print(chr(production_line[pointer_index]),end="")
            elif line[i+1] == "?":
                temp = False
                cont = line[i+2:]
                for j in range(len(cont)):
                    if cont[j] == "|" and not temp:
                        break
                    elif cont[j] == "\\":
                        if cont[j+1] == "|":
                            print(cont[j+1],end="")
                        elif cont[j+1] == "n":
                            print("\n",end="")
                        elif cont[j+1] == "\\":
                            print("\\",end="")
                        temp = True
                    if not temp and not (cont[j-1] == "\\" and not cont[j-2] == "\\"):
                        print(cont[j],end="")
                    else:
                        temp = False
                    i += 1
            i += 1
        elif cmd == ",":
            if line[i+1] == "u":
                if line[i+2] == "c":
                    s = input()
                    for j in range(len(s)):
                        if len(production_line)-pointer_index < len(s):
                            while len(production_line)-pointer_index < len(s):
                                production_line.append(0)
                        production_line[pointer_index+j] = ord(s[j])
                elif line[i+2] == "n":
                    num = int(input())
                    if line[i+3] == "#":
                        production_line[pointer_index] = num
                    elif line[i+3] == "+":
                        production_line[pointer_index] += num
                    elif line[i+3] == "-":
                        production_line[pointer_index] -= num
                    elif line[i+3] == "*":
                        production_line[pointer_index] *= num
                    elif line[i+3] == "/":
                        production_line[pointer_index] /= num
                elif line[i+2] == "f":
                    num = float(input())
                    if line[i+3] == "#":
                        production_line[pointer_index] = num
                    elif line[i+3] == "+":
                        production_line[pointer_index] += num
                    elif line[i+3] == "-":
                        production_line[pointer_index] -= num
                    elif line[i+3] == "*":
                        production_line[pointer_index] *= num
                    elif line[i+3] == "/":
                        production_line[pointer_index] /= num
                i += 2
            else:
                num = ""
                if line[i+1] == "c":
                    cont = line[i+3:]
                    for j in range(len(cont)):
                        if cont[j] == "|":
                            break
                        try:
                            production_line[pointer_index+j] = ord(cont[j])
                        except:
                            production_line.append(ord(cont[j]))
                else:
                    cont = line[i+2:]
                    for j in range(len(cont)):
                        if cont[j] != "|":
                            num += cont[j]
                        else:
                            break
                if num == "":
                    pass
                elif "." in num:
                    num = float(num)
                else:
                    num = int(num)
                if num == "":
                    pass
                elif line[i+1] == "#":
                    production_line[pointer_index] = num
                elif line[i+1] == "+":
                    production_line[pointer_index] += num
                elif line[i+1] == "-":
                    production_line[pointer_index] -= num
                elif line[i+1] == "*":
                    production_line[pointer_index] *= num
                elif line[i+1] == "/":
                    production_line[pointer_index] /= num
                if num == "":
                    i += j
                else:
                    i += j + 2
                
        elif cmd == "[":
            if line[i+1] == "0":
                cont = line[i+2:]
                extra = 0
                end = production_line[pointer_index]
                for j in range(len(cont)):
                    if cont[j] == "[":
                        extra += 1
                    elif cont[j] == "]" and extra > 0:
                        extra -= 1
                    elif cont[j] == "]" and extra <= 0:
                        endpoint = j + i + 2
                repeat = line[i+2:endpoint]
                while end != 0:
                    end = interpret_line(repeat,production_index)
            else:
                iterations = ""
                cont = line[i+1:]
                for j in range(len(line[i+1:])):
                        if cont[j] != "|":
                            iterations += cont[j]
                        else:
                            break
                iterations = int(iterations)
                cont = line[i+len(str(iterations))+1:]
                extra = 0
                for j in range(len(cont)):
                    if cont[j] == "[":
                        extra += 1
                    elif cont[j] == "]" and extra > 0:
                        extra -= 1
                    elif cont[j] == "]" and extra <= 0:
                        endpoint = j + i + 2
                repeat = line[i+len(str(iterations))+2:endpoint+1]
                for _ in range(iterations):
                    interpret_line(repeat,production_index)
            i = endpoint
        elif cmd == "@":
            lineN = ""
            cont = line[i+1:]
            for j in range(len(cont)):
                if cont[j] != "|":
                    lineN += cont[j]
                else:
                    break
                i += 1
            lineN = int(lineN)
            interpret_line(code[lineN],lineN)
            i += 1
        elif cmd == "¬":
            command = ""
            cont = line[i+1:]
            parameters = []
            t = 0
            for j in range(len(line[i+1:])):
                if cont[j] != "|" and t == 0:
                    command += cont[j]
                elif cont[j] != "|":
                    parameters[t-1] += cont[j]
                elif cont[j] == "|":
                    if t > 0:
                        if parameters[t-1] == "x":
                            parameters[t-1] = production_line[pointer_index]
                    if cont[j+1] == "|":
                        break
                    t += 1
                    parameters.append("")
            i += j+1
            for module in modulelist:
                if module(command):
                    rt = module(command)[1](parameters)
                    if rt:
                        interpret_line(rt,production_index)
        production_lines[production_index] = production_line
        pointer_indexes[production_index] = pointer_index
        while pointer_index > len(production_line)-1:
            production_line.append(0)
        i += 1
    return production_line[pointer_index]

def main():
    global modulelist
    modulelist = []
    modulelist.append(modules.timemodule.module_check)
    modulelist.append(modules.ifmodule.module_check)
    global pointer_indexes
    global code
    global production_lines
    with open("code.txt","r") as file:
        code = [line for line in file.readlines()]
    pointer_indexes = [0]*len(code)
    production_lines = [[0]]*len(code)
    interpret_line(code[0],0)
