import feedparser
import requests

RSS_URL = "https://rss.app/feeds/_bvBYLagJbGW6KZ0s.xml"
BOT_TOKEN = "8476480136:AAFesF5j0llmTtc-vToUkRGniWfRTRDYF94"
CHAT_ID = "@alfaqarrr"

feed = feedparser.parse(RSS_URL)

entry = feed.entries[0]

title = entry.title
link = entry.link

message = f"{title}\n{link}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})