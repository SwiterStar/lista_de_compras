
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
def editar():
    global porcomprar,comprado 
    print('\nQual das listas quer editar:\n\n1 - Por Comprar\n2 - Comprado')
    e=input('\nEscolha: ')
    if e=='1':
        if len(porcomprar)==0:
            print('\nPor comprar tem 0 Artigos')
            return
        if len(porcomprar)>0:
            print()
            for i in range(len(porcomprar)):print(f'{i+1} - {porcomprar[i]}')
            a=eval(input('\nEscolha: '))
            porcomprar[a-1]=input('\nPor Comprar: ')
    if e=='2':
        if len(comprado)==0:
            print('\nComprado tem 0 Artigos')
            return
        if len(comprado)>0:
            print()
            for i in range(len(comprado)):print(f'{i+1} - {comprado[i]}')
            a=eval(input('\nEscolha: '))
            comprado[a-1]=input('\nComprado: ')
    porcomprar.sort()
    comprado.sort()
def remover():
    global porcomprar,comprado 
    print('\nQual das listas quer editar:\n\n1 - Por Comprar\n2 - Comprado')
    e=input('\nEscolha: ')
    if e=='1':
        if len(porcomprar)==0:
            print('\nPor comprar tem 0 Artigos')
            return
        if len(porcomprar)>0:
            print()
            for i in range(len(porcomprar)):print(f'{i+1} - {porcomprar[i]}')
            a=eval(input('\nQual dos Artigos quer Remover: '))
            porcomprar.pop(a-1)
    if e=='2':
        if len(comprado)==0:
            print('\nComprado tem 0 Artigos')
            return
        if len(comprado)>0:
            print()
            for i in range(len(comprado)):print(f'{i+1} - {comprado[i]}')
            a=eval(input('\nQual dos Artigos quer Remover: '))
            comprado.pop(a-1)



#----------------------------------------------------------
menu()
#----------------------------------------------------------