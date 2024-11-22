def calcularCalor(m, c, vt):
    calculo = m * c * vt
    if kcal_cal == 'kcal': 
        print(f"Calculo Calor = {calculo} kcal")
    else:
        print(f"Calculo Calor = {calculo} cal")

def calcularVT(Q, m, c):
    calculo = Q / (m * c)
    print(f"variacion de Temperatura = {calculo} °C")
    return calculo

def calcularMasa(Q, c, vt):
    calculo = Q / (c * vt) 
    if kcal_cal == 'kcal': 
        print(f"masa es igual a = {calculo} kg")
    else:
        print(f"masa es igual a = {calculo} g")


def calcularTF():
    To = float(input("Ingrese valor de Temperatura inicial: "))
    calculo = calcularVT()
    Tf = To + calculo
    print(f"Temperatura final es {Tf}")
    return Tf

def calcularTo():
    Tf = float(input("Ingrese valor de Temperatura final: "))
    calculo = calcularVT()
    To = Tf + calculo
    print(f"Temperatura inicial es {To}")
    return print(f"Temperatura incial es = {To}")

while True:
    eleccion = int(input("Ingrese su eleccion: "))

    c  = float(input("Valor c: "))
    kcal_cal = input("Es kcal o es cal? ")

    '''
    Un trozo de metal de 100 gramos se calienta desde 20°C hasta 100°C. Luego, se sumerge
    en un recipiente con 50 gramos de agua a 20° C. Si la capacidad calorífica del agua es
    1kcal/kg °C. ¿Cuánta energía se necesita para calentar el agua?
    '''
    if eleccion == 1:
        print("Calcular Calor")
        m  = float(input("Valor m: ")) 
        vt = float(input("Valor vt: "))
        calcularCalor(m, c, vt)
    elif eleccion == 2:
        print("Calcular Masa")
        Q  = float(input("Valor Q: "))
        vt = float(input("Valor vt: "))
        calcularMasa(Q, c, vt)
    elif eleccion == 3:
        print("Calcular Variacion de Temperatura")
        Q  = float(input("Valor Q: "))
        m  = float(input("Valor m: "))
        calcularVT(Q, m, c)
    elif eleccion == 4:
        print("Calcular TF")
        calcularTF()
    else:
        print("Calcular To")
        calcularTo()
