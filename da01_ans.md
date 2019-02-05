# CS 1200 SP19 Homework 1
## Jack Kufa


### 1.
#### a)
1. H
2. 0
3. Hell
4. loC
5. 0021SC olleH
6. Hello CS1200
7. Hel
8. 2S

#### b)
`daynumber(2)` will display "Today is Tuesday!"

#### c)
xx xxxx yy yyyyy

#### d)
a is: `['Good', 2, 7]`

b is:`[['Good', 2, 7], ['Good', 2, 7]]`

#### e)
"3 3"


### 2.
```python
x = 2
y = 1/x
a = []

while x <= 15:
  print(1/x)
  a += [1/x]
  x += 1
print("the sum is: ", sum(a))
```

### 3.
```python
def pickWord(string):
    newstring = string[1:] + string[0] + "ay"
    return newstring
```

### 4.

#### a)
```python
def isTriangle(a, b, c):
    if (a + b) < c or (a + c) < b or (b + c) < a:
        print("no")
    else:
        print("yes")
```
#### b)
```python
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
```


### 5.
```python
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
```