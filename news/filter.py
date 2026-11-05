import re
from urllib.parse import urlparse


CATEGORY_KEYWORDS = {
    "AI": [
        "artificial intelligence", "openai", "chatgpt",
        "machine learning", "deep learning", "llm",
        "generative ai", "ai model", "ai agent"
    ],

    "Cybersecurity": [
        "cybersecurity", "hacking", "data breach",
        "vulnerability", "malware", "ransomware",
        "security flaw", "cyber attack"
    ],

    "Startups": [
        "startup", "funding", "venture capital",
        "acquisition", "series a", "series b"
    ],

    "Big Tech": [
        "google", "microsoft", "apple", "meta",
        "nvidia", "amazon", "intel"
    ],

    "Developer Tools": [
        "python", "javascript", "developer",
        "programming", "github", "framework",
        "software development"
    ]
}


def normalize_text(text):
    """Normalize text for duplicate detection."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())


def remove_duplicates(articles):

    unique_articles = []
    seen_urls = set()
    seen_titles = set()

    for article in articles:

        url = article.get("url")
        title = article.get("title")

        normalized_title = normalize_text(title or "")

        if url and url in seen_urls:
            continue

        if normalized_title and normalized_title in seen_titles:
            continue

        if url:
            seen_urls.add(url)

        if normalized_title:
            seen_titles.add(normalized_title)

        unique_articles.append(article)

    return unique_articles


def categorize_article(article):

    text = normalize_text(
        f"{article.get('title') or ''} "
        f"{article.get('description') or ''}"
    )

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if normalize_text(keyword) in text:
                return category

    return "General Technology"


def process_news(articles):

    unique_articles = remove_duplicates(articles)

    processed_articles = []

    for article in unique_articles:

        article["category"] = categorize_article(article)

        processed_articles.append(article)

    return processed_articles
