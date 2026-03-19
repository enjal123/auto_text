from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient
import os

def news_report(countries):

    n_api = os.getenv("NEWS_API_KEY")
    n_io_api = os.getenv("NEWSDATA_API_KEY")

    if not n_api and not n_io_api:
        return "❌ Missing news API keys."

    news_client = NewsApiClient(api_key=n_api) if n_api else None
    global_client = NewsDataApiClient(apikey=n_io_api) if n_io_api else None

    full_report = "📰 NEWS UPDATE\n\n"

    for country in countries:

        full_report += f"🌍 {country.upper()} HEADLINES\n"
        articles_added = 0

        if news_client:
            try:
                response = news_client.get_top_headlines(
                    q=country,
                    language="en",
                    page_size=5
                )

                for article in response.get("articles", []):
                    title = article.get("title")
                    url = article.get("url")

                    if title and url:
                        full_report += f"• {title}\n🔗 {url}\n\n"
                        articles_added += 1

            except Exception as e:
                print(f"NewsAPI error: {e}")

        if articles_added == 0 and global_client:
            try:
                response = global_client.latest_api(
                    q=country,
                    language="en",
                    size=5
                )

                for article in response.get("results", []):
                    title = article.get("title")
                    url = article.get("link")

                    if title and url:
                        full_report += f"• {title}\n🔗 {url}\n\n"
                        articles_added += 1

            except Exception as e:
                print(f"NewsDataAPI error: {e}")

        if articles_added == 0:
            full_report += "No recent headlines found.\n\n"

        full_report += "----------------------\n\n"

    return full_report
