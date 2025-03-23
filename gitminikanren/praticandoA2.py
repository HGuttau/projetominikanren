from kanren import Relation, facts, var, run, lall, lany
from kanren.constraints import neq

mae = Relation()
pai = Relation()

facts(mae, ('Carol', 'John'))
facts(mae, ('Carol', 'Julia'))
facts(mae, ('Carol', 'Leo'))

facts(pai, ('Eric', 'John'))
facts(pai, ('Eric', 'Julia'))
facts(pai, ('Eric', 'Leo'))

def pais(x, pessoa):
   return lany(
       mae(x, pessoa),
       pai(x, pessoa),
   )

def filhos(pessoa, x):
   return lany(
      mae(pessoa, x),
      pai(pessoa, x)
   )


def irmaos(pessoa, x):
    paisemcomum = var()
    return lall(
       pais(paisemcomum, pessoa),
       pais(paisemcomum, x),
       neq(pessoa, x)
    )
   


x = var()
print(run(2, x, irmaos('John', x)))