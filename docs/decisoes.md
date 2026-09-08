# Decisões do Projeto

Registro das principais decisões tomadas durante o desenvolvimento do ThemeManager.

---
## Decisão herdada da primeira versão do projeto - julho/2026

### Uso de JSON para armazenamento de dados:

- A primeira versão do ThemeManager adotou arquivos JSON para armazenar informações do projeto.
- Essa abordagem foi mantida na reorganização da versão atual.

Arquivos utilizados:

- `config.json` → armazena as escolhas do usuário.
- `settings.json` → arquivo de configuração do VS Code.
- Arquivos de dados → armazenam informações relacionadas aos temas e variações.

**Motivo:**

Utilizar uma estrutura simples, legível e fácil de editar, permitindo separar os dados da lógica do programa.

---
## 24/07/2026

### Reorganização do repositório

* Criado novo repositório.
* Removidas pastas duplicadas.
* Código antigo mantido como backup.
* Projeto será reorganizado em módulos.

**Motivo:**

Melhorar a organização do projeto e preparar a estrutura para futuras funcionalidades.

---

## Aproximadamente 05/08/2026

### Sistema de validação das escolhas do usuário

* Implementada validação das opções escolhidas pelo usuário.
* O programa verifica se a opção informada corresponde a uma opção disponível.

**Motivo:**

Evitar erros durante a execução e melhorar a experiência do usuário.

---

## 06/08/2026

### Criação de sistema de variações de temas

* Adicionado suporte para temas com diferentes variações.
* O usuário primeiro escolhe o tema e depois seleciona sua variação.

Fluxo:

```
Escolha do tema
        ↓
Escolha da variação
        ↓
Salvar configuração
```

**Motivo:**

Permitir maior flexibilidade na escolha dos temas e preparar o projeto para temas com múltiplas versões.

---

## 07/08/2026

### Documentação do projeto

* Criados arquivos de documentação:

  * `funcionamento.md`
  * `roadmap.md`
  * `ideias.md`
  * `decisoes.md`

**Motivo:**

Registrar o funcionamento atual, planejamento futuro e decisões tomadas durante o desenvolvimento.

---

# Mudanças

- Mudar o arquivo interface_variacao.json para a pasta dados
- Mudar o config.json para a pasta settings
- Mudar nome de arquivos 
	- interface_variacao.json - dados_variacao.json
	- temas.py - dados_temas.py
	- vscode_config.py - gerenciar_config_vscode.py
	- config.json - estado_atual.json
- Padronização entre as funções "escolha_tema" e "escolha_variacao"
