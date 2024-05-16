import requests

urls = [
    "https://google.com",
    "https://youtube.com",
    "https://facebook.com",
    "https://instagram.com",
    "https://linkedin.com",
    "https://pinterest.com",
    "https://github.com",
    "https://gitlab.com",
]


def print_status(url: str) -> None:
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")


def main() -> None:
    for url in urls:
        print_status(url=url)


if __name__ == "__main__":
    main()
