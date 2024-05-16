import asyncio

import aiohttp

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


async def print_status(session: aiohttp.ClientSession, url: str) -> None:
    async with session.get(url=url) as response:
        print(f"URL: {url}, Status Code: {response.status}")


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        tasks = (print_status(session=session, url=url) for url in urls)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
