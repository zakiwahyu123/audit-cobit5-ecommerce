# Website Audit Sistem Informasi E-Commerce — COBIT 5

Aplikasi Streamlit ini dikembangkan dari dokumen Tugas 1 AUSI:
**Form Audit Sistem Informasi pada Perusahaan E-Commerce Menggunakan Kerangka Kerja COBIT 5**.

## Fitur
- Beranda dan penjelasan lima prinsip COBIT 5.
- Identitas pelaksanaan audit.
- Form audit berisi 26 pertanyaan dari lima prinsip COBIT 5.
- Skor 0, 1, 2, 3, dan N/A.
- Kolom bukti/catatan dan rekomendasi.
- Perhitungan skor, persentase, dan interpretasi otomatis.
- Rekap per prinsip dan unduh detail jawaban ke CSV.
- Daftar pustaka sesuai dokumen sumber.

## Menjalankan di komputer (opsional)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Alur Google Colab → GitHub → Streamlit Community Cloud

### 1. Google Colab
1. Buka https://colab.research.google.com/
2. Buat notebook baru.
3. Upload `app.py` dan `requirements.txt` ke sesi Colab, atau clone repository GitHub.
4. Catatan: Colab cocok untuk menulis/menguji Python, tetapi aplikasi Streamlit yang akan dipublikasikan tetap dijalankan oleh Streamlit Community Cloud.

### 2. GitHub
1. Login ke https://github.com/
2. Buat repository baru, misalnya `audit-cobit5-ecommerce`.
3. Upload `app.py` dan `requirements.txt` ke repository.
4. Pastikan `app.py` berada di direktori utama (root) repository.

### 3. Streamlit Community Cloud
1. Buka https://share.streamlit.io/
2. Login menggunakan akun GitHub.
3. Pilih **Create app**.
4. Pilih repository `audit-cobit5-ecommerce`.
5. Branch: `main`.
6. Main file path: `app.py`.
7. Klik **Deploy**.
8. Tunggu proses instalasi selesai. Streamlit akan memberikan URL website.

## Catatan penting
- Isian audit tersimpan sementara di sesi aplikasi. Unduh CSV pada menu **Hasil Audit** agar rekap jawaban tersimpan di perangkat.
- Aplikasi ini adalah instrumen akademik, bukan hasil audit resmi PT Shopee Indonesia.
- Skala dan kategori interpretasi mengikuti dokumen Tugas 1, bukan kategori kapabilitas resmi COBIT 5.
