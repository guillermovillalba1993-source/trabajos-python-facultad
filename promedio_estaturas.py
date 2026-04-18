# a) Función para ingresar estaturas con validación simple
def ingresar_estaturas(cantidad):
    lista_estaturas = []
    for x in range(cantidad):
        estatura = float(input(f"Ingrese la estatura {x + 1}: "))
        # Validamos que la estatura sea razonable
        while estatura < 0.5 or estatura > 2.5:
            print("Estatura no válida. Intente de nuevo.")
            estatura = float(input(f"Ingrese la estatura {x + 1}: "))
        lista_estaturas.append(estatura)
    return lista_estaturas

# b) Función para el promedio
def obtener_promedio(lista):
    suma_total = 0
    for valor in lista:
        suma_total = suma_total + valor
    promedio = suma_total / len(lista)
    return promedio

# c) Función para contar personas más altas o iguales al promedio
def contar_altos_que_promedio(lista, prom):
    contador = 0
    for valor in lista:
        if valor >= prom:
            contador = contador + 1
    return contador

# d) Función para contar personas más bajas que el promedio
def contar_bajos_que_promedio(lista, prom):
    contador = 0
    for valor in lista:
        if valor < prom:
            contador = contador + 1
    return contador

# e) Función para obtener alturas superiores a un parámetro
def filtrar_superiores(lista, limite):
    nueva_lista = []
    for valor in lista:
        if valor > limite:
            nueva_lista.append(valor)
    return nueva_lista

# f) Función para obtener alturas en un rango (min, max)
def filtrar_rango(lista, minimo, maximo):
    nueva_lista = []
    for valor in lista:
        if valor >= minimo and valor <= maximo:
            nueva_lista.append(valor)
    return nueva_lista

# --- Programa Principal ---
n = int(input("¿Cuántas estaturas vas a cargar? "))
mis_estaturas = ingresar_estaturas(n)

promedio_general = obtener_promedio(mis_estaturas)
print("-" * 30)
print(f"El promedio es: {promedio_general:.2f}")

sobre_prom = contar_altos_que_promedio(mis_estaturas, promedio_general)
bajo_prom = contar_bajos_que_promedio(mis_estaturas, promedio_general)

print(f"Personas más altas o iguales al promedio: {sobre_prom}")
print(f"Personas más bajas que el promedio: {bajo_prom}")

# Ejemplo de los puntos e y f
umbral = 1.85
print(f"Alturas mayores a {umbral}: {filtrar_superiores(mis_estaturas, umbral)}")

rango_alturas = filtrar_rango(mis_estaturas, 1.60, 1.80)
print(f"Alturas entre 1.60 y 1.80: {rango_alturas}")