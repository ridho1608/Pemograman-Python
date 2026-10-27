import json
from pathlib import Path

import requests


def analisis_post(url: str, file_output: str = "hasil_analisis.json") -> list[dict[str, int | str]]:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    posts = response.json()

    post_user_1 = filter(lambda post: post["userId"] == 1, posts)
    post_terpilih = map(
        lambda post: {
            "id": post["id"],
            "title": post["title"],
            "title_length": len(post["title"]),
        },
        post_user_1,
    )
    hasil = sorted(post_terpilih, key=lambda post: post["title_length"], reverse=True)

    with Path(file_output).open("w", encoding="utf-8") as file:
        json.dump(hasil, file, indent=4, ensure_ascii=False)
    return hasil


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts"
    hasil = analisis_post(url)
    print(f"Berhasil memproses {len(hasil)} data dan menyimpannya ke hasil_analisis.json.")


if __name__ == "__main__":
    main()
