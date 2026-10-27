import math


def konversi_nilai_huruf(nilai_angka: float) -> str:
    if (
        isinstance(nilai_angka, bool)
        or not isinstance(nilai_angka, (int, float))
        or not math.isfinite(nilai_angka)
        or not 0 <= nilai_angka <= 100
    ):
        raise ValueError("Nilai angka harus berada pada rentang 0 sampai 100.")
    if nilai_angka >= 85:
        return "A"
    if nilai_angka >= 75:
        return "B"
    if nilai_angka >= 65:
        return "C"
    if nilai_angka >= 50:
        return "D"
    return "E"


def hitung_ipk(matakuliah: list[dict[str, int | float | str]]) -> float:
    peta_bobot = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
    total_bobot = 0.0
    total_sks = 0

    for mata_kuliah in matakuliah:
        sks = mata_kuliah["sks"]
        if isinstance(sks, bool) or not isinstance(sks, int) or sks <= 0:
            raise ValueError("SKS setiap mata kuliah harus berupa bilangan bulat positif.")
        huruf = konversi_nilai_huruf(mata_kuliah["nilai_angka"])
        total_bobot += peta_bobot[huruf] * sks
        total_sks += sks

    return round(total_bobot / total_sks, 2) if total_sks else 0.0


def generate_transkrip(
    nama: str, npm: str, matakuliah: list[dict[str, int | float | str]]
) -> str:
    ipk = hitung_ipk(matakuliah)
    transkrip = (
        f"=== TRANSKRIP AKADEMIK ===\nNama : {nama}\nNPM  : {npm}\n"
        f"IPK  : {ipk:.2f}\n---------------------------\n"
    )
    for mata_kuliah in matakuliah:
        huruf = konversi_nilai_huruf(mata_kuliah["nilai_angka"])
        transkrip += (
            f"- {mata_kuliah['nama_mk']} ({mata_kuliah['sks']} SKS): {huruf}\n"
        )
    return transkrip


if __name__ == "__main__":
    contoh_matakuliah = [{"nama_mk": "Python", "sks": 3, "nilai_angka": 90}]
    print(generate_transkrip("Test Student", "12345", contoh_matakuliah))
