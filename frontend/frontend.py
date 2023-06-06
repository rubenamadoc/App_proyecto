import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
# from folium.plugins import HeatMap

st.set_page_config(
    page_title="appTempo",
    page_icon="🏖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    # Aplicar estilos CSS para posicionar el texto en la esquina inferior derecha
    st.markdown(
        """
        <style>
        .footer {
            position: relative;
            left: 0;
            bottom: 0;
            color: rgba(250, 250, 250, 0.4);
            font-size: 14px;
            padding: 0.5rem 1rem;
            width: 100%;
            text-align: right;

        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Agregar el texto
    st.markdown(
        """
        <div class="footer">
        <p>Designed by Rubén Amado Cárdenas</p>
        </div>
        """,
        unsafe_allow_html=True
    )

#Inserta en la página una presentación
st.title('Bienvenido a appTempo')
st.header('¿Que te gustaría saber?')

# Crea tres columnas con los promedios de temperaturas, humedades y precipitaciones
col1, col2, col5 = st.columns(3)
with col1:
    st.subheader('Precipitaciones')
    r = requests.get('http://api_backend:5000/promedio_prob_precipitacion')
    st.write(r.text)

with col2:
    st.subheader('Temperaturas')
    v = requests.get('http://api_backend:5000/promedio_temperaturas')
    st.write(v.text)

with col5:
    st.subheader('Humedades')
    x = requests.get('http://api_backend:5000/promedio_humedades')
    st.write(x.text)

# Inserta un botón para la obtención de la probabilidad de frío o calor, dependiendo de que pulse mostrará uno u otro.
col3,col4 = st.columns(2)

with col3:
    st.write('Probalidad de calor')
    if st.button('Calor'):
        y = requests.get('http://api_backend:5000/probabilidad_calor')
        st.write(y.text,'%')
with col4:
    st.write('Probalidad de frío')
    if st.button('Frío'):
        w = requests.get('http://api_backend:5000/probabilidad_frio')
        st.write(w.text,'%')

# Crea un slidesahre con dos ventanas, en una se puede ver las condiciones actuales para navegar y en otra un pronóstico futuro de las condiciones.

st.subheader('Condciones para navegar')

tab1, tab2 = st.tabs(["Pronóstico", "Actual"])
with tab1:
    z = requests.get('http://api_backend:5000/condiciones_nav')
    st.info(z.text)

with tab2:
    a = requests.get('http://api_backend:5000/condiciones_nav_actual')
    st.info(a.text)

# Crear un mapa centrado en una ubicación específica
icono = requests.get('http://api_backend:5000/icono')
st.title("Mapa")
mapa = folium.Map(location=[37.26801411623821, -6.0622439050974215], zoom_start=12)
# Añadir un marcador al mapa
folium.Marker(location=[37.26801411623821, -6.0622439050974215], popup='Estación', icon=folium.Icon(color='black', icon=icono.text, prefix='fa')).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

# demo = requests.get('http://api_backend:5000/temperatura')
# st.text(demo.text)

main()