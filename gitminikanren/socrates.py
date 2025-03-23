from kanren import Relation, fact, var, run 


homem = Relation()
fact(homem, "Sócrates")

def mortal(x):
    return homem(x)

x = var()
r = run(1, x, mortal(x))

print(r)

