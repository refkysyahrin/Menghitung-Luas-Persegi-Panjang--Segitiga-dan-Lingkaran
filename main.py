import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar Menu
with st.sidebar :
    selected = option_menu('Hitung Luas Bangun',
    ['Hitung Luas Persegi Panjang',
     'Hitung Luas Segitiga',
     'Hitung Luas Lingkaran'],                   
    default_index=0)

# Halaman Hitung Luas Persegi Panjang
if (selected == 'Hitung Luas Persegi Panjang'):
    st.title("Hitung Luas Persegi Panjang")

    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0) 
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.write("Luas Persegi Panjang Adalah = ", luas)
        st.success(f"Luas Persegi Panjang Adalah = {luas}")

# Halaman Hitung Luas Segitiga
if (selected == 'Hitung Luas Segitiga'):
    st.title("Hitung Luas Segitiga")

    alas = st.slider ("Masukkan Nilai Alas", 100)
    tinggi = st.slider ("Masukkan Nilai Tinggi", 100) 
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write("Luas Segitiga Adalah = ", luas)
        st.success(f"Luas Segitiga Adalah = {luas}")

# Halaman Hitung Luas Lingkaran
if (selected == 'Hitung Luas Lingkaran'):
    st.title("Hitung Luas Lingkaran")
    
    r = st.number_input("Masukkan Nilai Jari-jari (r)", 0.0)
    hitung_lingkaran = st.button("Hitung Luas")

    if hitung_lingkaran:
        luas_lingkaran = 3.14 * (r ** 2)
        st.write("Luas Lingkaran Adalah = ", luas_lingkaran)
        st.success(f"Luas Lingkaran Adalah = {luas_lingkaran}")