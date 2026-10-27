from typing import Any


def validasi_mahasiswa(data: dict[str, Any]) -> None:
    for field in ("npm", "nama", "program_studi"):
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Field '{field}' wajib berupa teks yang tidak kosong.")


if __name__ == "__main__":
    validasi_mahasiswa(
        {"npm": "12345", "nama": "Nama Mahasiswa", "program_studi": "Informatika"}
    )
