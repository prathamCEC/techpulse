import requests

from config import GNEWS_API_KEY, NEWS_LIMIT

GNEWS_URL = "https://gnews.io/api/v4/top-headlines"


def fetch_tech_news():

    params = {
        "category": "technology",
        "lang": "en",
        "max": NEWS_LIMIT,
        "apikey": GNEWS_API_KEY
    }

    try:
        response = requests.get(
            GNEWS_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        articles = data.get("articles", [])

        news_list = []

        for article in articles:

            news_list.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "source": article.get("source", {}).get("name"),
                "published_at": article.get("publishedAt"),
                "image": article.get("image")
            })

        print(f"Successfully fetched {len(news_list)} articles.")

        return news_list

    except requests.exceptions.RequestException as error:
        print(f"GNews API error: {error}")
        return []

    except ValueError as error:
        print(f"Invalid JSON response: {error}")
        return []
