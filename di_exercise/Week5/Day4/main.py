n = 'the'
p= "man"
# print(f"{n} {p}")

def assemble (*args):
    return " ".join(args)
assemble(n,p)
a= assemble(n,p)
print(a)
