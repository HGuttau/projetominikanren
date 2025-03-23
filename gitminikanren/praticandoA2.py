from kanren import Relation, facts, var, run, lall, lany
from kanren.constraints import neq

mae = Relation()
pai = Relation()
facts(mae, ('Carol', 'John'))
facts(pai, ('Eric', 'John'))

def pais(x, pessoa):
   return lany(
       mae(x, pessoa),
       pai(x, pessoa),
   )

x = var()
print(run(2, x, pais(x, 'John')))