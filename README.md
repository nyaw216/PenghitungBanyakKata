# Analisis Running Time Pencarian Kata dalam Teks

Aplikasi ini merupakan aplikasi berbasis **Streamlit** yang digunakan untuk menganalisis dan membandingkan **running time algoritma pencarian kata dalam teks** menggunakan dua pendekatan, yaitu **iteratif** dan **rekursif**.

---

## 📌 Deskripsi Aplikasi

Aplikasi ini menerima masukan berupa teks dan sebuah kata kunci, kemudian menghitung jumlah kemunculan kata kunci tersebut di dalam teks menggunakan:
- Algoritma **iteratif**
- Algoritma **rekursif**

Selain menampilkan hasil perhitungan, aplikasi ini juga mengukur **running time** dari masing-masing algoritma dan menyajikannya dalam bentuk **grafik perbandingan**, sehingga pengguna dapat mengamati perbedaan performa kedua pendekatan tersebut pada berbagai ukuran input.

---

## 🎯 Tujuan Pengembangan

Tujuan dari pembuatan aplikasi ini adalah:
1. Mengimplementasikan algoritma pencarian kata secara iteratif dan rekursif.
2. Membandingkan performa kedua algoritma berdasarkan running time.
3. Mengamati pengaruh ukuran input teks terhadap waktu eksekusi algoritma.
4. Memberikan visualisasi perbandingan running time dalam bentuk grafik.
5. Memahami perbedaan antara analisis kompleksitas teoritis dan performa aktual algoritma.

---

## 🛠️ Teknologi yang Digunakan

- **Python**
- **Streamlit**
- **Pandas**
- **Altair**
- **NumPy**

---

## 🚀 Cara Menggunakan secara Lokal

### 1️⃣ Clone Repository

```bash
git clone <url-repository-anda>
cd <nama-folder-repository>
```

### 2️⃣ Buat Environment
```bash
python -m venv venv
```
Aktifkan virtual environment:
- **Windows**
```bash
venv\Scripts\activate
```
- **Linux/macOS**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Pastikan file `requirements.txt` tersedia, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 4️⃣ Menjalankan Aplikasi Streamlit
```bash
streamlit run app.py
```

---

### 📂 Struktur File
```text
├── app.py              # File utama Streamlit
├── algorithms.py       # Implementasi algoritma iteratif & rekursif
├── requirements.txt    # Daftar dependency
└── README.md           # Dokumentasi aplikasi
```

---

### ⚠️ Catatan Penting
- Pada ukuran input besar (misalnya > 1000 kata), algoritma rekursif dapat mengalami kegagalan eksekusi akibat batas maksimum kedalaman rekursi Python.
- Algoritma iteratif tetap dapat dijalankan dengan stabil pada ukuran input besar.
- Perbedaan ini menjadi salah satu fokus analisis dalam tugas besar ini.

---

### 👥 Tim Pengembang
- Fathan Akbar Nashrullah (103012400002)
- Husnul Khotimah (103012430019)
- Naufal Hanif (103012400088)


