# Sistema de Gestión de Inventario (SISTEMA INV PRADO.MAPR)

Una aplicación de consola en Python ligera e intuitiva para administrar inventarios de productos en tiempo real mediante un diccionario dinámico.

---

## 📌 Características

- **Gestión de Stock:** Agrega unidades a productos existentes o registra nuevos elementos automáticamente.
- **Normalización de Texto:** Convierte las entradas a minúsculas para evitar duplicados por diferencias de mayúsculas/minúsculas (ej. "Manzana" y "manzana" se tratan como el mismo producto).
- **Validación de Datos:** Previene fallos por ingreso de texto en campos numéricos y evita la inserción de cantidades negativas.
- **Búsqueda y Eliminación:** Consulta rápida de stock por producto y eliminación definitiva de registros.
- **Navegación Interactiva:** Menú estructurado con pausado de pantalla para mayor comodidad del usuario.

---

## 🛠️ Requisitos Previos

- **Python 3.x** instalado en el sistema.

 No requiere librerías externas o dependencias adicionales.

---

## 🚀 Uso del Sistema

1. **Clonar o descargar** el archivo `.py` en tu equipo.
2. Abre la terminal o consola de comandos en la carpeta donde se encuentra el archivo.
3. Ejecuta el programa con:

```bash
python nombre_del_archivo.py