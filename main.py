from news.fetcher import fetch_tech_news


def main():

    print("\n========== TECHPULSE ==========")
    print("Fetching technology news...\n")

    articles = fetch_tech_news()

    if not articles:
        print("No articles available.")
        return

    for index, article in enumerate(articles, start=1):

        print(f"\n{index}. {article['title']}")
        print(f"Source: {article['source']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
