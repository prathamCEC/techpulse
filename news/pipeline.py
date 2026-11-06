
from concurrent.futures import ThreadPoolExecutor, as_completed

from news.fetcher import fetch_tech_news
from news.filter import process_news
from news.summarizer import summarize_article


def generate_news_briefing(category=None, limit=5):

    print("[PIPELINE] Started", flush=True)

    # Step 1: Fetch news
    print("[PIPELINE] Fetching technology news...", flush=True)

    articles = fetch_tech_news()

    print(f"[PIPELINE] Fetched {len(articles)} articles", flush=True)

    if not articles:
        return ["Unable to fetch technology news. Please try again later."]

    # Step 2: Filter news
    print("[PIPELINE] Filtering articles...", flush=True)

    for article in articles:
        print("\n[TITLE]", article.get("title"), flush=True)
        print("[DESCRIPTION]", article.get("description"), flush=True)
        print("[VALID]", process_news([article]), flush=True)

    processed_articles = process_news(articles)

    print(
        f"[PIPELINE] Articles after filtering: {len(processed_articles)}",
        flush=True
    )

    if category:
        processed_articles = [
            article for article in processed_articles
            if article["category"].lower() == category.lower()
        ]

    if not processed_articles:
        return ["No relevant articles found for this category."]

    selected_articles = processed_articles[:limit]

    # Step 3: Summarize articles concurrently
    print("[PIPELINE] Starting parallel summarization...", flush=True)

    summaries = {}

    with ThreadPoolExecutor(max_workers=3) as executor:

        future_to_index = {
            executor.submit(summarize_article, article): index
            for index, article in enumerate(selected_articles)
        }

        for future in as_completed(future_to_index):

            index = future_to_index[future]
            article = selected_articles[index]

            try:
                summary = future.result()

                if summary:
                    summaries[index] = summary
                    print(
                        f"[PIPELINE] Article {index + 1} summarized successfully!",
                        flush=True
                    )
                else:
                    print(
                        f"[PIPELINE] Article {index + 1} returned no summary.",
                        flush=True
                    )

            except Exception as error:
                print(
                    f"[PIPELINE] Error summarizing article {index + 1}: {error}",
                    flush=True
                )

    # Step 4: Format messages in original article order
    messages = []

    for index, article in enumerate(selected_articles):

        summary = summaries.get(index)

        if not summary:
            continue

        message = (
            f"{len(messages) + 1}. {article['title']}\n\n"
            f"📂 Category: {article['category']}\n\n"
            f"📰 Summary:\n{summary['summary']}\n\n"
            f"💡 Why it matters:\n{summary['why_it_matters']}\n\n"
            f"🎯 Key takeaway:\n{summary['key_takeaway']}\n\n"
            f"🔗 Read more: {article['url']}"
        )

        messages.append(message)

    if not messages:
        return ["News was fetched, but summarization failed. Please try again later."]

    print(
        f"[PIPELINE] Completed! Generated {len(messages)} summaries.",
        flush=True
    )

    return messages
