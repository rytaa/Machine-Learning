# Health Services Data Analysis

## Tentang Project

Project ini dibuat untuk menganalisis data layanan kesehatan menggunakan Python. Data yang digunakan berasal dari file `health.csv`, yang berisi informasi mengenai jenis layanan, lokasi, dan aksesibilitas kursi roda.

Dalam project ini, data diolah dan divisualisasikan untuk melihat pola persebaran layanan kesehatan. Selain itu, digunakan juga algoritma Machine Learning untuk mencoba mengelompokkan lokasi layanan dan memprediksi aksesibilitas kursi roda. Model yang sudah dilatih kemudian di-deploy sebagai API menggunakan Flask.

## Yang Dikerjakan

- Melihat struktur dan isi dataset.
- Mengecek data kosong dan data duplikat.
- Membersihkan data sebelum dianalisis.
- Melihat persebaran layanan kesehatan berdasarkan kota dan jenis layanan.
- Membuat visualisasi data menggunakan grafik.
- Melakukan analisis korelasi pada data numerik.
- Mengelompokkan lokasi layanan menggunakan K-Means.
- Membuat model prediksi menggunakan Random Forest.
- Mengevaluasi hasil prediksi model.
- Menyimpan model yang sudah dilatih.
- Men-deploy model sebagai API menggunakan Flask dan mengujinya dengan curl.

## Tools yang Digunakan

- Python
- Pandas dan NumPy
- Matplotlib dan Seaborn
- Scikit-learn
- Flask
- Jupyter Notebook

## Algoritma

**Random Forest Classifier**

Digunakan untuk memprediksi kategori aksesibilitas kursi roda berdasarkan informasi kota, jenis layanan, dan provinsi.

**K-Means Clustering**

Digunakan untuk mengelompokkan lokasi layanan kesehatan berdasarkan koordinat latitude dan longitude.

## File Project

- `health.csv` — dataset yang digunakan untuk analisis.
- `project.ipynb` — notebook berisi proses analisis data dan penerapan Machine Learning.
- `random_forest_health.pkl` — model hasil training (berisi model, encoder, dan daftar fitur). File ini dibuat setelah cell penyimpanan model di notebook dijalankan.
- `app.py` — aplikasi Flask untuk deployment model sebagai API.
- `data.json` — contoh input untuk menguji API.

## Cara Menjalankan

1. Download atau clone repository ini.
2. Pastikan file `health.csv` berada di folder yang sama dengan notebook.
3. Install library yang diperlukan:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter flask
   ```

4. Buka Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Buka file `project.ipynb` dan jalankan cell secara berurutan sampai file `random_forest_health.pkl` terbentuk.

## Deployment

Setelah model dilatih dan disimpan, tahap berikutnya adalah deployment, yaitu membuat model dapat dipakai lewat API. Pada project ini, deployment dilakukan secara lokal menggunakan Flask.

### Alur Deployment

1. Model Random Forest disimpan dengan `pickle` ke file `random_forest_health.pkl`. File ini berisi tiga hal: model, encoder untuk kolom kategori, dan daftar kolom fitur.
2. `app.py` memuat file tersebut saat server dijalankan.
3. API menerima input berupa `city`, `taxonomy_name`, dan `province` dalam format JSON.
4. Input teks diubah menjadi angka memakai encoder yang sama seperti saat training.
5. Model memprediksi aksesibilitas kursi roda, lalu API mengembalikan label dan probabilitasnya.

### Menjalankan API

1. Pastikan file `app.py`, `data.json`, dan `random_forest_health.pkl` berada di folder yang sama.
2. Jalankan server Flask:

   ```bash
   python app.py
   ```

   Jika berhasil, akan muncul tulisan `Running on http://127.0.0.1:5000`. Biarkan terminal ini tetap terbuka.

3. Buka terminal baru di folder yang sama, lalu uji API.

   **Command Prompt (cmd) atau Linux/Mac:**

   ```bash
   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @data.json
   ```

   **PowerShell (Windows):**

   ```powershell
   curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '@data.json'
   ```

   Atau memakai `Invoke-RestMethod`:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -ContentType "application/json" -Body (Get-Content data.json -Raw)
   ```

### Contoh Input (`data.json`)

```json
{
    "city": "Vancouver",
    "taxonomy_name": "Individual Counselling",
    "province": "BC"
}
```

Nilai `city`, `taxonomy_name`, dan `province` harus sama persis dengan kategori yang ada di dataset.

### Contoh Output

```json
{
  "label": "Aksesibel",
  "prediction": "Y",
  "probability": {
    "N": 0.3084,
    "Y": 0.6916
  }
}
```

Keterangan:

- `prediction`: `Y` berarti layanan aksesibel untuk kursi roda, `N` berarti tidak.
- `probability`: tingkat keyakinan model untuk masing-masing kelas.

### Penanganan Error

Jika kategori yang dimasukkan tidak ada di dataset, API akan mengembalikan error 400. Contoh:

```json
{"error": "Kategori 'Jakarta' tidak dikenal pada kolom CITY"}
```

### Catatan

- Server ini adalah development server bawaan Flask, cocok untuk praktik lokal dan bukan untuk production.
- Gunakan versi scikit-learn yang sama saat menyimpan dan memuat model agar file `.pkl` dapat dibuka tanpa masalah.

## Hasil

Melalui project ini, dilakukan analisis terhadap data layanan kesehatan serta penerapan K-Means dan Random Forest. Model Random Forest mencapai akurasi sekitar 73,95% pada data uji, lalu berhasil di-deploy sebagai API Flask yang dapat menerima input JSON dan mengembalikan prediksi aksesibilitas. Hasil analisis dan evaluasi model dapat dilihat langsung dari output yang dihasilkan saat notebook dijalankan.

## Author

Dita Adelia Putri

Project Machine Learning
