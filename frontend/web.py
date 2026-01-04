import streamlit as st
import requests
import matplotlib.pyplot as plt
import os

# 1. Configuración: ¿Dónde vive el cerebro?
API_URL = os.getenv("API_URL","http://127.0.0.1:8000")

st.title("🍎 LifeOS Infinity - Panel de Control")

# 2. SECCIÓN: Ver Alimentos


with st.sidebar:
    st.header("Añadir nuevo alimento")

    name = st.text_input("Nombre del alimento")
    protein = st.number_input("Proteínas (por 100g)" , min_value=0.0, format="%.2f")
    carbs = st.number_input("Carbohidratos (por 100g)" , min_value=0.0, format="%.2f")
    fats = st.number_input("Grasas (por 100g)" , min_value=0.0, format="%.2f")
    if st.button("Guardar en base de datos"):
        new_food = {
            "name": name,
            "protein_per_100g": protein,
            "carbs_per_100g": carbs,
            "fats_per_100g": fats 
        }
        try:
            response = requests.post(f"{API_URL}/foods",json = new_food)
            if response.status_code == 200:
                st.success(f"{name} añadido correctamente")
            else:
                st.error(f" Error del servidor: {response.text}")
        except Exception as e:
            st.error(f"No se puedo conectar: {e}")


tab1, tab2 = st.tabs(["📦 Inventario", "🧮 Calculadora"])

# === PESTAÑA 1: VER LISTA ===
with tab1:
    if st.button("Cargar lista"):
        try:
            res = requests.get(f"{API_URL}/foods")
            if res.status_code == 200:
                st.table(res.json())
        except Exception as e:
            st.error(f"Error de conexión: {e}")

with tab2:
    st.header("Diseña tu comida")
    
    try:
        res = requests.get(f"{API_URL}/foods")
        if res.status_code == 200:
            all_foods = res.json()
            food_names = [f["name"] for f in all_foods]
        else:
            food_names = []
    except:
        st.error("No se pueden cargar los alimentos")
        food_names = []
    
    selected_items = st.multiselect("Seleciona los alimentos",options = food_names)

    meal_payload = []
    
    if selected_items:
        st.write("Indica el peso de cada alimento (en gramos)")

        for item_name in selected_items:
            grams = st.number_input(f"Gramos de {item_name}", min_value = 0, key=item_name)
            meal_payload.append({"name":item_name, "weight_g": grams})

        if st.button("🧮 Calcular Macros Totales"):
            try:
                res = requests.post(f"{API_URL}/meal/calculate",json=meal_payload)
                if res.status_code == 200:
                    result = res.json()
                    st.success(f"Cálculo realizado con éxito")

                    st.divider()
                    st.subheader("📊 Distribución Calórica")

                    # 1. Datos y Colores
                    labels = ['Proteínas', 'Carbos', 'Grasas']
                    sizes = [result['total_protein'], result['total_carbs'], result['total_fats']]
                    colors = ['#ff7675', '#0984e3', '#00b894'] # Rojo suave, Azul, Verde

                    # 2. Lienzo
                    fig, ax = plt.subplots()
                    fig.patch.set_alpha(0) # Fondo transparente
                    ax.patch.set_alpha(0)

                    # 3. Dibujar el DONUT (Sin etiquetas externas)
                    wedges, texts, autotexts = ax.pie(
                        sizes, 
                        # labels=labels, <--- BORRAMOS ESTO (Para no ensuciar el gráfico)
                        colors=colors, 
                        autopct='%1.0f%%', 
                        startangle=90,
                        pctdistance=0.85, # Porcentajes más pegados al borde
                        wedgeprops={'width': 0.4, 'edgecolor': '#0e1117', 'linewidth': 2},
                        textprops={'color': "white"}
                    )

                    # 4. Estilizar los números de dentro (Porcentajes)
                    for autotext in autotexts:
                        autotext.set_color('white')
                        autotext.set_weight('bold')
                        autotext.set_fontsize(12)

                    # 5. CREAR LA LEYENDA (La clave del minimalismo)
                    # frameon=False: Quita el recuadro feo de la leyenda
                    # loc='lower center': La pone abajo centrada
                    # ncol=3: La pone en horizontal (3 columnas) en vez de vertical
                    leg = ax.legend(wedges, labels,
                              title="Macronutrientes",
                              loc="center",
                              bbox_to_anchor=(0.5, -0.1), # La empujamos un poco hacia abajo
                              ncol=3, 
                              frameon=False,
                              labelcolor="white" # Texto blanco para modo oscuro
                              )

                    # Hack para que el título de la leyenda también sea blanco
                    plt.setp(leg.get_title(), color='white')

                    ax.axis('equal')  
                    st.pyplot(fig)


                    col1,col2,col3 = st.columns(3)
                    col1.metric("Proteínas",f"{result["total_protein"]:.2f} g")
                    col2.metric("Carbohidratos",f"{result["total_carbs"]:.2f} g")
                    col3.metric("Grasas",f"{result["total_fats"]:.2f} g")
                else:st.error(f"Error al calcular")
            except Exception as e:
                st.error(f"Error de técnico: {e}")



st.header("Inventario de Alimentos")      

# Botón para refrescar datos
if st.button("Cargar Alimentos"):
    try:
        # Hacemos la llamada al camarero (API)
        response = requests.get(f"{API_URL}/foods")
        
        if response.status_code == 200:
            foods = response.json() # Convertimos el JSON a lista de Python
            
            if foods:
                # Streamlit es mágico: le das una lista y te pinta una tabla
                st.table(foods)
            else:
                st.warning("El almacén está vacío. ¡Añade alimentos!")
        else:
            st.error("Error al conectar con el servidor.")
            
    except requests.exceptions.ConnectionError:
        st.error("🚨 No puedo conectar con el Backend. ¿Está encendido?")