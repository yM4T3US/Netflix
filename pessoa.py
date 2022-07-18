from datetime import date
from sqlalchemy import Column, Integer, Date, String
from Netflix.daos.bd import BancoDados


class Pessoa(BancoDados.Base):

    __tablename__ = "pessoas"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    _nome = Column(String, nullable=False)
    _data_nascimento = Column(Date, nullable=False)


    def __init__(self, nome: str, data_nascimento: date):

        self._nome = nome
        self._data_nascimento = data_nascimento
        self._trabalhos = []

    def __str__(self):
        return (f"Nome: {self._nome}\n"
                f"Data de nascimento: {self._data_nascimento}\n")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            if nome != self._nome:
                self._nome = nome
        raise TypeError("Nome inválido")

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if not hasattr(self, "_data_nascimento"):
            self._data_nascimento = None
        elif data_nascimento < date.today():
            self._data_nascimento = data_nascimento
        else:
            raise ValueError("Data de nascimento deve ser do tipo datetime e ser menor que a atual.")

    @property
    def trabalhos(self):
        copia_trabalhos = self._trabalhos
        return copia_trabalhos

    @trabalhos.setter
    def trabalhos(self, trabalhos):
        if not hasattr(self, "_trabalhos"):
            self._trabalhos = None
        else:
            for x in trabalhos:
                for conteudo, cargo in x:
                    if isinstance(conteudo, str) and isinstance(cargo, str):
                        teste = True
                    else:
                        raise TypeError
            if teste:
                self._trabalhos = trabalhos

    def adicionar_trabalho(self, cont):
        self.trabalhos.append(cont)






