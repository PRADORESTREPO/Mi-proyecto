# SISTEMA INV PRADO.MAPR

Una aplicación de consola desarrollada en Python para la gestión y control de inventarios de productos en tiempo real. El sistema permite registrar nuevos elementos o actualizar las cantidades de los existentes, realizar búsquedas puntuales de stock, eliminar registros obsoletos y consultar el catálogo completo de manera segura, estructurada y libre de fallos gracias a un sólido control de excepciones.

---

## Funcionalidades

- **Agregar producto:** Registra un nuevo producto y su cantidad o incrementa el stock si el producto ya existe. Permite salir del bucle de ingreso al presionar la tecla espacio (o presionar Enter con un texto vacío).
- **Ver stock:** Visualiza el listado completo de todos los productos almacenados con sus respectivas unidades disponibles.
- **Buscar producto:** Consulta la cantidad en existencia de un producto específico mediante una búsqueda por nombre.
- **Eliminar producto:** Remueve definitivamente un producto del inventario mediante la eliminación de su clave en el diccionario.
- **Normalización de texto:** Convierte los nombres ingresados a minúsculas para evitar registros duplicados por variaciones de mayúsculas/minúsculas y los muestra formateados con inicial mayúscula (`capitalize()`).
- **Manejo integral de excepciones:** Captura errores de tipo de dato (`ValueError`), búsquedas fallidas (`KeyError`), salidas forzadas por teclado (`KeyboardInterrupt`) y entradas vacías en cada una de las opciones del menú.

---

## Cómo ejecutar

### Requisitos previos
- **Python 3.x** instalado en el sistema.

### Pasos de ejecución local

1. Clonar o descargar este repositorio en tu equipo.
2. Abrir la terminal o consola de comandos en la carpeta donde se encuentra el archivo `.py`.
3. Ejecutar la aplicación con el comando:
   ```bash
   python nombre_del_archivo.py

   """

## SISTEMA INV PRADO.MAPR - Sistema de Gestión de Inventario


🛠️ TECNOLOGÍAS USADAS:
- Python 3: Lenguaje principal para la lógica de negocio, estructuras 
  de datos (diccionarios) y control de excepciones.
- Git & GitHub: Control de versiones y gestión de repositorio remoto.
- Inteligencia Artificial (IA): Soporte en la refactorización, manejo 
  de errores avanzado y generación de documentación.
============================================================
"""