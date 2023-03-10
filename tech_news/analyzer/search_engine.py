from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    return [
        (news["title"], news["url"])
        for news in search_news({"title": {"$regex": title, "$options": "i"}})
    ]


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        list = search_news({"timestamp": format_date})
        return [(news["title"], news["url"]) for news in list]
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 8
def search_by_tag(tag):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
        )
    ]


# Requisito 9
def search_by_category(category):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"category": {"$regex": category, "$options": "i"}}
        )
    ]
