def isTriangle(a, b, c):
    if (a + b) < c or (a + c) < b or (b + c) < a:
        print("no")
    else:
        print("yes")

def stickInput():
    a = int(input("enter triangle side 1: "))
    b = int(input("enter triangle side 2: "))
    c = int(input("enter triangle side 3: "))
    isTriangle(a, b, c)