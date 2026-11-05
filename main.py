from news.fetcher import fetch_tech_news
from news.filter import process_news


def main():

    print("\n========== TECHPULSE ==========\n")

    articles = fetch_tech_news()

    if not articles:
        print("No articles found.")
        return

    processed_articles = process_news(articles)

    print(f"\nTotal articles: {len(articles)}")
    print(f"After filtering: {len(processed_articles)}")

    for index, article in enumerate(processed_articles, start=1):

        print(f"\n{index}. {article['title']}")
        print(f"Category: {article['category']}")
        print(f"Source: {article['source']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")

        print("-" * 60)


if __name__ == "__main__":
    main()
