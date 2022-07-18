from Netflix.models.conteudo import Conteudo
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey





class Filme(Conteudo):

    __tablename__ = "filmes"

    acervo = []

    id_filme = Column(Integer, primary_key=True)
    _idioma = Column(String, nullable=True)
    _classificacao = Column(Integer, nullable=True)
    duracao = Column(Integer, nullable=False)
    conteudo = Column(Integer, ForeignKey("conteudo.id"))




    def __init__(self, titulo: str, data_lancamento: date,
                 data_expiracao: float, genero: str, duracao: int):
        super().__init__(titulo, genero, data_expiracao, data_lancamento)


        self._idioma = None
        self._classificacao = None
        self.duracao = duracao
        Filme.acervo.append(self)

    def __str__(self):
        return (f"\n{10 * ' '}{Conteudo.__str__(self)}"
                f"Idioma: {self._idioma}\n"
                f"Classificação: {self._classificacao}\n"
                f"Duração: {self.__duracao}")

    @property
    def idioma(self):
        return self._idioma

    @idioma.setter
    def idioma(self, novo_idioma):
        if isinstance(novo_idioma, str):
            if novo_idioma != self._idioma:
                self._idioma = novo_idioma
            else:
                raise TypeError("Idioma inválido")

    @property
    def classificacao(self):
        return self._classificacao

    @classificacao.setter
    def classificacao(self, nova_classificacao):
        if isinstance(nova_classificacao, int):
            if nova_classificacao != self._classificacao:
                self._classificacao = nova_classificacao
            else:
                raise TypeError("Classificação inválida")

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: int):
        if not hasattr(self, "_duracao"):
            self.__duracao = None
        if duracao >= 60 and isinstance(duracao, int):
            self.__duracao = duracao
        else:
            raise ValueError("Duração mínima do filme deve ser 60 minutos e do tipo inteiro.")


    def gerar_indicacoes(self) -> list["Filme"]:
        melhores_filmes = []
        for objeto in Filme.acervo:
            if objeto.nota > 95.0:
                melhores_filmes.append(objeto)
        return melhores_filmes





