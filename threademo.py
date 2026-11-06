
from concurrent.futures import ThreadPoolExecutor
import time


def process_article(article):
    print(f"Processing: {article}")

    time.sleep(3)  # Simulate API latency

    print(f"Completed: {article}")

    return f"{article} summarized"


articles = ["Article 1", "Article 2", "Article 3"]

start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:

    results = executor.map(process_article, articles)

for result in results:
    print(result)

end = time.time()

print(f"Total time: {end - start:.2f} seconds")
