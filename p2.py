x = 2
y = 1/x
a = []

while x <= 15:
  print(1/x)
  a += [1/x]
  x += 1
print("the sum is: ", sum(a))