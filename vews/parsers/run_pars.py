from app import client

from .bbc.bbc_parser import bbc
from .dw.dw_parser import dw
from .nplus.n_plus_parser import n_plus
from config import URL_PLUS_ONE, URL_DW, URL_BBC


@client.task(bind=True)
def run(self):
    bbc(URL_BBC)
    dw(URL_DW)
    n_plus(URL_PLUS_ONE)
