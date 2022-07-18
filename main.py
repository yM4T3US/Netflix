from perfil import Perfil
from filme import Filme
from serie import Serie
from episodio import Episodio
from pessoa import Pessoa
from datetime import date
                                                #conteúdos#

                                                #episodio e série#

piloto = Episodio(1, "Piloto", "1ª temporada")

peakyblinders = Serie("Peaky Blinders", "ABC", 2018-8-22, 120.0, [["1ª", "2ª"]], ["Piloto", "Blabla"])

#pessoa

frazus = Pessoa("Frazus", 2002-8-27)


#filme
nao_olhe_para_cima = Filme("Não olhe para cima", 2022-3-22, 2022-4-22, "Ficção Científica", 90)

                                                #perfis#

#perfil

Mateus = Perfil("mateusalmeida996007570@gmail.com", "Mateus")
Mateus.cpf = "037.627.940-06"
Mateus.data_nascimento = date(2022, 8, 27)
Mateus.assistidos = [["Blabla", date(2022,7,6)], ["Blublu", date(2022,8,3)]]


print(Mateus)
print(Mateus.gerar_indicacoes("Ação"))

