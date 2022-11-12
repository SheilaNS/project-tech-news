import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
