from typing import Any

from sistem_informasi.model import Mahasiswa
from sistem_informasi.utils import validasi_mahasiswa

_mahasiswa: dict[str, dict[str, str]] = {}


def create_mahasiswa(mahasiswa: Mahasiswa) -> dict[str, str]:
    record = mahasiswa.to_dict()
    validasi_mahasiswa(record)
    if mahasiswa.npm in _mahasiswa:
        raise ValueError(f"Mahasiswa dengan NPM '{mahasiswa.npm}' sudah terdaftar.")
    _mahasiswa[mahasiswa.npm] = record
    return record.copy()


def get_mahasiswa(npm: str) -> dict[str, str] | None:
    record = _mahasiswa.get(npm)
    return record.copy() if record is not None else None


def list_mahasiswa() -> list[dict[str, str]]:
    return [record.copy() for record in _mahasiswa.values()]


def update_mahasiswa(npm: str, **perubahan: Any) -> dict[str, str]:
    if npm not in _mahasiswa:
        raise KeyError(f"Mahasiswa dengan NPM '{npm}' tidak ditemukan.")
    field_tidak_dikenal = perubahan.keys() - {"nama", "program_studi"}
    if field_tidak_dikenal:
        raise ValueError(f"Field tidak dapat diubah: {', '.join(sorted(field_tidak_dikenal))}.")

    record = {**_mahasiswa[npm], **perubahan}
    validasi_mahasiswa(record)
    _mahasiswa[npm] = record
    return record.copy()


def delete_mahasiswa(npm: str) -> dict[str, str]:
    try:
        return _mahasiswa.pop(npm)
    except KeyError:
        raise KeyError(f"Mahasiswa dengan NPM '{npm}' tidak ditemukan.") from None


if __name__ == "__main__":
    contoh = Mahasiswa("12345", "Nama Mahasiswa", "Informatika")
    create_mahasiswa(contoh)
    print(get_mahasiswa("12345"))
