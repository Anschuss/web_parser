from vews import News
from app import db


def write_news(name: str, text: dict, url: str):
    old_news = News.query.filter(News.name == name).first()
    db.session.delete(old_news)
    db.session.commit()
    news = News(name=name, title=text["title"], img=text["img"], body=text["body"], url=url)
    db.session.add(news)
    db.session.commit()