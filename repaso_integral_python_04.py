# ============================================
# REPASO INTEGRAL DE PYTHON
# Material de consulta - todo lo visto hasta ahora
# ============================================

# --------------------------------------------
# 1. VARIABLES Y TIPOS DE DATO
# --------------------------------------------
nombre = "Juan"          # texto (string)
edad = 25                 # numero entero (int)
estatura = 1.75            # numero decimal (float)
es_estudiante = True        # booleano (True o False)

print(nombre, edad, estatura, es_estudiante)


# --------------------------------------------
# 2. INPUT Y CONVERSION DE TIPOS
# input() siempre devuelve texto, por eso hay que 
# convertir si vamos a hacer calculos
# --------------------------------------------
edad_texto = input("Cuantos anios tienes?: ")   # queda como texto
edad_numero = int(input("Cuantos anios tienes?: "))    # se convierte a entero
precio = float(input("Precio: "))                # se convierte a decimal


# --------------------------------------------
# 3. F-STRINGS - insertar variables dentro de un texto
# --------------------------------------------
print(f"Hola {nombre}, tienes {edad} anios")


# --------------------------------------------
# 4. CONDICIONALES
# --------------------------------------------
edad = 20

if edad < 12:
    print("Eres nino")
elif edad < 18:
    print("Eres adolescente")
else:
    print("Eres adulto")

# and: se cumple SOLO si AMBAS condiciones son verdaderas
if edad >= 18 and es_estudiante:
    print("Eres adulto y estudiante")

# or: se cumple si AL MENOS UNA condicion es verdadera
if edad < 12 or edad > 65:
    print("Aplica descuento especial")


# --------------------------------------------
# 5. WHILE - repetir mientras se cumpla una condicion
# --------------------------------------------
contador = 0
while contador < 3:
    print(f"Vuelta numero {contador}")
    contador = contador + 1


# --------------------------------------------
# 6. LISTAS - guardar varios datos juntos
# --------------------------------------------
frutas = ["manzana", "pera", "uva"]

print(frutas[0])         # accede al primer elemento -> "manzana"
frutas.append("sandia")   # agrega al final
print(len(frutas))        # cuenta cuantos elementos hay
print(sum([10, 20, 30]))  # suma los elementos (solo con numeros)


# --------------------------------------------
# 7. FOR - recorrer una lista
# --------------------------------------------
for fruta in frutas:
    print(fruta)

# enumerate() da la posicion y el contenido a la vez
for i, fruta in enumerate(frutas):
    print(i, fruta)


# --------------------------------------------
# 8. LIST COMPREHENSION - forma corta de crear listas
# --------------------------------------------
numeros = [1, 2, 3, 4, 5]

# forma larga
cuadrados_largo = []
for n in numeros:
    cuadrados_largo.append(n**2)

# forma corta (hace lo mismo)
cuadrados_corto = [n**2 for n in numeros]

# con condicion
pares = [n for n in numeros if n % 2 == 0]


# ============================================
# EJERCICIOS PARA PRACTICAR
# ============================================

# Ejercicio 1 (variables + f-strings): 
# Crea variables con tu nombre, tu edad y tu ciudad. 
# Imprime una frase usando las 3 en un f-string.


# Ejercicio 2 (condicionales): 
# Pide una nota (0 a 5) y di si "Aprobado" (>=3) o "Reprobado".


# Ejercicio 3 (while): 
# Pide numeros al usuario uno por uno hasta que escriba "salir".
# Al final, muestra cuantos numeros escribio.


# Ejercicio 4 (listas + for): 
# Crea una lista con 5 precios. Recorrela e imprime cuales 
# son mayores a 20000.


# Ejercicio 5 (list comprehension): 
# A partir de una lista de edades, crea una nueva lista solo 
# con las edades mayores de edad (18+).
