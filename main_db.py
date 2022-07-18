
from datetime import date

from daos.conteudoDAO import ConteudoDAO
from Netflix.models.filme import Filme
from Netflix.models.serie import Serie
from Netflix.models.episodio import Episodio
from Netflix.models.perfil import Perfil
# from Netflix.models.conteudo import Conteudo
from Netflix.models.pessoa import Pessoa
from Netflix.funcoes_db import menu_classes, menu_opcoes, dicionario_menu_classes
from daos.perfilDAO import PerfilDAO
from daos.filmeDAO import FilmeDAO
from daos.episodioDAO import EpisodioDAO
# from daos.serieDAO import SerieDAO



def entrada_filme_serie(escolha):
    resposta_3 = int(input(f"Deseja {escolha} filme [1] ou série [2]? "))
    return resposta_3

def insercao_dados_conteudo(escolha_filme_serie, cont):
    print("Insira os dados do conteúdo\n")
    titulo = str(input("Título: "))
    genero = str(input("Gênero: "))
    lancamento = date.fromisoformat(input("Data de lançamento: "))
    expiracao = date.fromisoformat(input("Data de expiração: "))
    duracao = int
    if escolha_filme_serie == 2:
        temporada = input().split(" ")
        cont = Serie(titulo, genero, lancamento, expiracao, temporada)
        seriesDB = ConteudoDAO()
        seriesDB.save(cont)
    elif escolha_filme_serie == 1:
        cont = Filme(titulo, genero, lancamento, expiracao, duracao)
        filmesDB = ConteudoDAO()
        filmesDB.save(cont)


def insercao_dados_episodio(ep):
    print("Insira os dados do episódio\n")
    nr = int(input("Número: "))
    nome = str(input("Nome: "))
    temporada = str(input("Temporada: "))
    ep = Episodio(nr, nome, temporada)
    episodiosDB = EpisodioDAO()
    episodiosDB.save(ep)

def insercao_dados_perfil(per):
    print("Insira os dados do episódio\n")
    nome = str(input("Nome: "))
    email = str(input("E-mail: "))
    per = Perfil(email, nome)
    perfisDB = PerfilDAO()
    perfisDB.save(per)

def insercao_dados_pessoa(pes):
    print("Insira os dados da pessoa\n")
    nome = str(input("Nome: "))
    nascimento = date.fromisoformat(input("Data de nascimento: "))
    pes = Pessoa(nome, nascimento)
    pessoasDB = PessoaDAO()
    pessoadDB.save(pes)





print(f"{60*'=-'}\n")
print(f"{'BEM-VINDO AO NETFLIX':^120}\n")
print(f"{60*'=-'}\n")




# menu_opcoes

menu_opcoes()

resposta_menu_opcoes = int(input("Resposta: "))

print(f"\n{60*'=-'}\n")



# menu_classes

menu_classes(resposta_menu_opcoes)

resposta_menu_classes = int(input("Resposta: "))

print(f"\n{60*'=-'}\n")




# menu4 - criações

if resposta_menu_opcoes == 1:

      if resposta_menu_classes == 1:
            escolha_filme_serie = int(input(f"Deseja {dicionario_menu_classes()[resposta_menu_opcoes]} filme [1] ou série [2]? "))

            # entradas de dados para a criação do objeto filme ou série

            print("Insira os dados do conteúdo\n")
            titulo = str(input("Título: "))
            genero = str(input("Gênero: "))
            lancamento = date.fromisoformat(input("Data de lançamento: "))
            expiracao = date.fromisoformat(input("Data de expiração: "))
            duracao = int(input("Duração: "))
            if escolha_filme_serie == 2:
                temporada = input().split(" ")
                # serie = Serie(titulo, genero, lancamento, expiracao, temporada)
                # seriesDB = SerieDAO()
                # seriesDB.save(serie)
            elif escolha_filme_serie == 1:
                filme = Filme(titulo, genero, lancamento, expiracao, duracao)
                filmesDB = FilmeDAO()
                filmesDB.save(filme)





      elif resposta_menu_classes == 2:

          # entrada de dados para criação do objeto episodio

          print("Insira os dados do episódio\n")
          nr = int(input("Número: "))
          nome = str(input("Nome: "))
          temporada = str(input("Temporada: "))
          episodio = Episodio(nr, nome, temporada)
          episodiosDB = EpisodioDAO()
          episodiosDB.save(episodio)



      elif resposta_menu_classes == 3:

          # entrada de dados para criação do objeto perfil

          print("Insira os dados do episódio\n")
          nome = str(input("Nome: "))
          email = str(input("E-mail: "))
          perfil = Perfil(email, nome)
          perfisDB = PerfilDAO()
          perfisDB.save(perfil)

      elif resposta_menu_classes == 4:

          # entrada de dados para criação do objeto pessoa

          print("Insira os dados da pessoa\n")
          nome = str(input("Nome: "))
          nascimento = date.fromisoformat(input("Data de nascimento: "))
          pessoa = Pessoa(nome, nascimento)
          pessoasDB = PessoaDAO()
          pessoadDB.save(pessoa)


