import threading

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
    threads = []
    for url in urls:
        thread = threading.Thread(target=print_status, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
