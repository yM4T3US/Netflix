from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from Netflix.daos.bd import BancoDados



class Conteudo(BancoDados.Base):

    __tablename__ = "conteudo"

    id = Column(Integer, primary_key=True)
    _identificacao = Column(Integer)
    _titulo = Column(String)
    _nota = Column(Float)
    _genero = Column(String)
    _descricao = Column(String)
    data_lancamento = Column(Date)
    _data_expiracao = Column(Date)
    filme = relationship("Filme")
    # type = Column(String)


    conteudos = []

    def __init__(self, titulo: str, data_lancamento: date, data_expiracao: float, genero: str):

        self._identificacao = None
        self._titulo = titulo
        self._nota = None
        self._descricao = None
        self.data_lancamento = data_lancamento
        self._data_expiracao = data_expiracao
        self._diretor = None
        self._elenco = None
        self._genero = genero
        self._tag = []
        Conteudo.conteudos.append(self)

    def __str__(self):
        return (f"\n{10 * ' '}Id: {self._id}\n"
                f"{10 * ' '}Titulo: {self._titulo}\n"
                f"{10 * ' '}Nota: {self._nota}\n"
                f"{10 * ' '}Descrição: {self._descricao}\n"
                f"{10 * ' '}Data de lançamento: {self._data_lancamento}\n"
                f"{10 * ' '}Data de expiração: {self._data_expiracao}\n"
                f"{10 * ' '}Diretor: {self._diretor}\n"
                f"{10 * ' '}Elenco: {self._elenco}\n"
                f"{10 * ' '}Gênero: {self._genero}\n"
                f"{10 * ' '}Tag: {self._tag}\n")


    @property
    def identificacao(self):
        return self._identificacao

    @identificacao.setter
    def identificacao(self, nova_id):
        if isinstance(nova_id, int):
            if nova_id != self._id:
                self._identificacao = nova_id
        else:
            raise TypeError("Id inválida")

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str):
            if novo_titulo != self._titulo:
                self._titulo = novo_titulo
        else:
            raise TypeError("Titulo inválido")

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nova_nota):
        if isinstance(nova_nota, float):
            if nova_nota != self._nota:
                self._nota = nova_nota
        else:
            raise TypeError("Nota inválida")

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if isinstance(nova_descricao, str):
            if nova_descricao != self._descricao:
                self._descricao = nova_descricao
        else:
            raise TypeError("Descrição inválida")

    @property
    def data_lancamento(self):
        return self._data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, data_lancamento: date):
        if not hasattr(self, "_data_lancamento"):
            self._data_lancamento = None
        if data_lancamento != date.today():
            self._data_lancamento = data_lancamento
        else:
            raise ValueError("Data de lançamento deve ser diferente da atual e do tipo datetime.")

    @property
    def data_expiracao(self):
        return self._data_expiracao

    @data_expiracao.setter
    def data_expiracao(self, data_expiracao: float):
        if not hasattr(self, "_data_expiracao"):
            self._data_expiracao = None
        if isinstance(data_expiracao, float) and data_expiracao >= 30:
            self._data_expiracao = data_expiracao
        else:
            raise ValueError("Data de expiração deve ser do tipo float e maior que 30 dias a partir da atual.")

    @property
    def diretor(self):
        return self._diretor

    @diretor.setter
    def diretor(self, novo_diretor):
        if isinstance(novo_diretor, str):
            if novo_diretor != self._diretor:
                self._diretor = novo_diretor
        else:
            raise TypeError("Diretor inválido")

    @property
    def elenco(self):
        copia_elenco = self._elenco
        return copia_elenco

    @elenco.setter
    def elenco(self, novo_elenco):
        for artista in novo_elenco:
            if isinstance(artista, str):
                teste = True
            else:
                raise TypeError("Elenco inválido")
        if teste:
            self._elenco = novo_elenco

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        if isinstance(genero, str):
            if genero != self._genero:
                self._genero = genero
        else:
            raise TypeError("Gênero inválido")

    @property
    def tag(self) -> list[str]:
        copia_tag = self._tag
        return copia_tag

    @tag.setter
    def tag(self, nova_tag):
        for tag in nova_tag:
            if isinstance(tag, str):
                teste = True
            else:
                raise TypeError("Tag inválida")
        if teste:
            self._tag = nova_tag

    def alterar_genero(self, genero: str) -> bool:
        self._genero = genero

    def incrementar_prazo(self, data: date) -> bool:
        self._data_expiracao += data

    def inserir_avaliacao(self, nota: float) -> float:
        self._nota = nota

    def inserir_tag(self, tag: list[str]) -> bool:
        self._tag.append(tag)

    def remover_tag(self, tag: str) -> bool:
        self._tag.remove(tag)








