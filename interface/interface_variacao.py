import json

#Função responsável por fazer a escolha de variação do tema

def escolha_variacao(tema_escolhido):

    with open("dados/dados_variacao.json" , "r" , encoding= "utf-8") as arquivo:
        
        interface_variacao = json.load(arquivo)
        variacoes_disponiveis = interface_variacao[tema_escolhido]
        
        for indice, variacao in enumerate(variacoes_disponiveis, start=1):
            print(f'{indice} - {variacao}')
            
    
    #Validação da escolha do usuário em relação a variação de temas
    
    while True:
        try:
            print( "-" * 40)
            variacao = int(input('Escolha uma variação de tema: '))
            
            if 1 <= variacao <= len(variacoes_disponiveis):
                
                variacao_escolhida = variacoes_disponiveis[variacao - 1]
                print(f'Você escolheu a variação: {variacao_escolhida}')
                
                return variacao_escolhida
        
            print('Opção Inválida!')
            
        except ValueError:
            print('Digite apenas números!')
            

            
        