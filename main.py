from news.fetcher import fetch_tech_news
from news.filter import process_news
from bot.telegram_bot import run_bot


def main():

    print("\n========== TECHPULSE ==========\n")
    print("Fetching technology news...\n")

    articles = fetch_tech_news()

    if not articles:
        print("No articles found.")
        return

    processed_articles = process_news(articles)

    print(f"Fetched: {len(articles)}")
    print(f"After filtering: {len(processed_articles)}")

    for index, article in enumerate(processed_articles, start=1):

        print(f"\n{index}. {article['title']}")
        print(f"Category: {article['category']}")
        print(f"Source: {article['source']}")
        print(f"Description: {article['description']}")
        print(f"Published: {article['published_at']}")
        print(f"URL: {article['url']}")

        print("-" * 60)


if __name__ == "__main__":
    run_bot()