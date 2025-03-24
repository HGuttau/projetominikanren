from kanren import Relation, facts, var, run, lall, lany
from kanren.constraints import neq

diadasemana = Relation()

facts(diadasemana, 'Segunda-Feira')
facts(diadasemana, 'Terça-Feira')
facts(diadasemana, 'Quarta-Feira')
facts(diadasemana, 'Quinta-Feira')
facts(diadasemana, 'Sexta-Feira')
facts(diadasemana, 'Sábado')
facts(diadasemana, 'Domingo')

ontem = Relation()

facts(ontem,('Domingo','Sábado'))
facts(ontem,('Segunda-Feira','Domingo'))
facts(ontem,('Terça-Feira','Segunda-Feira'))
facts(ontem,('Quarta-Feira','Terça-Feira'))
facts(ontem,('Quinta-Feira','Quarta-Feira')) 
facts(ontem,('Sexta-Feira','Quinta-Feira'))
facts(ontem,('Sábado','Sexta-Feira'))

# Dias em que cada criatura mente
mentira = Relation()
facts(mentira, ('Leão', 'Segunda-Feira'))
facts(mentira, ('Leão', 'Terça-Feira'))
facts(mentira, ('Leão', 'Quarta-Feira'))
facts(mentira, ('Unicornio', 'Quinta-Feira'))
facts(mentira, ('Unicornio', 'Sexta-Feira'))
facts(mentira, ('Unicornio', 'Sábado'))

# Dias em que cada criatura fala a verdade
verdade = Relation()
facts(verdade, ('Leão', 'Quinta-Feira'))
facts(verdade, ('Leão', 'Sexta-Feira'))
facts(verdade, ('Leão', 'Sábado'))
facts(verdade, ('Leão', 'Domingo'))
facts(verdade, ('Unicornio', 'Segunda-Feira'))
facts(verdade, ('Unicornio', 'Terça-Feira'))
facts(verdade, ('Unicornio', 'Quarta-Feira'))
facts(verdade, ('Unicornio', 'Domingo'))

def amanha(dia, x):
    return ontem(x, dia)

def fala_leao(z):
    dd = var()
    return mentira('Leão', amanha(z, dd))

def fala_unicornio(y):
    zz = var()
x = var()

s = run(0, x, verdade('Leão', x), verdade('Unicornio', x))

print(s)

