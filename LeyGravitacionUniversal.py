import math

print("Inicio")

#Constantes
G = 6.674 * 10e-11

def Calculo():
    m1 = 0
    m2 = 0
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
        m1 = 5.972 * 10e24
        m2 = 0
        r  = 1 * 10e11
        F= G *(m1 * m2)/r**2
        return F

def CalcularGravedad():
    #Gravedad = (G * Masa)/radio**2
    #Luna = (Masa)7.349 * 10e22             (radio)1.738 * 10e6
    #Marte = (Masa)6.4185 * 10e23           (radio)3.396 * 10e6
    #Tierra = (Masa)5.972 * 10e24           (radio)6.371 * 10e6
    Masa = 1.9 * 10e27
    radio = 7.14 * 10e7

    Gravedad = (G * Masa)/radio ** 2
    GravedadGM = G * Masa
    print(f"{G} * {Masa} = {GravedadGM}")
    
    print(f"{radio} ** 2 = {radio ** 2}")
    
    print(f"{GravedadGM} / {radio ** 2} = {Gravedad}")
    
    #return print(f"Gravedad es {}")
    m1 = 5.972 * 10e24
    r = 1 * 10e11
    F= 3.984 * 10e-8
    m2 = F * r **2/ G * m1
    print(m2)
    #print(f"{F}+N")
m1 = 5.972 * 10e24
r = 1 * 10e11
F= 3.984 * 10e-8
m2 = F * r **2/ G * m1

#CalcularGravedad()
print("Fin")