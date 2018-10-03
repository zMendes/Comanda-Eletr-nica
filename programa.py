import json

running = True
comanda = {}

while running:
    with open("cardapio.json",'r') as f:
        content=f.read()
        cardapio=json.loads(content)
    menu = int(input("Comanda Eletrônica\n0. Sair\n1. Imprimir cardápio\n2. Adicionar item\n3. Remover item\n4. Imprimir comanda\n-->"))
    if menu ==0:
        print("Até mais")
        with open('cardapio.json','w') as f:
            content=json.dumps(cardapio)
            f.write(content)
        running = False
    if menu ==1:
        if cardapio == '{}':
            print("Não há nada aqui")
        else:
            print("O cardápio possui os seguintes itens:")
            for a,b in cardapio.items():
                print("- {0}({1:.2f}R$)".format(a,b))
    
    if menu ==2:
        escolha= input("Gostaria de adicionar ao cardápio ou à comanda? " )
        if escolha=="cardápio" or escolha=="cardapio":
            pedido=input("O que deseja adicionar ao cardápio? " )
            preco=float(input("Preço:  "))
            if preco<0:
                print("O preço não pode ser negativo")
            else:
                cardapio[pedido] = preco
                print("Item adicionado")
        if escolha=="comanda":            
            pedido = input("Faça sua escolha: ")
            if pedido in cardapio:
                quantidade= int(input("Quantidade: "))
                comanda[pedido] = quantidade
                print("Quantidade atual de {0}: {1}".format(pedido,comanda[pedido]))
            else:
                print("Não há este produto no cardápio.")
    if menu ==3:
        escolha=(input("Deseja remover do cardapio ou da comanda?"))
        if escolha=='comanda':
            pedido=input("Pedido a ser removido:")
            if pedido in comanda:
                quantidade=int(input("Quantidade a remover: "))
                if quantidade<0:
                    print("Não é possível remover quantidade não positiva")
                else:
                    if (comanda[pedido]-quantidade)>=0:
                        comanda[pedido]=comanda[pedido]-quantidade
                        print ("Quantidade atual de {0} : {1}".format(pedido,comanda[pedido]))
                    if comanda[pedido]-quantidade== 0:
                        del comanda[pedido]
                    #if comanda[pedido]-quantidade<0:
                    #   print ("Máxima a ser removido:{0}\nNão é possível remover mais que a quantidade presente na comanda".format(comanda[pedido]))    
            else:
                print("Este item não está na comanda")
        if escolha=='cardapio' or escolha=='cardápio':
            pedido=input('Qual item deseja remover do cardápio?')
            if pedido in cardapio:
                del cardapio[pedido]
            else:
                print("Item não cadastrado")
    if menu==4:
        total=0
        for item in comanda:
            print("{0}:{1}".format(item,comanda[item]))
            total += cardapio[item] * comanda[item]
        print("Preço:{0}".format(total))