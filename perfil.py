from Netflix.models.conteudo import Conteudo
from sqlalchemy import Column, Integer, String
from Netflix.daos.bd import BancoDados
from datetime import date


class Perfil(BancoDados.Base):
    """Classe perfil salvando no bd"""

    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True)
    _nome = Column(String, nullable=False)
    _email = Column(String, nullable=False)
    senha = Column(Integer, nullable=True)
    _cpf = Column(String, nullable=True)
    _data_nascimento = Column(String, nullable=True)


    def __init__(self, email: str, nome: str):

        self._email = email
        self.senha = None
        self._nome = nome
        self._cpf = None
        self._data_nascimento = None
        self._favoritos = None
        self._assistidos = None
        self._minha_lista = None
        self.__indicacoes = None

    def __str__(self):
        retorno = f"E-mail: {self._email}\n"
        retorno += f"Nome: {self._nome}\n"
        retorno += f"CPF: {self._cpf}\n"
        retorno += f"Data de nascimento: {self._data_nascimento}\n"
        # retorno += f"Favoritos: {', '.join(x.__str__() for x in self.__favoritos)}\n"
        retorno += f"Assistidos: {self._assistidos}\n"
        retorno += f"Minha lista: {self._minha_lista}\n"
        print()
        print("-=" * 20)
        print()
        retorno = retorno.replace(",", " ")
        return retorno

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not hasattr(self, "_email"):
            self._email = None
        if isinstance(email, str):
            if "@" in email and "." in email:
                self._email = email
        else:
            raise TypeError("E-mail inválido.")

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        if not hasattr(self, "_senha"):
            self._senha = None
        elif isinstance(senha, int) and len(str(senha)) >= 6:
            self._senha = senha
        else:
            raise ValueError("A senha deve ser do tipo inteiro com no mínimo 6 dígitos.")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            if nome != self.nome:
                self._nome = nome
        else:
            raise TypeError("Nome inválido.")

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if not hasattr(self, "_cpf"):
            self._cpf = None
        if isinstance(cpf, str):
            if "." in cpf and "-" in cpf:
                novo = cpf.replace(".", "")
                novo = novo.replace("-", "")
                if len(novo) == 11:
                    self._cpf = cpf
            else:
                novo = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
            return novo
        else:
            raise TypeError("CPF inválido")

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if isinstance(data_nascimento, date):
            if data_nascimento != self._data_nascimento:
                self._data_nascimento = data_nascimento
        else:
            raise TypeError("Data de nascimento inválida")

    @property
    def favoritos(self):
        return self._favoritos

    @favoritos.setter
    def favoritos(self, novos_favoritos):
        if isinstance(novos_favoritos, list):
            for favorito in novos_favoritos:
                if isinstance(favorito, str):
                    if novos_favoritos != self._favoritos:
                        self._favoritos = novos_favoritos
        else:
            raise TypeError("Lista de favoritos inválida")

    @property
    def assistidos(self):
        copia_assistidos = self._assistidos
        return copia_assistidos

    @assistidos.setter
    def assistidos(self, assistidos):
        if not hasattr(self, "_assistidos"):
            self._assistidos = None
        teste = False
        if isinstance(assistidos, list):
            for assistido in assistidos:
                if isinstance(assistido[0], str) and isinstance(assistido[1], date):
                    teste = True
                else:
                    teste = False
        if teste:
            self._assistidos = assistidos
        else:
            raise TypeError("Lista de assistidos inválida")

    @property
    def minha_lista(self):
        copia_minha_lista = self._minha_lista
        return copia_minha_lista

    @minha_lista.setter
    def minha_lista(self, nova_lista):
        teste = False
        if isinstance(nova_lista, list):
            for z in nova_lista:
                if isinstance(z, str):
                    teste = True
                else:
                    teste = False
        if teste:
            self.__minha_lista = nova_lista
        else:
            raise TypeError("Lista inválida")


    def gerar_indicacoes(self, gen) -> list[Conteudo]:
        indicacoes = self.minha_lista or []
        for conteudo in Conteudo.conteudos:
            if conteudo.genero == gen and conteudo not in self._assistidos:
                indicacoes.append(conteudo)
        return indicacoes

    def assistir(self, cont: str, data: date) -> bool:
        self._assistidos.append([cont, data])
        return True

    def favoritar(self, cont: str) -> bool:
        self.favoritos.append(cont)
        return True

    def adicionar_minha_lista(self, cont: str) -> bool:
        self.minha_lista.append(cont)
        return True





