#string = input("enter a string: ")
#print(string[1:] + string[0] + "ay")

#string = input("enter a string: ")

def pickWord(string):
    head = string[0]
    newstring = string[1:] + string[0] + "ay"
    return newstring

def main():
    s = input("Enter a string: ")
    print(newstring(s))