# menu5 - exclusões

if resposta_menu_opcoes == 2:

    if resposta_menu_classes == 1:
        if entrada_filme_serie("deletar") == 1:
            filmesDB.find_filmes()
            filmesDB.delete()

        elif entrada_filme_serie("deletar") == 2:
            seriesDB.find_series()
            seriesDB.delete()

    elif resposta_menu_classes == 2:
        episodiosDB.find_all()
        episodiosDB.delete()

    elif resposta_menu_classes == 3:
        perfisDB.find_all()
        perfisDB.delete()

    elif resposta_menu_classes == 4:
        pessoasDB.find_all()
        pessoasDB.delete()

# menu6 - updates

dicionario_atributos_conteudos = {1: titulo, 2: genero, 3: duracao, 4: lancamento, 5: expiracao}

if resposta_menu_opcoes == 3:

    if menu_classes(resposta_menu_opcoes) == 1:

        if entrada_filme_serie(resposta_menu_opcoes) == 1:
            print("Qual o nome do filme que deseja realizar a alteração?")
            resposta_entrada_filme = str(input())
            filme = filmesDB.find_by_nome_equals(resposta_entrada_filme)
            insercao_dados_conteudo(escolha_filme_serie, filme)

        elif entrada_filme_serie(resposta_menu_opcoes) == 2:
            print("Qual o nome da série que deseja fazer a alteração?")
            resposta_entrada_serie = input()
            serie = seriesDB.find_by_nome_equals(resposta_entrada_serie)
            insercao_dados_conteudo(escolha_filme_serie, serie)

    elif menu_classes(resposta_menu_opcoes) == 2:
        print("Qual o nome do episódio que deseja realizar a alteração?")
        resposta_entrada_episodio = str(input())
        episodio = episodiosDB.find_by_nome_equals(resposta_entrada_episodio)
        insercao_dados_episodio(episodio)

    elif menu_classes(resposta_menu_opcoes) == 3:
        print("Qual o nome do perfil que deseja realizar a alteração?")
        resposta_entrada_perfil = str(input())
        perfil = perfisDB.find_by_nome_equals(resposta_entrada_perfil)
        insercao_dados_perfil(perfil)

    elif menu_classes(resposta_menu_opcoes) == 4:
        print("Qual cadastro de pessoa você gostaria de alterar?")
        resposta_entrada_pessoa = str(input())
        pessoa = pessoasDB.find_by_nome_equals(resposta_entrada_pessoa)
        insercao_dados_pessoa(pessoa)

# menu7 - leitura

if resposta_menu_opcoes == 4:

    if menu_classes(resposta_menu_opcoes) == 1:

        if entrada_filme_serie(resposta_menu_opcoes) == 1:
            print("Qual o nome do filme que deseja ler?")
            nome_filme = str(input())
            print(filmesDB.find_by_nome_equals_first(nome_filme))

        elif entrada_filme_serie(resposta_menu_opcoes) == 2:
            print("Qual o nome da série que deseja ler?")
            nome_serie = str(input())
            print(seriesDB.find_by_nome_equals_first(nome_serie))

    elif menu_classes(resposta_menu_opcoes) == 2:

        print("Qual o nome do episódio que deseja ler?")
        nome_episodio = str(input())
        print(episodiosDB.find_by_nome_equals(nome_episodio))

    elif menu_classes(resposta_menu_opcoes) == 3:
        print("Qual o nome do perfil que deseja ler")
        nome_perfil = str(input())
        print(perfisDB.find_by_nome_equals_first(nome_perfil))

    elif menu_classes(resposta_menu_opcoes) == 2:
        print("Qual o nome da pessoa que deseja ler?")
        nome_pessoa = str(input())
        print(pessoasDB.find_by_nome_equals(nome_pessoa))

# menu8 - listar

if resposta_menu_opcoes == 5:

    if menu_classes(resposta_menu_opcoes) == 1:

        if entrada_filme_serie(resposta_menu_opcoes) == 1:
            print(filmesDB.find_all())

        elif entrada_filme_serie(resposta_menu_opcoes) == 2:
            print(seriesDB.find_all())

    elif menu_classes(resposta_menu_opcoes) == 2:
        print(episodiosDB.find_all())

    elif menu_classes(resposta_menu_opcoes) == 3:
        print(perfisDB.find_all())

    elif menu_classes(resposta_menu_opcoes) == 4:
        print(pessoasDB.find_all())































































print(f"\n{60*'=-'}\n")





nao_olhe_para_cima = Filme("Não olhe para cima", 2022-3-22, 2022-4-22, "Ficção Científica", 90)
























for i in range(3):
    print()
