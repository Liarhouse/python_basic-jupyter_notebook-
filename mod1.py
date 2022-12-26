# mod1.py

def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b
    
def mul(a, b):
    return a * b
    
def div(a, b):
    if b == 0:
        b = 1
    return a / b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 3))