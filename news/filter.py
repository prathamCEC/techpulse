import re


CATEGORY_KEYWORDS = {
    "AI": [
        "artificial intelligence", "openai", "chatgpt",
        "machine learning", "deep learning", "llm",
        "generative ai", "ai model", "ai agent",
        "gemini", "claude", "grok", "neural network"
    ],

    "Cybersecurity": [
        "cybersecurity", "hacking", "data breach",
        "vulnerability", "malware", "ransomware",
        "security flaw", "cyber attack", "zero-day",
        "phishing", "encryption"
    ],

    "Startups": [
        "startup", "funding", "venture capital",
        "acquisition", "series a", "series b",
        "seed funding", "valuation"
    ],

    "Big Tech": [
        "google", "microsoft", "apple", "meta",
        "nvidia", "amazon", "intel", "samsung"
    ],

    "Developer Tools": [
        "python", "javascript", "github", "developer",
        "programming", "software development",
        "framework", "open source", "database",
        "api", "linux"
    ],

    "Hardware": [
        "processor", "gpu", "cpu", "chip",
        "semiconductor", "graphics card",
        "smartphone", "laptop", "data center"
    ],

    "Science & Emerging Technology": [
        "quantum computing", "robotics",
        "space technology", "biotechnology",
        "scientific research", "renewable energy",
        "solar cells", "autonomous systems"
    ],

    "Gaming Technology": [
        "game engine", "gaming hardware",
        "graphics technology", "cloud gaming",
        "game development", "virtual reality",
        "augmented reality"
    ]
}


EXCLUDED_KEYWORDS = [
    "merchandise", "playable toy", "store stock",
    "lowest price", "discount", "shopping deal",
    "buy now", "product review", "coupon"
]


TECH_INDICATORS = [
    # General technology
    "technology", "tech", "digital", "computer",
    "software", "hardware", "internet", "online",

    # AI
    "artificial intelligence", "ai", "machine learning",
    "deep learning", "llm", "chatgpt", "siri",
    "generative ai", "ai model",

    # Devices and hardware
    "smartphone", "iphone", "android", "laptop",
    "processor", "gpu", "cpu", "chip",
    "semiconductor", "graphics card", "qi2",
    "charger", "display", "oled", "snapdragon",

    # Cybersecurity
    "cybersecurity", "malware", "ransomware",
    "data breach", "vulnerability", "phishing",
    "security flaw", "zero-day",

    # Development
    "programming", "developer", "github",
    "javascript", "python", "api", "database",
    "open source", "framework",

    # Emerging technology
    "robotics", "quantum computing", "biotechnology",
    "cloud computing", "data center", "autonomous systems",

    # Gaming technology
    "gaming hardware", "game engine", "cloud gaming",
    "virtual reality", "augmented reality"
]


def normalize_text(text):
    """Normalize text for matching."""

    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)

    return " ".join(text.split())


def is_valid_article(article):
    """Check whether an article contains essential information."""

    title = article.get("title")
    url = article.get("url")

    if not title or not url:
        return False

    if not url.startswith(("http://", "https://")):
        return False

    if len(title.strip()) < 15:
        return False

    return True


def is_relevant(article):
    title = normalize_text(article.get("title") or "")
    description = normalize_text(article.get("description") or "")

    content = f"{title} {description}"

    # Reject promotional and shopping content
    if any(keyword in content for keyword in EXCLUDED_KEYWORDS):
        return False

    # Accept articles containing technology indicators
    if any(
        normalize_text(keyword) in content
        for keyword in TECH_INDICATORS
    ):
        return True

    return False


def categorize_article(article):
    """Assign a technology category to an article."""

    content = normalize_text(
        f"{article.get('title') or ''} "
        f"{article.get('description') or ''}"
    )

    for category, keywords in CATEGORY_KEYWORDS.items():

        if any(normalize_text(keyword) in content for keyword in keywords):
            return category

    return "General Technology"


def remove_duplicates(articles):
    """Remove duplicate articles using URLs and titles."""

    unique_articles = []
    seen_urls = set()
    seen_titles = set()

    for article in articles:

        url = article.get("url")
        title = normalize_text(article.get("title") or "")

        if url and url in seen_urls:
            continue

        if title and title in seen_titles:
            continue

        if url:
            seen_urls.add(url)

        if title:
            seen_titles.add(title)

        unique_articles.append(article)

    return unique_articles


def process_news(articles):
    """Run the complete news filtering pipeline."""

    valid_articles = [
        article for article in articles
        if is_valid_article(article)
    ]

    relevant_articles = [
        article for article in valid_articles
        if is_relevant(article)
    ]

    unique_articles = remove_duplicates(relevant_articles)

    for article in unique_articles:
        article["category"] = categorize_article(article)

    return unique_articles
