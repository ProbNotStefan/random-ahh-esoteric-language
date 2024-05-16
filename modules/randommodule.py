import random
def randint(parameters):
    mn = int(parameters[0])
    mx = int(parameters[1])
    r = random.randint(mn,mx)
    return f",#{r}|"
def randrand(parameters):
    r = random.random()
    return f",#{r}|"
def randuni(parameters):
    mn = int(parameters[0])
    mx = int(parameters[1])
    r = random.uniform(mn,mx)
    return f",#{r}|"

def module_check(command):
    if command == "rint":
        return (True,randint)
    elif command == "rr":
        return (True,randint)
    elif command == "runi":
        return (True,randint)
