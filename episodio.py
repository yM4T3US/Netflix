from datetime import date
from Netflix.models.pessoa import Pessoa
from sqlalchemy import Column, Integer, String, Date
from Netflix.daos.bd import BancoDados


class Episodio(BancoDados.Base):

    __tablename__ = "episódios"

    id = Column(Integer, primary_key=True)
    _nr = Column(Integer, nullable=False)
    _nome = Column(String, nullable=False)
    _data_lancamento = Column(Date)
    _temporada = Column(String, nullable=False)
    _resumo = Column(String)


    def __init__(self, nr: int, nome: str, temporada: str):
        self._nr = nr
        self._nome = nome
        self._data_lancamento = None
        self._temporada = temporada
        self._resumo = None
        self._participacao = None

    def __str__(self):
        return (f"\n{20 * ' '}Nr: {self._nr}\n"
                f"{20 * ' '}Nome: {self._nome}\n"
                f"{20 * ' '}Data de lançamento: {self._data_lancamento}\n"
                f"{20 * ' '}Temporada: {self._temporada}\n"
                f"{20 * ' '}Resumo: {self._resumo}\n"
                f"{20 * ' '}Participação: {self._participacao}")

    @property
    def nr(self):
        return self._nr

    @nr.setter
    def nr(self, novo_nr):
        if isinstance(novo_nr, int):
            if novo_nr != self._nr:
                self._nr = novo_nr
        else:
            raise TypeError("Novo número inválido")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            if novo_nome != self._nome:
                self._nome = novo_nome
        else:
            raise TypeError("Nome inválido")

    @property
    def data_lancamento(self):
        return self._data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, nova_data):
        if isinstance(nova_data, date):
            if nova_data != self._data_lancamento:
                self._data_lancamento = nova_data
        else:
            raise TypeError("Data de lançamento inválida")

    @property
    def temporada(self):
        return self._temporada

    @temporada.setter
    def temporada(self, nova_temporada):
        if isinstance(nova_temporada, str):
            if nova_temporada != self._temporada:
                self._temporada = nova_temporada
        else:
            raise TypeError("Temporada inválida")

    @property
    def resumo(self):
        return self._resumo

    @resumo.setter
    def resumo(self, novo_resumo):
        if isinstance(novo_resumo, str):
            if novo_resumo != self._resumo:
                self._resumo = novo_resumo
        else:
            raise TypeError("Resumo inválido")

    @property
    def participacao(self):
        copia_participacao = self._participacao
        return copia_participacao

    @participacao.setter
    def participacao(self, nova_participacao):
        for participacao in nova_participacao:
            if isinstance(participacao, Pessoa):
                teste = True
            else:
                raise TypeError("Participação inválida")
        if teste:
            self._participacao = nova_participacao

    def adicionar_participacao(self, pe: Pessoa) -> bool:
        self.participacao.append(pe.nome)
        return True



