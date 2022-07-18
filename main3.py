from pessoa import Pessoa
from Netflix.daos.pessoaDAO import PessoaDAO
from datetime import date

frazus = Pessoa("Frazus", date(2002, 8, 27))
frozen = Pessoa("Frozen", date(2003, 8, 27))

pessoasDB = PessoaDAO()
pessoasDB.save(frazus)
pessoasDB.save(frozen)

pessoas = pessoasDB.find_all()



print(pessoasDB.find_by_nome_equals("Frazus"))

print(frazus.id)
print(frozen.id)

pessoasDB.delete(frazus)

print(frazus in pessoas)






