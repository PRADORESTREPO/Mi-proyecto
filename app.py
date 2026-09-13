import streamlit as st

st.set_page_config(page_title="SISTEMA INV PRADO.MAPR", page_icon="📦")

# 1. MANTENER EL ESTADO EN MEMORIA (Reemplaza a la variable local de main)
if "inventario" not in st.session_state:
    st.session_state.inventario = {}

st.title("📦 SISTEMA INV PRADO.MAPR")

# 2. REEMPLAZO DEL MENÚ CON UNA BARRA LATERAL (Sidebar)
opcion = st.sidebar.selectbox(
    "Seleccione una opción:",
    ["Agregar producto", "Ver stock", "Buscar producto", "Eliminar producto"]
)

# ---------------------------------------------------------
# OPCIÓN 1: AGREGAR PRODUCTO
# ---------------------------------------------------------
if opcion == "Agregar producto":
    st.subheader("Agregar o Actualizar Producto")
    
    # Reemplazo de los input() por st.text_input y st.number_input
    nombre_producto = st.text_input("Ingrese el nombre del producto:").strip().lower()
    cantidad = st.number_input("Ingrese la cantidad:", min_value=1, step=1)
    
    if st.button("Guardar en Inventario"):
        if nombre_producto:
            st.session_state.inventario[nombre_producto] = (
                st.session_state.inventario.get(nombre_producto, 0) + cantidad
            )
            st.success(f"Se agregaron {cantidad} unidad(es) de '{nombre_producto.capitalize()}'.")
        else:
            st.warning("Por favor, ingrese un nombre de producto válido.")

# ---------------------------------------------------------
# OPCIÓN 2: VER STOCK
# ---------------------------------------------------------
elif opcion == "Ver stock":
    st.subheader("Stock Actual")
    
    if len(st.session_state.inventario) == 0:
        st.info("====> No hay productos en el stock <====")
    else:
        # Mostramos los datos de forma limpia
        for prod, cant in st.session_state.inventario.items():
            st.write(f"- **{prod.capitalize()}**: {cant} unidad(es)")

# ---------------------------------------------------------
# OPCIÓN 3: BUSCAR PRODUCTO
# ---------------------------------------------------------
elif opcion == "Buscar producto":
    st.subheader("Buscar Producto")
    busqueda = st.text_input("Ingrese el producto que quiere buscar:").strip().lower()
    
    if st.button("Buscar"):
        if busqueda in st.session_state.inventario:
            cant = st.session_state.inventario[busqueda]
            st.success(f"Stock de **{busqueda.capitalize()}**: {cant} unidad(es)")
        else:
            st.error(f"El producto '{busqueda.capitalize()}' no se encuentra en el stock.")

# ---------------------------------------------------------
# OPCIÓN 4: ELIMINAR PRODUCTO
# ---------------------------------------------------------
elif opcion == "Eliminar producto":
    st.subheader("Eliminar Producto")
    remover = st.text_input("Ingrese el producto que quiere remover:").strip().lower()
    
    if st.button("Eliminar"):
        if remover in st.session_state.inventario:
            del st.session_state.inventario[remover]
            st.success(f"Se ha eliminado '{remover.capitalize()}' del inventario.")
        else:
            st.error(f"El producto '{remover.capitalize()}' no existe en el stock.")
