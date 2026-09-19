"""
Personal Data Analytics Portfolio - Task 1: Web Scraping
Source: Books to Scrape (https://books.toscrape.com/)
This website is designed for scraping practice.
"""

import csv
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT = Path(__file__).parent / "data" / "books.csv"


def scrape_books(max_pages=5):
    rows = []

    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        print(f"Scraping page {page}: {url}")

        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 CodeAlpha Internship Project"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a.get("title", "").strip()
            price_text = book.select_one(".price_color").get_text(strip=True)
            rating_class = book.select_one("p.star-rating").get("class", [])

            rating_words = {
                "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
            }
            rating = next(
                (rating_words[word] for word in rating_words if word in rating_class),
                None
            )

            availability = book.select_one(".availability").get_text(" ", strip=True)

            rows.append({
                "title": title,
                "price_gbp": float(price_text.replace("£", "")),
                "rating": rating,
                "availability": availability,
                "page": page,
            })

        time.sleep(0.5)

    return rows


def save_csv(rows):
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} records to {OUTPUT}")


if __name__ == "__main__":
    try:
        data = scrape_books(max_pages=5)
        save_csv(data)
    except Exception as exc:
        print("\nScraping failed.")
        print("Check your internet connection and try again.")
        print(f"Error: {exc}")
