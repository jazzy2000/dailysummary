import feedparser

print("Hello, World!")

def getViennaNews():
    feed = feedparser.parse("https://rss.orf.at/news.xml")

    for entry in feed.entries:
        title = entry.title
       # published = entry.date

        print(title)
        #print(published)

def getGlobalNews():
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")

    for entry in feed.entries:
        title = entry.title
       # published = entry.date

        print(title)
        #print(published)

getViennaNews()
getGlobalNews()
