# Superpower Jira Report Creator at Notion

|                |                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------:|
| Language       | [Python 3.8](https://www.python.org/ "Python's Homepage")                                                  |
| External API   | [Notion API - 2022-06-28 version](https://developers.notion.com/reference/intro "Notion's API reference")  |
|                | [Jira API](https://developer.atlassian.com/server/jira/platform/rest-apis/ "Jira's API reference")         |

Um comando poderoso para extrair screenshots e dados do Jira para *automagicamente*
criar um relatório de sprint no notion - no seu database de preferência ✨

## 1. O que esse comando faz afinal?
`todo`

## 2. Setup
`todo`

#### Instalando dependências 
Uma vez que o projeto está instalado no seu computador, vá para a pasta dele no terminal
e instale as dependências do projeto usando o comando:
```
pip3 install -r requirements.txt
``` 

### Configurando variáveis de ambiente
Para a `cli` funcionar, você precisa adicionar algumas variáveis de ambiente no seu terminal.
Para isso rode os comandos a seguir alterando o que está depois de `=` por seus respectivos valores:
- Troque `<your_notion_workspace_url>` pela url do seu workspace (tem a carinha https://www.notion.so/nome_aquii/)
- Troque `<your_notion_api_key>` pelo token que você recebe ao [configurar uma nova integração no Notion](https://developers.notion.com/docs/getting-started).
- Troque `<your_notion_database_id>` pelo id do "database de atas" que você deseja inserir a nova ata criada pela cli.
- Troque `your_notion_template_page_id>` pelo id de uma página que tem o conteúdo que você quer usar de
template e copiar para a nova página que criar.
```bash
export NOTION_BASE_URL=<your_notion_workspace_url>
export NOTION_API_KEY=<your_notion_api_key>
export NOTION_DATABASE_ID=<your_notion_database_id>
export NOTION_TEMPLATE_PAGE_ID=<your_notion_template_page_id>
```

## 3. Como usar
Para usar basta estar na pasta do projeto e rodar o comando:
```bash
python3 -m report_creator.main
```

E esperar a mágica acontecer :) 

## 4. Referências legais para fazer algo parecido
- Meu outro repo: [dehatanes/super-useful-notion-cli](https://github.com/dehatanes/super-useful-notion-cli)

---
Made with :heart: by @dehatanes & @thomasdoconski
