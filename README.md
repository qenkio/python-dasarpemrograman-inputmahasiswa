# Nilai Mahasiswa

Tugas dasar pemrograman - program buat catat nilai mahasiswa, itung rata-rata, sama nentuin predikatnya.

## Cara pakai

```
python nilai_mahasiswa.py
```

Nanti diminta masukin nama sama nilai satu-satu. Kalau udah semua, tinggal enter kosong pas ditanya nama lagi.

Data otomatis kesimpen ke `nilai.txt`, jadi kalau dijalanin lagi nanti data lama ikut kebaca.

## Poin-poin yang ada di kode ini

- Fungsi `predikat()` sama `pesan()` buat nentuin grade dan kasih semangat sesuai nilainya
- Validasi input pakai try-except, biar kalau salah ketik (bukan angka) programnya gak crash
- Data mahasiswa disimpen di list of dict
- Baca-tulis file buat nyimpen data antar sesi
- Dipecah jadi beberapa fungsi biar gak numpuk di satu tempat
