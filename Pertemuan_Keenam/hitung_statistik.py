import math
import statistics


def hitung_statistik(data: list[float]) -> dict[str, float | int | None]:
    if not data:
        raise ValueError("List angka tidak boleh kosong.")
    if any(
        isinstance(angka, bool)
        or not isinstance(angka, (int, float))
        or not math.isfinite(angka)
        for angka in data
    ):
        raise TypeError("Semua elemen harus berupa angka yang finite.")

    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": statistics.mode(data),
        "range": max(data) - min(data),
        "std_dev": statistics.stdev(data) if len(data) > 1 else 0.0,
    }


if __name__ == "__main__":
    print(hitung_statistik([10, 20, 20, 30, 40, 50, 60, 70, 80]))
