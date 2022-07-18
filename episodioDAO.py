from Netflix.models.episodio import Episodio
from Netflix.daos.bd import BancoDados

class EpisodioDAO:

    def __init__(self):
        self.bd = BancoDados()

    def save(self, episodio: Episodio):
        self.bd.session.add(episodio)
        self.bd.session.commit()

    def save_all(self, episodios: list[Episodio]):
        for episodio in episodios:
            self.bd.session.add(episodio)
        self.bd.session.commit()

    def find_all(self):
        return self.bd.session.query(Episodio).all()

    def find_by_nome(self, nome: str) -> list:
        return self.bd.session.query(Episodio._nome.ilike(f"%{nome}")).all()

    def find_by_nome_equals(self, nome: str) -> list:
        return self.bd.session.query(Episodio).filter(Episodio._nome == nome).all()

    def find_by_nome_equals(self, nome: str) ->str:
        return self.bd.session.query(Episodio).filter(Episodio._nome == nome).first()

    def delete(self, episodio):
        self.bd.session.delete(episodio)
        self.bd.session.commit()