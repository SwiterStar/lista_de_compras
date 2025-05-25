
#----------------------------------------------------------
porcomprar=[]
comprado=[]
#----------------------------------------------------------
def nline():
    print('\n----------------------------------------------------------')
def menu():
    while True:
        nline()
        print('\n1 - Adicionar\n2 - Editar\n3 - Remover\n4 - Listar\n5 - Mover\n6 - Sair')
        nline()
        o=input('\nEscolha: ')
        if o=='1':adicionar()
        if o=='2':editar()
        if o=='3':remover()
        if o=='4':listar()
        if o=='5':mover()
        if o=='6':sair()
def adicionar():
    global porcomprar,comprado 
    print('\nA qual das listas quer Adicionar:\n\n1 - Por Comprar\n2 - Comprado')
    e=input('\nEscolha: ')
    if e=='1':
        a=input('\nPor Comprar: ')
        porcomprar.append(a)
        print(f'\n{a} foi adicionado a Por Comprar')
    if e=='2':
        a=input('\nComprado: ')
        comprado.append(a)
        print(f'\n{a} foi adicionado a Comprado')
    porcomprar.sort()
    comprado.sort()



#----------------------------------------------------------
menu()
#----------------------------------------------------------