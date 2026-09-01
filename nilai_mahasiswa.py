import os

FILENAME = "nilai.txt"


def predikat(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    return "D"


def pesan(grade):
    if grade == "A":
        return "Mantap! Pertahankan prestasimu!"
    elif grade == "B":
        return "Bagus! Sedikit lagi bisa dapet A!"
    elif grade == "C":
        return "Ayo tingkatkan lagi belajarnya!"
    return "Jangan menyerah, semangat belajar!"


def input_nilai():
    while True:
        try:
            return float(input("Nilai: "))
        except ValueError:
            print("Masukkan angka ya!")


def input_semua_mahasiswa():
    data = []
    while True:
        nama = input("\nNama : ")
        if nama == "":
            break
        nilai = input_nilai()
        data.append({"nama": nama, "nilai": nilai})
    return data


def cetak_tabel(data):
    print(f"\n{'='*50}")
    print(f"{'Nama':<15} {'Nilai':<7} {'Grade':<6} Keterangan")
    print(f"{'-'*50}")
    for mhs in data:
        grade = predikat(mhs["nilai"])
        print(f"{mhs['nama']:<15} {mhs['nilai']:<7.2f} {grade:<6} {pesan(grade)}")
    print(f"{'='*50}")


def rata_rata(data):
    if not data:
        return 0
    return sum(mhs["nilai"] for mhs in data) / len(data)


def simpan_ke_file(data):
    with open(FILENAME, "w") as f:
        f.write(f"{'Nama':<15} {'Nilai':<7} {'Grade'}\n")
        f.write(f"{'-'*30}\n")
        for mhs in data:
            grade = predikat(mhs["nilai"])
            f.write(f"{mhs['nama']:<15} {mhs['nilai']:<7.2f} {grade}\n")
        f.write(f"{'-'*30}\n")
        f.write(f"Rata-rata: {rata_rata(data):.2f}\n")
    print(f"Data tersimpan ke {FILENAME}")


def muat_dari_file():
    if not os.path.exists(FILENAME):
        return []

    data = []
    with open(FILENAME, "r") as f:
        for baris in f:
            baris = baris.strip()
            if "," in baris:
                nama, nilai = baris.split(",")
                data.append({"nama": nama, "nilai": float(nilai)})
    return data


def main():
    data_lama = muat_dari_file()
    if data_lama:
        print("Data tersimpan sebelumnya ditemukan:")
        cetak_tabel(data_lama)

    data_baru = input_semua_mahasiswa()
    if not data_baru:
        print("Tidak ada data baru yang dimasukkan")
        return

    semua_data = data_lama + data_baru
    cetak_tabel(semua_data)
    print(f"Rata-rata: {rata_rata(semua_data):.2f}")

    simpan_ke_file(semua_data)


if __name__ == "__main__":
    main()
