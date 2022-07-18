from Netflix.models.perfil import Perfil
from Netflix.daos.bd import BancoDados

class PerfilDAO:

    def __init__(self):
        self.bd = BancoDados()

    def save(self, perfil: Perfil):
        self.bd.session.add(perfil)
        self.bd.session.commit()

    def save_all(self, perfis: list[Perfil]):
        for perfil in perfis:
            self.bd.session.add(perfil)
        self.bd.session.commit()

    def find_all(self):
        return self.bd.session.query(Perfil).all()

    def find_by_nome(self, nome: str) -> list:
        return self.bd.session.query(Perfil._nome.ilike(f"%{nome}")).all()

    def find_by_nome_equals(self, nome: str) -> list:
        return self.bd.session.query(Perfil).filter(Perfil._nome == nome).all()

    # def find_by_nome_equals_first(self, nome: str) -> str:
    #     return self.bd.session.query(Perfil).filter(Perfil._nome.ilike(f"%{nome}%")).first()

    def find_by_nome_equals_first(self, nome: str) -> str:
        return self.bd.session.query(Perfil).filter(Perfil._nome == nome).first()

    def delete(self, perfil):
        self.bd.session.delete(perfil)
        self.bd.session.commit()






