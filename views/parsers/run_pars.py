from app import client

from .dw.dw_parser import dw
from .nplus.n_plus_parser import n_plus
from config import URL_PLUS_ONE, URL_DW


@client.task
def run():
    dw(URL_DW)
    n_plus(URL_PLUS_ONE)
