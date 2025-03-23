from kanren import Relation, facts, var, conde, run

# Criar as constantes:
MARIA = 'Maria'
CARLA = 'Carla'
LUCAS = 'Lucas'

# Vamos criar os predicados e as relações lógicas.
mae = Relation()
irma = Relation()

# Vamos adicionar so fatos as relações lógicas.
facts(mae, (MARIA, LUCAS)) # <- definimos que Maria é mãe de Lucas
facts(irma, (MARIA, CARLA)) #< - Como acima, definimos que MARIA é a irmã de Carla

# Agora vamos fazer a inferência para dizer que CARLA é TIA de LUCAS.

def tia(z, y):
    x = var()
    return conde(
        (mae(x, y),
         irma(x, z))
    )

t = var()
r = run(1, t, tia(t, LUCAS))

print(f'{r[0]} é tia de {LUCAS}')