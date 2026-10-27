import utilitas_akademik as ua


def main() -> None:
    matakuliah = [
        {"nama_mk": "Pemrograman Modern", "sks": 3, "nilai_angka": 88},
        {"nama_mk": "Komputasi Data", "sks": 4, "nilai_angka": 78},
        {"nama_mk": "Basis Data", "sks": 3, "nilai_angka": 92},
    ]
    print(ua.generate_transkrip("Ridho Gustama", "20241320027", matakuliah))


if __name__ == "__main__":
    main()
