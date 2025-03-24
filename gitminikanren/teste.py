from kanren import Relation, facts, var, run, lall, lany
from kanren.constraints import neq

#lall = logical all, condition that satisfy multiple goals at once.
#lany = logical any, conditions that satisfy any goals individually.
#neq = constraint goal constructor in Kanren. It ensures that two values (or logic variables) are not unified as equal.



ontem = Relation()

facts(ontem,('domingo','sábado'))
facts(ontem,('segunda-feira','domingo'))
facts(ontem,('terça-feira','segunda-feira'))
facts(ontem,('quarta-feira','terça-feira'))
facts(ontem,('quinta-feira','quarta-feira')) 
facts(ontem,('sexta-feira','quinta-feira'))
facts(ontem,('sábado','sexta-feira'))

mentira = Relation()

facts(mentira,('leão', 'segunda-feira'))
facts(mentira,('leão', 'terça-feira'))
facts(mentira,('leão', 'quarta-feira'))

facts(mentira,('unicórnio', 'quinta-feira'))
facts(mentira,('unicórnio', 'sexta-feira'))
facts(mentira,('unicórnio', 'sábado'))

verdade = Relation()

facts(verdade,('leão', 'quinta-feira'))
facts(verdade,('leão', 'sexta-feira'))
facts(verdade,('leão', 'sábado'))
facts(verdade,('leão', 'domingo'))


facts(verdade,('unicórnio', 'domingo'))
facts(verdade,('unicórnio', 'segunda-feira'))
facts(verdade,('unicórnio', 'terça-feira'))
facts(verdade,('unicórnio', 'quarta-feira'))

def mudou(x,animal):

    dd_ontem = var()

    return lany(

            lall( 
            ontem(x,dd_ontem),
            mentira(animal,x),
            verdade(animal,dd_ontem)
            ),

            lall( 
            ontem(x,dd_ontem),
            verdade(animal,x),
            mentira(animal,dd_ontem)
            )
        )

x = var()

x = run(0,x,mudou(x,'unicórnio'),mudou(x,'leão'))

print(x)



