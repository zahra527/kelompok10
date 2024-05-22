#import module
import streamlit as st
import pandas as pd
from PIL import Image

def MyBG_colour(wch_colour):
    my_colour=f"<style>.stApp{{bacground-color:{wch_colour};}}</style>"
    st.markdown(my_colour,unsafe_allow_html=True)
MyBG_colour("#EA4855")

st.markdown("""
        <style>
        [data-testid=stSidebar]{
        background-color:#A08989;
}
        </style>
        """,unsafe_allow_html=True)
with st.sidebar:
        "##"

def Halaman_Utama():
    st.header('Aplikasi Perhitungan Kekentalan Metode Laju Alir Dengan Metode Oswald/Engler',divider="rainbow")
    st.title("Logika Pemrograman Komputer :blue [Kelompok 10]")
    st.image("foto lpk.png")
    st.markdown(''':rainbow[Hallo Guys!]''')
    st.markdown('''Aplikasi ini dapat digunakan untuk melakukan perhitungan kekentalan dengan menggunakan metode laju alir Oswald/Engler dengan menginput nilai densitas dan rata-rata dari laju alir yang didapat pada saat pengujian.''')
    st.markdown(''':blue[ARE YOU READY? LET'S GO!!!]''')



def Informasi():
     st.write("**INFORMASI**")
     st.write("Penetapan kekentalan (viskositas) menggunakan metode Engler dan Oswald merupakan dua cara yang umum digunakan untuk mengukur viskositas cairan. Berikut adalah penjelasan singkat mengenai masing-masing metode:")
     st.title(''':rainbow[Viskometer Engler]''')
     st.image("engler.jpg")
     st.write("Metode Engler menggunakan alat yang disebut viskometer Engler. Prinsip dasar metode ini adalah mengukur waktu yang dibutuhkan oleh sejumlah tertentu cairan untuk mengalir melalui orifis kecil pada suhu tertentu.")
     st.title(''':rainbow[Viskometer Oswald]''')
     st.image("oswald.jpg")
     st.write("Metode Oswald menggunakan alat yang disebut viskometer kapiler atau viskometer Oswald. Prinsip dasarnya adalah mengukur waktu yang dibutuhkan cairan untuk melewati dua tanda di dalam tabung kapiler pada suhu tertentu.")
     st.title(''':rainbow[Rumus Penetapan Kekentalan Metode Laju Alir Oswald/Engler]''')
     st.image('rumus2.png')


def Kalkulator_Perhitungan():
    st.image('rumus1.png')
    massa= st.number_input('Masukkan massa (g)')
    st.write("Massa sebesar",massa,step=1.0000,default_value = 1.0000)
    volume= st.number_input('Masukkan volume (mL)')
    st.write("Volume sebesar",volume,step=0.0010, default_value = 1.0000)
    if st.button("Hitung Nilai Densitas"):
        Densitas=massa/volume
        st.write(f"Densitas sebesar={Densitas}g/mL")

    st.image('rumus2.png')
    Densitas_sampel= st.number_input('Masukkan densitas sampel (g/mL)')
    Rata_rata_laju_alir_sampel = st.number_input ('Masukkan rata-rata laju alir sampel (s)')
    Densitas_air = st.number_input ('Masukkan densitas air (g/mL)')
    Rata_rata_laju_alir_air = st.number_input('Masukkan rata-rata laju alir air (s)')
    Viskositas_aquadest = st.number_input('Masukkan viskositas aquadest')
    Viskositas = 0
    if st.button("Hitung Nilai Viskositas"):
       Viskositas=(Densitas_sampel * Rata_rata_laju_alir_sampel) / (Densitas_air * Rata_rata_laju_alir_air) * Viskositas_aquadest
       st.write(f'Viskositas sebesar={Viskositas} P')

def Tabel_Viskositas():
    st.title(''':rainbow[Viskositas Air]''')
    st.write("Viskositas air adalah sifat fisik untuk dapat mengukur ketebalan suatu kekentalan air")

    #Membuat dataframe untuk tabel viskositas air
    data = {
         "Temperatur (°C)": list(range(1, 31)),
         "Viskositas (mPa.s)": [
              1.732, 1.647, 1.619, 1.568, 1.520, 1.474, 1.429, 1.386, 1.346, 1.307,
              1.270, 1.235, 1.201, 1.169, 1.138, 1.108, 1.080, 1.053, 1.027, 1.002, 
              0.978, 0.955, 0.933, 0.911, 0.893, 0.873, 0.854, 0.836, 0.818, 0.802
         ]
    }
    df = pd.DataFrame(data)
    st.write(df)

menu_options=["Halaman Utama","Informasi","Kalkulator Perhitungan","Tabel Viskositas"]
selected_menu=st.sidebar.radio("**Options**",menu_options)

if selected_menu=="Halaman Utama":
    page_bg_img="""
    <style>
    </style>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)
    Halaman_Utama()
elif selected_menu=="Informasi":
    Informasi()
elif selected_menu=="Kalkulator Perhitungan":
    Kalkulator_Perhitungan()
elif selected_menu=="Tabel Viskositas":
    Tabel_Viskositas()
