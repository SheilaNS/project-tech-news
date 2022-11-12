import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    links = selector.css("a.next::attr(href)").get()
    return links


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": len(selector.css(".content-list li").getall()),
        "summary": "".join(
            selector.css(
                "div.entry-content > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css(".label::text").get(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []

    while len(news) <= amount:
        html = fetch(url)
        news_list = scrape_novidades(html)
        for news_url in news_list:
            details = fetch(news_url)
            news_details = scrape_noticia(details)
            news.append(news_details)
        url = scrape_next_page_link(html)

    news = news[:amount]
    create_news(news)
    return news
