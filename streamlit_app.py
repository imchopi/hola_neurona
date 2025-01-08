import streamlit as st

# Mostrar la imagen y el título
st.image("./img/neurona.jpg")
st.subheader("¡Hola neurona!")

# Opciones de pestañas
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.subheader("Una neurona con una entrada y un peso")
    
    # Control deslizante para ajustar el peso
    w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=2.50, key="slider_tab1_w0")
    
    # Entrada numérica para el valor de la entrada
    x0 = st.number_input("Introduzca el valor de la entrada", min_value=0.0, value=5.0, key="input_tab1_x0")
    
    # Cálculo de la salida
    if st.button("Calcular la salida", key="button_tab1"):
        y = w0 * x0
        st.write(f"La salida de la neurona es {y}")

with tab2:
    st.subheader("Dos entradas")

    # Dividir en dos columnas
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, key="slider_tab2_w0")
        x0 = st.number_input("Entrada x₀", min_value=0.0, key="input_tab2_x0")
    with col2:
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, key="slider_tab2_w1")
        x1 = st.number_input("Entrada x₁", min_value=0.0, key="input_tab2_x1")
    
    # Cálculo de la salida
    if st.button("Calcular la salida", key="button_tab2"):
        y = w0 * x0 + w1 * x1
        st.write(f"La salida de la neurona es {y}")

with tab3:
    st.subheader("Tres entradas y sesgo")

    # Dividir en tres columnas
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, key="slider_tab3_w0")
        x0 = st.number_input("Entrada x₀", min_value=0.0, key="input_tab3_x0")
    with col2:
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, key="slider_tab3_w1")
        x1 = st.number_input("Entrada x₁", min_value=0.0, key="input_tab3_x1")
    with col3:
        w2 = st.slider("Peso w₂", min_value=0.0, max_value=5.0, key="slider_tab3_w2")
        x2 = st.number_input("Entrada x₂", min_value=0.0, key="input_tab3_x2")
    
    # Sesgo en una fila aparte
    b = st.number_input("Introduzca el valor del sesgo", min_value=0.0, key="input_tab3_b")
    
    # Cálculo de la salida
    if st.button("Calcular la salida", key="button_tab3"):
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.write(f"La salida de la neurona es {y}")
