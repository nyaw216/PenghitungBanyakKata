import streamlit as st
import time
import pandas as pd
import numpy as np
import altair as alt

# import function dari algorithms.py
from algorithms import (
    preprocess_text,
    count_keywords_iterative,
    count_keywords_recursive
)

st.title("Penghitung Banyak Kata dalam Teks")

# field untuk memasukkan teks panjang
text = st.text_area("Masukkan teks", height=150)
# field untuk memasukkan kata kunci yang ingin dihitung banyaknya
keywords = st.text_input("Masukkan keyword (pisahkan dengan koma)")

if st.button("Jalankan Analisis"):
    # pra-proses teks panjang menjadi huruf kecil semua dan mengabaikan tanda baca
    words = preprocess_text(text)
    # memasukkan kata kunci ke dalam array key_list
    key_list = [k.strip().lower() for k in keywords.split(",") if k.strip() != ""]

    # menghitung input size sesuai banyak kata
    word_count = len(words)
    st.info(f"Input size (jumlah kata): {word_count}")

    # hitung iteratif
    start = time.time()
    result_iter = count_keywords_iterative(words, key_list)
    time_iter = time.time() - start

    # hitung rekursif
    time_rec = None
    result_rec = None
    rec_error = None

    try:
        start = time.time()
        result_rec = count_keywords_recursive(words, key_list, 0)
        time_rec = time.time() - start
    except RecursionError: # jika rekursif error karena kedalaman maksimal
        rec_error = "RecursionError: maximum recursion depth exceeded (maksimal kedalaman rekursif adalah 1000)"

    # output iteratif
    st.subheader("Hasil Iteratif")
    st.write(f"Total kemunculan {key_list}: {result_iter}")
    st.write(f"Running time: {time_iter:.6f} detik")

    # output rekursif
    st.subheader("Hasil Rekursif")
    if rec_error: # jika rekursif error karena kedalaman maksimal
        st.error(rec_error)
    else:
        st.write(f"Total kemunculan keyword: {result_rec}")
        st.write(f"Running time: {time_rec:.6f} detik")

    # deklarasi grafik
    df = pd.DataFrame({
        "Algoritma": ["Iteratif", "Rekursif"],
        "Running Time (detik)": [
            time_iter,
            time_rec if time_rec is not None else np.nan
        ]
    })
    chart = alt.Chart(df).mark_bar().encode(
        x="Algoritma",
        y="Running Time (detik)"
    )

    # output grafik
    st.altair_chart(chart, use_container_width=True)

