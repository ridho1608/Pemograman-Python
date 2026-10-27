from dataclasses import asdict, dataclass


@dataclass
class Mahasiswa:
    npm: str
    nama: str
    program_studi: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


if __name__ == "__main__":
    print(Mahasiswa("12345", "Nama Mahasiswa", "Informatika").to_dict())
