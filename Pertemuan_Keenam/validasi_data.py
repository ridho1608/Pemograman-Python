from collections.abc import Callable
from typing import Any


def validasi_data(
    data: dict[str, Any],
    schema: dict[str, dict[str, Any]],
    *validators: Callable[[dict[str, Any]], bool],
    **field_validators: Callable[[Any], bool],
) -> tuple[bool, list[str]]:
    errors: list[str] = []

    for key, rules in schema.items():
        if key not in data:
            if rules.get("required", True):
                errors.append(f"Kunci '{key}' wajib ada.")
            continue

        value = data[key]
        expected_type = rules.get("type")
        if expected_type is not None and not isinstance(value, expected_type):
            if isinstance(expected_type, tuple):
                expected_name = " atau ".join(item.__name__ for item in expected_type)
            else:
                expected_name = expected_type.__name__
            errors.append(
                f"Field '{key}' harus bertipe {expected_name}, "
                f"mendapat {type(value).__name__}."
            )
            continue

        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "min" in rules and value < rules["min"]:
                errors.append(
                    f"Field '{key}' bernilai {value}, kurang dari batas minimum "
                    f"{rules['min']}."
                )
            if "max" in rules and value > rules["max"]:
                errors.append(
                    f"Field '{key}' bernilai {value}, melebihi batas maksimum "
                    f"{rules['max']}."
                )

    for validator in validators:
        if not validator(data):
            errors.append("Data tidak lolos validasi kustom.")

    for key, validator in field_validators.items():
        if key in data and not validator(data[key]):
            errors.append(f"Field '{key}' tidak lolos validasi kustom.")

    return not errors, errors


if __name__ == "__main__":
    schema_mahasiswa = {
        "nama": {"type": str, "required": True},
        "umur": {"type": int, "min": 17, "max": 60},
        "ipk": {"type": float, "min": 0.0, "max": 4.0},
    }
    data_input = {"nama": "Ridho", "umur": 20, "ipk": 3.75}
    print(validasi_data(data_input, schema_mahasiswa, nama=lambda nama: bool(nama.strip())))
