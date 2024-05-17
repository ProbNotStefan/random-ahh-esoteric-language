import math
def squarert(parameters):
    num = float(parameters[0])
    return f",#{round(math.sqrt(num),5)}|"
def cubert(parameters):
    num = float(parameters[0])
    return f",#{round(math.cbrt(num),5)}|"
def factorial(parameters):
    num = int(parameters[0])
    return f",#{math.factorial(num)}|"
def degrees(parameters):
    num = float(parameters[0])
    return f",#{round(math.degrees(num),5)}|"
def radians(parameters):
    num = float(parameters[0])
    return f",#{round(math.radians(num),5)}|"
def floor(parameters):
    num = float(parameters[0])
    return f",#{math.floor(num)}|"
def ceil(parameters):
    num = float(parameters[0])
    return f",#{math.ceil(num)}|"
def roundnum(parameters):
    num = float(parameters[0])
    x = int(parameters[1])
    return f",#{round(num,x)}|"
def sin(parameters):
    num = float(parameters[0])
    return f",#{round(math.sin(num),5)}|"
def cos(parameters):
    num = float(parameters[0])
    return f",#{round(math.cos(num),5)}|"
def tan(parameters):
    num = float(parameters[0])
    return f",#{round(math.tan(num),5)}|"
def asin(parameters):
    num = float(parameters[0])
    return f",#{round(math.asin(num),5)}|"
def acos(parameters):
    num = float(parameters[0])
    return f",#{round(math.acos(num),5)}|"
def atan(parameters):
    num = float(parameters[0])
    return f",#{round(math.atan(num),5)}|"
def sinh(parameters):
    num = float(parameters[0])
    return f",#{round(math.sinh(num),5)}|"
def cosh(parameters):
    num = float(parameters[0])
    return f",#{round(math.cosh(num),5)}|"
def tanh(parameters):
    num = float(parameters[0])
    return f",#{round(math.tanh(num),5)}|"
def pi(parameters):
    return f",#{math.pi}|"


def module_check(command):
    if command == "sqrt":
        return (True,squarert)
    elif command == "cbrt":
        return (True,cubert)
    elif command == "fct":
        return (True,factorial)
    elif command == "deg":
        return (True,degrees)
    elif command == "rad":
        return (True,radians)
    elif command == "flr":
        return (True,floor)
    elif command == "ceil":
        return (True,ceil)
    elif command == "round":
        return (True,roundnum)
    elif command == "sin":
        return (True,sin)
    elif command == "cos":
        return (True,cos)
    elif command == "tan":
        return (True,tan)
    elif command == "asin":
        return (True,asin)
    elif command == "acos":
        return (True,acos)
    elif command == "atan":
        return (True,atan)
    elif command == "sin":
        return (True,sinh)
    elif command == "cosh":
        return (True,cosh)
    elif command == "tanh":
        return (True,tanh)
    elif command == "pi":
        return (True,pi)
    
    
        