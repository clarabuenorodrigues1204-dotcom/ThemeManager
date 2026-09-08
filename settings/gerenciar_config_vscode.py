import json
import os

#função responsável por alterar a chave que guarda o tema do vscode

def alterar_tema_vscode(variacao_escolhida):
    caminho = os.environ["APPDATA"] + "\\Code\\User\\settings.json"
    
    with open(caminho, "r", encoding="utf-8") as arquivo:
        settings = json.load(arquivo)
        
    settings["workbench.colorTheme"] = variacao_escolhida
    
    with open(caminho, "w" , encoding="utf-8") as arquivo:
        json.dump(settings, arquivo, indent=4, ensure_ascii=False) 