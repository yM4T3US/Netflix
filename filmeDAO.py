from Netflix.daos.conteudoDAO import ConteudoDAO
from Netflix.models.filme import Filme
from Netflix.daos.bd import BancoDados

class FilmeDAO(ConteudoDAO):

    def __init__(self):
        super().__init__()

        self.bd = BancoDados()

    def find_filmes(self):
        return self.bd.session.query(Filme).all()

