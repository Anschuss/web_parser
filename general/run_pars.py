from .secondary import n_pluse_one, bbc
from config import URL_PLUS_ONE as n_plus_url, URL_BBC as bbc_url


def get_all():
    n_plus = n_pluse_one(n_plus_url)
    bbc_news = bbc(bbc_url)
    all_preview = [n_plus, bbc_news]

    return all_preview
