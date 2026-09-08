import json

#Função responsável por atualizar e salvar a escolha do usuário

def salvar_config(tema_escolhido , variacao_escolhida):
    with open("settings/estado_atual.json" , "r" , encoding= "utf-8") as arquivo:
        config = json.load(arquivo)
        
        config["tema_atual"] = tema_escolhido
        config["variacao_atual"] = variacao_escolhida
        
    with open("settings/estado_atual.json", "w" , encoding="utf-8") as arquivo:
        json.dump(config, arquivo , indent=4, ensure_ascii= False)   
    