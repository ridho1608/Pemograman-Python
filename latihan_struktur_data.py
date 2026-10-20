"""Latihan string, list, set, dictionary, dan pembacaan file."""

from collections import Counter
import re


# 1. Pengolahan kalimat
def analisis_kalimat(kalimat):
    kata = kalimat.split()
    terpanjang = max(kata, key=len) if kata else "(tidak ada)"
    return {
        "jumlah_kata": len(kata),
        "jumlah_karakter": len(kalimat),  # termasuk spasi dan tanda baca
        "kata_terpanjang": terpanjang,
        "title_case": kalimat.title(),
    }


# 2. Analisis nilai mahasiswa
def kategori_nilai(nilai):
    """Skala: A >= 85, B >= 75, C >= 65, D >= 50, selain itu E."""
    if nilai >= 85:
        return "A"
    if nilai >= 75:
        return "B"
    if nilai >= 65:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def analisis_nilai(daftar_nilai):
    if not daftar_nilai:
        raise ValueError("Daftar nilai tidak boleh kosong.")
    kelompok = {kategori: [] for kategori in "ABCDE"}
    for nilai in daftar_nilai:
        kelompok[kategori_nilai(nilai)].append(nilai)
    return {
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "tertinggi": max(daftar_nilai),
        "terendah": min(daftar_nilai),
        "kelompok_kategori": kelompok,
        "frekuensi_kategori": {
            kategori: len(nilai_kategori)
            for kategori, nilai_kategori in kelompok.items()
        },
    }


# 3. Operasi set penerima beasiswa
def analisis_beasiswa(beasiswa_a, beasiswa_b):
    a, b = set(beasiswa_a), set(beasiswa_b)
    return {
        "menerima_keduanya": a & b,
        "hanya_a": a - b,
        "b_tanpa_a": b - a,
        "semua_penerima_unik": a | b,
    }


# 4. Inventaris: nama barang -> (harga, stok)
inventaris = {}


def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        raise ValueError(f"Barang {nama!r} sudah ada.")
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")
    inventaris[nama] = (harga, stok)


def update_stok(nama, stok_baru):
    if nama not in inventaris:
        raise KeyError(f"Barang {nama!r} tidak ditemukan.")
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)


def cari_barang_berdasarkan_harga(harga_min, harga_maks):
    return {
        nama: (harga, stok)
        for nama, (harga, stok) in inventaris.items()
        if harga_min <= harga <= harga_maks
    }


def total_nilai_inventaris():
    return sum(harga * stok for harga, stok in inventaris.values())


# 5. Analisis teks dari file
def analisis_file_teks(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        teks = file.read()

    # Regex mengambil rangkaian huruf/angka; hasil dinormalisasi ke huruf kecil.
    kata = re.findall(r"\b\w+\b", teks.lower(), flags=re.UNICODE)
    frekuensi = Counter(kata)
    total_kata = len(kata)
    kata_unik = set(kata)
    hapax = {k for k, jumlah in frekuensi.items() if jumlah == 1}
    return {
        "frekuensi": dict(frekuensi),
        "10_tersering": frekuensi.most_common(10),
        "hapax_legomena": hapax,
        "rasio_kata_unik": len(kata_unik) / total_kata if total_kata else 0,
        "total_kata": total_kata,
    }


def main():
    while True:
        print("\n=== MENU LATIHAN STRUKTUR DATA ===")
        print("1. Analisis kalimat")
        print("2. Analisis nilai mahasiswa")
        print("3. Operasi set beasiswa")
        print("4. Inventaris toko")
        print("5. Analisis teks dari file")
        print("0. Keluar")
        pilihan = input("Pilih soal (0-5): ").strip()

        if pilihan == "1":
            print("\n=== 1. Analisis kalimat ===")
            kalimat = input("Masukkan kalimat: ")
            for label, nilai in analisis_kalimat(kalimat).items():
                print(f"{label.replace('_', ' ').title()}: {nilai}")

        elif pilihan == "2":
            print("\n=== 2. Analisis nilai ===")
            try:
                teks_nilai = input(
                    "Masukkan nilai, pisahkan dengan koma (contoh: 90,80,72,60,45): "
                )
                nilai_mahasiswa = [float(x.strip()) for x in teks_nilai.split(",")]
                hasil_nilai = analisis_nilai(nilai_mahasiswa)
                print(f"Rata-rata: {hasil_nilai['rata_rata']:.2f}")
                print(f"Nilai tertinggi: {hasil_nilai['tertinggi']}")
                print(f"Nilai terendah: {hasil_nilai['terendah']}")
                print(f"Pengelompokan nilai A-E: {hasil_nilai['kelompok_kategori']}")
                print(f"Frekuensi kategori A-E: {hasil_nilai['frekuensi_kategori']}")
            except ValueError as error:
                print("Input nilai tidak valid:", error)

        elif pilihan == "3":
            print("\n=== 3. Analisis beasiswa ===")
            penerima_a = input("ID penerima beasiswa A (pisahkan dengan koma): ").split(",")
            penerima_b = input("ID penerima beasiswa B (pisahkan dengan koma): ").split(",")
            hasil_beasiswa = analisis_beasiswa(
                [x.strip() for x in penerima_a if x.strip()],
                [x.strip() for x in penerima_b if x.strip()],
            )
            for label, nilai in hasil_beasiswa.items():
                print(f"{label.replace('_', ' ').title()}: {sorted(nilai)}")

        elif pilihan == "4":
            print("\n=== 4. Inventaris toko ===")
            inventaris.clear()
            tambah_barang("Buku", 5000, 10)
            tambah_barang("Pulpen", 3000, 20)
            tambah_barang("Tas", 75000, 5)
            update_stok("Pulpen", 25)
            print("Daftar inventaris:", inventaris)
            print("Barang dengan harga Rp3.000-Rp50.000:",
                  cari_barang_berdasarkan_harga(3000, 50000))
            print("Total nilai inventaris: Rp", total_nilai_inventaris(), sep="")

        elif pilihan == "5":
            print("\n=== 5. Analisis file teks ===")
            nama_file = input("Nama/path file teks (contoh: teks.txt): ").strip()
            try:
                hasil_teks = analisis_file_teks(nama_file)
                print("Total kata:", hasil_teks["total_kata"])
                print("Frekuensi setiap kata:", hasil_teks["frekuensi"])
                print("10 kata paling sering:", hasil_teks["10_tersering"])
                print("Hapax legomena:", sorted(hasil_teks["hapax_legomena"]))
                print(f"Rasio kata unik (TTR): {hasil_teks['rasio_kata_unik']:.4f}")
            except FileNotFoundError:
                print(f"File {nama_file!r} tidak ditemukan.")

        elif pilihan == "0":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 5.")


if __name__ == "__main__":
    main()
