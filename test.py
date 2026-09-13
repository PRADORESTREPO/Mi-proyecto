def mostrar_menu():
    print("\n====================SISTEMA INV PRADO.MAPR====================")
    print("1. Agregar producto")
    print("2. Ver stock")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("==============================================================")

def agregar_producto(inventario):
    while True:
        nombre_producto = input("\nIngrese el producto (o escriba 'salir' para finalizar): ").strip().lower()
        
        if nombre_producto == "salir":
            break
        
        try:
            cantidad = int(input(f"Ingrese cuántas unidades ingresa de '{nombre_producto.capitalize()}': "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            
            inventario[nombre_producto] = inventario.get(nombre_producto, 0) + cantidad
            print(f" Se agregaron {cantidad} unidad(es) de '{nombre_producto.capitalize()}'.")
        except ValueError:
            print(" Error: Debe ingresar un número entero válido para la cantidad.")


def ver_stock(inventario):
    print("\n==================== STOCK ACTUAL ====================")
    if len(inventario) == 0:
        print("====> No hay productos en el stock <====")
    else:
        for prod, cant in inventario.items():
            print(f"- {prod.capitalize()}: {cant} unidad(es)")
    
    input("\nPresione ENTER para volver al menú principal...")


def buscar_producto(inventario):
    busqueda = input("\nIngrese el producto que quiere buscar: ").strip().lower()
    
    if busqueda in inventario:
        print(f"-> Stock de {busqueda.capitalize()}: {inventario[busqueda]} unidad(es)")
    else:
        print(f" El producto '{busqueda.capitalize()}' no se encuentra en el stock.")
    
    input("\nPresione ENTER para volver al menú principal...")


def eliminar_producto(inventario):
    remover = input("\nIngrese el producto que quiere remover del stock: ").strip().lower()
    
    if remover in inventario:
        del inventario[remover]
        print(f" Se ha eliminado '{remover.capitalize()}' del inventario.")
    else:
        print(f" El producto '{remover.capitalize()}' no existe en el stock.")


def main():
    inventario = {}
    
    while True:
        mostrar_menu()
        opcion_input = input("Digite alguna de las opciones: ")
        
        if opcion_input.isdigit():
            opcion = int(opcion_input)
            
            if opcion == 1:
                agregar_producto(inventario)
            elif opcion == 2:
                ver_stock(inventario)
            elif opcion == 3:
                buscar_producto(inventario)
            elif opcion == 4:
                eliminar_producto(inventario)
            elif opcion == 5:
                print("\n=== GRACIAS POR USAR NUESTRO SISTEMA ===")
                break
            else:
                print(" Opción fuera de rango. Seleccione un número del 1 al 5.")
        else:
            print(" Entrada inválida. Ingrese un número entre 1 y 5.")


main()     
            
                
                
                
                
                
                
            
                
                
            
        
    
                
            
 
            
        

            
                 
                
            
                
                
                
                
                
                
            
                
                
            
        
    
                
            
 
            