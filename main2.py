import math

def calcular_area_cuadrado():
    # calcular el area del cuadrado
    a = float(input("Ingrese el lado del cuadrado: "))
    area_cuadrado = a * a # también puede ser a ** 2
    print(f"El area del cuadrado es: {area_cuadrado}")

calcular_area_cuadrado()

def calcular_area_rectangulo():
    # calcular el area del rectangulo
    b = float(input("Ingrese la base del rectangulo: "))
    h = float(input("Ingrese la altura del rectangulo: "))
    area_rectangulo = b * h
    print(f"El area del rectangulo es: {area_rectangulo}")

calcular_area_rectangulo()

def calcular_area_triangulo():
    # calcular el area del triangulo
    b = float(input("Ingrese la base del triangulo: "))
    h = float(input("Ingrese la altura del triangulo: "))
    area_triangulo = (b * h) / 2
    print(f"El area del triangulo es: {area_triangulo}")

calcular_area_triangulo()

def calcular_area_paralelogramo():
    # calcular el area del paralelogramo
    b = float(input("Ingrese la base del paralelogramo: "))
    h = float(input("Ingrese la altura del paralelogramo: "))
    area_paralelogramo = b * h
    print(f"El area del paralelogramo es: {area_paralelogramo}")

calcular_area_paralelogramo()

def calcular_area_trapecio():
    # calcular el area del trapecio
    B = float(input("Ingrese la base mayor del trapecio: "))
    b = float(input("Ingrese la base menor del trapecio: "))
    h = float(input("Ingrese la altura del trapecio: "))
    area_trapecio = ((B + b) / 2) * h
    print(f"El area del trapecio es: {area_trapecio}")

calcular_area_trapecio()

def calcular_area_circulo():
    # calcular el area del circulo
    r = float(input("Ingrese el radio del circulo: "))
    area_circulo = math.pi * r ** 2
    print(f"El area del circulo es: {area_circulo}")

calcular_area_circulo()

def calcular_area_rombo():
    # Calcular el area del rombo
    D = float(input("Ingrese la diagonal mayor del rombo: "))
    d = float(input("Ingrese la diagonal menor del rombo: "))
    area_rombo = (D * d) / 2
    print(f"El area del rombo es: {area_rombo}")

calcular_area_rombo()

def calcular_area_poligono_regular():
    # Calcular el area del poligono regular
    P = float(input("Ingrese el perimetro del poligono regular: "))
    a = float(input("Ingrese el apotema del poligono regular: "))
    area_poligono = (P * a) / 2
    print(f"El area del poligono regular es: {area_poligono}")

calcular_area_poligono_regular()

def calcular_volumen_cubo():
    #Calcular el volumen del cubo
    l = float(input("Ingrese el lado o arista del cubo: "))
    volumen_cubo = l ** 3
    print(f"El volumen del cubo es: {volumen_cubo}")

calcular_volumen_cubo()

def calcular_volumen_paralelepipedo():
    #Calcular el volumen del paralelepipedo
    l = float(input("Ingrese el largo del paralelepipedo: "))
    b = float(input("Ingrese el ancho o base del paralelepipedo: "))
    h = float(input("Ingrese la altura del paralelepipedo: "))
    volumen_paralelepipedo = l * b * h
    print(f"El volumen del paralelepipedo es: {volumen_paralelepipedo}")

calcular_volumen_paralelepipedo()

def calcular_volumen_cilindro():
    #Calcular el volumen del cilindro
    r = float(input("Ingrese el radio de la base del cilindro: "))
    h = float(input("Ingrese la altura del cilindro: "))
    volumen_cilindro = math.pi * r**2 * h
    print(f"El volumen del cilindro es: {volumen_cilindro}")

calcular_volumen_cilindro()

def calcular_volumen_esfera():
    #Calcular el volumen de la esfera
    r = float(input("Ingrese el radio de la esfera: "))
    volumen_esfera = (4/3) * math.pi * r ** 3
    print(f"El volumen de la esfera es: {volumen_esfera}")

calcular_volumen_esfera()

def calcular_volumen_cono():
    #Calcular el volumen del cono
    r = float(input("Ingrese el radio de la base del cono: "))
    h = float(input("Ingrese la altura del cono: "))
    volumen_cono = (1/3) * math.pi * r**2 * h
    print(f"El volumen del cono es: {volumen_cono}")

calcular_volumen_cono()


