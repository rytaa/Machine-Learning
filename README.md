# Machine-Learning
Health services data analysis using Python, data visualization, K-Means clustering, and Random Forest classification to analyze wheelchair accessibility.
# Health Services Data Analysis

## Tentang Project

Project ini dibuat untuk menganalisis data layanan kesehatan menggunakan Python. Data yang digunakan berasal dari file `health.csv`, yang berisi informasi mengenai jenis layanan, lokasi, dan aksesibilitas kursi roda.

Dalam project ini, data diolah dan divisualisasikan untuk melihat pola persebaran layanan kesehatan. Selain itu, digunakan juga algoritma Machine Learning untuk mencoba mengelompokkan lokasi layanan dan memprediksi aksesibilitas kursi roda.

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

## Tools yang Digunakan

- Python
- Pandas dan NumPy
- Matplotlib dan Seaborn
- Scikit-learn
- Jupyter Notebook

## Algoritma

**Random Forest Classifier**

Digunakan untuk memprediksi kategori aksesibilitas kursi roda berdasarkan informasi kota, jenis layanan, dan provinsi.

**K-Means Clustering**

Digunakan untuk mengelompokkan lokasi layanan kesehatan berdasarkan koordinat latitude dan longitude.

## File Project

- `health.csv` — dataset yang digunakan untuk analisis.
- `project.ipynb` — notebook berisi proses analisis data dan penerapan Machine Learning.
- `random_forest_health.pkl` — file model yang sudah disimpan setelah proses training.

File model akan tersedia setelah proses penyimpanan model berhasil dijalankan.

## Cara Menjalankan

1. Download atau clone repository ini.
2. Pastikan file `health.csv` berada di folder yang sama dengan notebook.
3. Install library yang diperlukan:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

4. Buka Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Buka file `project.ipynb` dan jalankan cell secara berurutan.

## Hasil

Melalui project ini, dilakukan analisis terhadap data layanan kesehatan serta penerapan K-Means dan Random Forest. Hasil analisis dan evaluasi model dapat dilihat langsung dari output yang dihasilkan saat notebook dijalankan.

## Author

Dita Adelia Putri

Project Machine Learning
