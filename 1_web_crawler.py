import json
from dataclasses import dataclass, asdict
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com/"


@dataclass
class Quote:
    text: str
    author: str
    tags: List[str]


def parse_quotes_from_html(html: str) -> List[Quote]:
    """단일 페이지 HTML에서 인용구 목록을 파싱합니다."""
    soup = BeautifulSoup(html, "html.parser")
    quote_elements = soup.select("div.quote")

    quotes: List[Quote] = []
    for q in quote_elements:
        text = q.select_one("span.text").get_text(strip=True)
        author = q.select_one("small.author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.select("div.tags a.tag")]
        quotes.append(Quote(text=text, author=author, tags=tags))

    return quotes


def get_next_page_url(html: str, current_url: str) -> str | None:
    """다음 페이지 링크가 있으면 절대 URL을 반환하고, 없으면 None 반환."""
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next > a")
    if not next_link:
        return None
    href = next_link.get("href")
    return urljoin(current_url, href)


def crawl_quotes(start_url: str = BASE_URL, timeout: int = 10) -> List[Quote]:
    """quotes.toscrape.com의 전체 페이지를 순회하며 quote 데이터를 수집합니다."""
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        }
    )

    all_quotes: List[Quote] = []
    current_url = start_url

    while current_url:
        response = session.get(current_url, timeout=timeout)
        response.raise_for_status()

        html = response.text
        all_quotes.extend(parse_quotes_from_html(html))
        current_url = get_next_page_url(html, current_url)

    return all_quotes


def save_quotes_to_json(quotes: List[Quote], output_file: str = "quotes.json") -> None:
    """수집한 quote 목록을 JSON 파일로 저장합니다."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump([asdict(q) for q in quotes], f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    quotes = crawl_quotes()
    save_quotes_to_json(quotes)

    print(f"총 {len(quotes)}개의 quote를 수집하여 quotes.json에 저장했습니다.")
    print("\n[크롤링 결과 전체 출력]")

    for idx, quote in enumerate(quotes, start=1):
        print(f"\n{idx}. {quote.text}")
        print(f"   - author: {quote.author}")
        print(f"   - tags: {', '.join(quote.tags) if quote.tags else '(없음)'}")