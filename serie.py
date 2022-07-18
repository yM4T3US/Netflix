from Netflix.models.pessoa import Pessoa
from Netflix.models.episodio import Episodio
from Netflix.models.conteudo import Conteudo
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Serie(Conteudo):

    __tablename__ = "series"

    id_serie = Column(Integer, primary_key=True)
    conteudo = Column(Integer, ForeignKey("conteudo.id"))

    __mapper_args__ = {
        "polymorphic_identity": "series",
    }

    def __init__(self, titulo: str, genero: str, data_lancamento: date, data_expiracao: date, temporada: list[str]):

        super().__init__(titulo, genero, data_lancamento, data_expiracao)

        self._temporada = temporada
        self._criadores = []
        self._episodios = []

    def __str__(self):
        return (f"{Conteudo.__str__(self)}"
                f"{10 * ' '}Temporada: {self._temporada}\n"
                f"{10 * ' '}Criadores: {self._criadores}\n"
                f"{10 * ' '}Episódios: {self._episodios}")

    @property
    def temporada(self):
        copia_temporada = self._temporada
        return copia_temporada

    @temporada.setter
    def temporada(self, nova_temporada):
        for temporada in nova_temporada:
            if isinstance(temporada, str):
                teste = True
            else:
                teste = False
        if teste:
            self._temporada = nova_temporada
        else:
            raise TypeError("Temporada inválida")

    @property
    def criadores(self):
        copia_criadores = self._criadores
        return copia_criadores

    @criadores.setter
    def criadores(self, novos_criadores):
        for criador in novos_criadores:
            if isinstance(criador, Pessoa):
                teste = True
            else:
                teste = False
        if teste:
            self._criadores = novos_criadores
        else:
            raise TypeError("Criador inválido")

    @property
    def episodios(self, temp: str) -> bool:
        copia_episodios = self._episodios
        return copia_episodios

    @episodios.setter
    def episodios(self, novos_episodios):
        for episodio in novos_episodios:
            if isinstance(episodio, Episodio):
                teste = True
            else:
                teste = False

        if teste:
            self._episodios = novos_episodios
        else:
            raise TypeError("Episódios inválidos")

    def adicionar_criador(self, pe: Pessoa) -> bool:
        self._criadores.append(pe.nome)
        return True

    def adicionar_temporada(self, nome: str) -> bool:
        self._temporada.append(nome)
        return True

    def adicionar_episodios(self, eps: list[Episodio]) -> bool:
        self._episodios.append([eps])
        return True
