import time
def module_sleep(parameters):
    amt = float(parameters[0])
    time.sleep(amt)
    return 
def module_check(command):
    if command == "slp":
        return (True,module_sleep)