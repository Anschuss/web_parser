from .secondary import main
from config import URL_PLUS_ONE as n_plus_url


def get_all():
    n_plus_one = main(n_plus_url)

    all_preview = {"n_plus_one": n_plus_one}

    return all_preview
