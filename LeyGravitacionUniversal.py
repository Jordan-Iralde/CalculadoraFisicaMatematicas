import math

print("Inicio")
m1 = 0
m2 = 0
G = 6.674 * 10e-11
#Programa 1
#m1 = 10                    
#m2 = 20                    

#Programa 2
#m1 = 5.972 * 10**24        
#m2 = 1000                  

#Programa 3(Error en datos)
#m1 = 2 * 10 ** 30         
#m2 = 3 * 10 ** 30          

#Programa 4
def CalcularFuerza():
    m1 = 5.972 * 10 ** 24
    m2 = 0
    r  = 10 ** 11
    F= G *(m1 * m2)/r**2
    return F

m1 = 5.972 * 10 ** 24
r = 1 * 10 ** 11
F= 3.984 * 10 ** -8
m2 = F * r **2/ G * m1

print(m2)
#print(f"{F}+N")
print("Fin")