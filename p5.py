def altDef(xs):
    result = xs[-1]
    xs = xs[:-1]
    xs.reverse()
    for x in xs:
        result = x - result
    return result
print(altDef([17,5,8,10]))