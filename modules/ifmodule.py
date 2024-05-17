def greater_than(parameters):
    a = float(parameters[0])
    b = float(parameters[1])
    if a > b:
        return parameters[2]
    return
def less_than(parameters):
    a = float(parameters[0])
    b = float(parameters[1])
    if a < b:
        return parameters[2]
    return
def equal_to(parameters):
    a = parameters[0]
    b = parameters[1]
    if a == b:
        return parameters[2]
    return
def not_equal_to(parameters):
    a = parameters[0]
    b = parameters[1]
    if a != b:
        return parameters[2]
    return
def module_check(command):
    if command == ">":
        return (True,greater_than)
    elif command == "<":
        return (True,less_than)
    elif command == "=":
        return (True,equal_to)
    elif command == "!=":
        return (True,not_equal_to)