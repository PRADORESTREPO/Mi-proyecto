print("====================SISTEMA INV PRADO.MAPR====================")


producto = {}

continuar = 0
cantidad = 0
while True:
    print("1.Agregar producto")
    print("2.Ver stock")
    print("3.Buscar producto")
    print("4.Eliminar producto")
    print("5.Salir")
    print("=============================================")
    opcion = int(input("Digite alguna de las opciones"))
        
    if opcion == 1:
        
    
       while True:   
        productos = input("ingrese el producto(si desea salir ponga la palabra (salir)):")
    
        print("=============================")
   
        if productos == "salir":
            
            break
        
        cantidad = int(input(f"Ingrese cuantas unidades ingresa de {productos} "))
        if productos in producto:
                    
            producto[productos] += cantidad
                    
        else:
            producto[productos] = cantidad
   
    elif opcion == 2:
        

        for producto1, cantidad in producto.items():
                            
            print(f"- {producto1.capitalize()}: {cantidad}")
            
        volver = input("¿Si quiere volver al menu principal presione el espacio? ")
        
        
    elif opcion == 3:
        
        busqueda = input("Ingrese producto que quiere filtrar o (presione el espacio para volver al menu) ").capitalize()
        while True:
           
            if busqueda == "":
               break
      
            for busqueda in producto:
            
                print(f"-> Stock de {busqueda.capitalize()}: {producto[busqueda]}")
                
                break
                
                
                      
            
            
                
                    
                
                
                
            
        
    
                
            
 
            