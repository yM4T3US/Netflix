from Netflix.models.pessoa import Pessoa
from Netflix.daos.bd import BancoDados

class PessoaDAO:

    def __init__(self):
        self.bd = BancoDados()

    def save(self, pessoa: Pessoa):
        self.bd.session.add(pessoa)
        self.bd.session.commit()

    def save_all(self, pessoas: list[Pessoa]):
        for pessoa in pessoas:
            self.bd.session.add(pessoa)
        self.bd.session.commit()

    def find_all(self):
        return self.bd.session.query(Pessoa).all()

    def find_by_nome(self, nome: str) -> list:
        return self.bd.session.query(Pessoa._nome.ilike(f"%{nome}")).all()

    def find_by_nome_equals(self, nome: str) -> list:
        return self.bd.session.query(Pessoa).filter(Pessoa._nome == nome).first()

    def delete(self, pessoa):
        self.bd.session.delete(pessoa)
        self.bd.session.commit()



