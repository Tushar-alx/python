import shutil 

width = shutil.get_terminal_size().columns

# 1	 Without return value without argument

def printLine():
    print('_' * width)

# 2	Without return value with argument 

def printMessage(message):  
    print(message.center(width))

# 3	 With return value without argument

def getPi():
    pi = 22/7
    return pi 

printLine() 
printMessage('Hello')
printLine()

pi = getPi()
print("pi =",pi)