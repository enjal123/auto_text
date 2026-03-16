from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient
import os
def news_report(countries):

    n_api = os.getenv("NEWS_API_KEY")
    n_io__api = os.getenv("NEWSDATA_API_KEY")

    news_client = NewsApiClient(api_key=n_api)
    global_client = NewsDataApiClient(apikey=n_io__api)

    full_report = "📰 NEWS UPDATE\n\n"

    for country in countries:

        full_report += f"🌍 {country.upper()} HEADLINES\n"

        articles_added = 0

        # -------- TRY NEWSAPI FIRST --------
        try:
            response = news_client.get_top_headlines(
                q=country,
                language="en",
                page_size=5
            )

            articles = response.get("articles", [])

            for article in articles:
                title = article.get("title")
                url = article.get("url")

                if title and url:
                    full_report += f"• {title}\n🔗 {url}\n\n"
                    articles_added += 1

        except Exception as e:
            print(f"NewsAPI error for {country}: {e}")


        # -------- FALLBACK TO NEWSDATAAPI --------
        if articles_added == 0:
            try:
                response = global_client.latest_api(
                    q=country,
                    language="en",
                    size=5
                )

                articles = response.get("results", [])

                for article in articles:
                    title = article.get("title")
                    url = article.get("link")

                    if title and url:
                        full_report += f"• {title}\n🔗 {url}\n\n"
                        articles_added += 1

            except Exception as e:
                print(f"NewsDataAPI error for {country}: {e}")


        if articles_added == 0:
            full_report += "No recent headlines found.\n\n"

        full_report += "----------------------\n\n"

    return full_report