import feedparser


def get_headlines(rss_url):
    """
    Extracts titles from an RSS feed located at `rss_url`.

    @param rss_url: URL of the RSS feed
    @returns: a list of titles from the RSS feed
    """

    feed = feedparser.parse(rss_url)

    return [entry.title for entry in feed.entries]


google_news_url = "https://news.google.com/news/rss"
print(get_headlines(google_news_url))
