# Sistema de Gestión de Inventario (SISTEMA INV PRADO.MAPR)

Una aplicación de gestión de inventarios en tiempo real desarrollada en Python y adaptada con **Streamlit** para ofrecer una interfaz web interactiva, moderna y accesible desde cualquier navegador.

---

## 📌 Características

- **Gestión de Stock:** Agrega unidades a productos existentes o registra nuevos elementos automáticamente.
- **Normalización de Texto:** Convierte las entradas a minúsculas para evitar duplicados por diferencias de mayúsculas/minúsculas (ej. "Manzana" y "manzana" se tratan como el mismo producto).
- **Validación de Datos:** Evita registros vacíos y asegura el ingreso correcto de valores numéricos para el stock.
- **Búsqueda y Eliminación:** Consulta rápida de stock por producto y eliminación definitiva de registros.
- **Interfaz Web Interactiva:** Control intuitivo mediante barra lateral de navegación y notificaciones visuales sobre el estado del inventario.

---

## 🚀 Deploy y Adaptación a Streamlit

Para desplegar este proyecto en un entorno web como **Streamlit Community Cloud**, se realizó una refactorización del código fuente original (creado inicialmente para ejecutarse en la consola/terminal).

### 🤖 Asistencia con Inteligencia Artificial
La migración de la consola a la interfaz web de Streamlit se llevó a cabo utilizando **Inteligencia Artificial (IA)** como asistente de código. La IA permitió adaptar la lógica síncrona de comandos por teclado a una arquitectura reactiva e interactiva propia de la web.

### 🔄 Cambios principales aplicados al código fuente:

1. **Reemplazo de Entrada y Salida Estándar:**
   - Se eliminaron las funciones nativas `print()` e `input()`, las cuales bloqueaban la ejecución en servidores web.
   - Se implementaron componentes gráficos de Streamlit como `st.text_input()`, `st.number_input()`, `st.button()` y `st.success() / st.error()`.

2. **Gestión de Estado Persistente (`st.session_state`):**
   - En consola, la variable `inventario` permanecía viva dentro del ciclo `while True`. En Streamlit, la página se reejecuta desde el inicio con cada interacción.
   - Se adaptó el diccionario de inventario para que se almacene dentro de `st.session_state.inventario`, garantizando que la información de los productos no se borre al presionar botones o cambiar de opción.

3. **Navegación Visual:**
   - Se sustituyó el menú impreso en texto por una barra de navegación lateral (`st.sidebar.selectbox`).

---

## 🛠️ Requisitos Previos

- **Python 3.x**
- **Streamlit**

Para instalar la dependencia necesaria, ejecuta en tu terminal:

```bash
pip install streamlit
```

---

## 💻 Ejecución Local

1. **Clona o descarga** este repositorio en tu equipo.
2. Abre la terminal en la carpeta principal del proyecto.
3. Ejecuta la aplicación con el siguiente comando:

```bash
streamlit run app.py
```

4. El sistema abrirá automáticamente una pestaña en tu navegador predeterminado en `http://localhost:8501`.

---

## 📋 Funcionalidades del Menú

| Opción | Acción | Descripción |
| :--- | :--- | :--- |
| **Agregar producto** | Formulario de registro | Permite ingresar un producto y su cantidad enviándolo directamente a la memoria de la app. |
| **Ver stock** | Vista de Inventario | Muestra el listado completo de productos registrados con sus respectivas unidades. |
| **Buscar producto** | Consulta por nombre | Muestra en pantalla el stock disponible de un producto en específico. |
| **Eliminar producto** | Borrado de registro | Remueve un producto del inventario de forma definitiva. |

---

## 🌐 Despliegue en la Nube (Streamlit Cloud)

Para publicar esta app de forma gratuita en la nube:

1. Sube tu código junto con este `README.md` a tu repositorio en **GitHub**.
2. Asegúrate de incluir un archivo `requirements.txt` que contenga la línea:
   ```text
   streamlit
   ```
3. Conecta tu cuenta de GitHub a [Streamlit Community Cloud](https://streamlit.io/cloud).
4. Selecciona tu repositorio y la rama principal para realizar el **Deploy** instantáneo.