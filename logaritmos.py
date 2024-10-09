from calendar import c
from re import T, sub
#a y c Existen en los Reales Y a y c > 0
#log 8(1) = 0             ====>     8 ** 0 = 1
print("inicio")

def log(a, b):
        #log a (b) = C
        #a ** c = b
        # Y = log sub(a) (b) = C    => (a) ** c = b

    c = 0
    while a > 0:
        
        if a ** c == b:
            print(f"{a} ** {c} = {b} \n")
            break
        else:
            c = c + 1
            print(f"Fallo, c es: {c}")

while True:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    print(8 ** 0)
    log(a, b)

print("fin")