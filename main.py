from os import system
system('cls')

from time import sleep
import dados.dados_temas as dados_temas  
from interface import interface_variacao
from settings.save_config import salvar_config
from settings.gerenciar_config_vscode import alterar_tema_vscode
from interface.interface_temas import escolha_tema

tema_escolhido = escolha_tema(dados_temas.temas)


variacao_escolhida = interface_variacao.escolha_variacao(tema_escolhido)

alterar_tema_vscode(variacao_escolhida)

salvar_config(tema_escolhido, variacao_escolhida)

print( "-" * 40)
print('Aplicando....')
print(f'Seu tema atual é: {variacao_escolhida}')
sleep(1)




