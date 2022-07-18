from Netflix.models.conteudo import Conteudo
from Netflix.models.filme import Filme
from Netflix.models.serie import Serie
from Netflix.daos.bd import BancoDados


class ConteudoDAO:

    def __init__(self):
        self.bd = BancoDados()

    def save(self, conteudo: Conteudo):
        self.bd.session.add(conteudo)
        self.bd.session.commit()

    def save_all(self, conteudos: list[Conteudo]):
        for conteudo in conteudos:
            self.bd.session.add(conteudo)
        self.bd.session.commit()

    def find_all(self):
        return self.bd.session.query(Conteudo).all()

    def find_filmes(self):
        return self.bd.session.query(Filme).all()


    def find_by_nome_equals_first(self, nome: str) -> str:
        return self.bd.query(Conteudo).filter(Conteudo._titulo == nome).first()

    def delete(self, conteudo):
        self.bd.session.delete(conteudo)
        self.bd.session.commit()


