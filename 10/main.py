a = input("Enter a: ")
b = input("Enter b: ")

def middleret(a,b):
    return f'{a[0:len(a)//2]}{b}{a[len(a)//2:]}'

print(middleret(a,b))