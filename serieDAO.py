from Netflix.daos.conteudoDAO import ConteudoDAO
from Netflix.models.serie import Serie
from Netflix.daos.bd import BancoDados

class SerieDAO(ConteudoDAO):

    def __init__(self):
        super().__init__()

        self.bd = BancoDados()

    def find_series(self):
        return self.bd.session.query(Serie).all()