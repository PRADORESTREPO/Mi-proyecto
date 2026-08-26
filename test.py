inventario = {}

while True:
    nombre = input("Ingresa el producto (o escribe 'salir' para terminar): ").strip().lower()
    
    if nombre == "salir":
        break
        
    cantidad = int(input(f"¿Cuántos de '{nombre}' deseas agregar?: "))
    
    # Si el producto ya existe en el diccionario, sumamos la cantidad
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        # Si no existe, lo agregamos por primera vez
        inventario[nombre] = cantidad

    
    
    
    print(f"-> Ahora tienes {inventario[nombre]} unidad(es) de '{nombre}'.\n")

print("\n--- INVENTARIO FINAL ---")


for producto, cantidad in inventario.items():
    print(f"- {producto.capitalize()}: {cantidad}")