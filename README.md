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

#### Instalando dependências 
Uma vez que o projeto está instalado no seu computador, vá para a pasta dele no terminal
e instale as dependências do projeto usando o comando:
```
pip3 install -r requirements.txt
``` 

### Configurando variáveis de ambiente do Notion
Para a `cli` funcionar, você precisa adicionar algumas variáveis de ambiente no seu terminal.
Para isso rode os comandos a seguir alterando o que está depois de `=` por seus respectivos valores:
- Troque `<your_notion_workspace_url>` pela url do seu workspace (tem a carinha https://www.notion.so/nome_aquii/)
- Troque `<your_notion_api_key>` pelo token que você recebe ao [configurar uma nova integração no Notion](https://developers.notion.com/docs/getting-started).
- Troque `<your_notion_database_id>` pelo id do "database de atas" que você deseja inserir a nova ata criada pela cli.
- Troque `your_notion_template_page_id>` pelo id de uma página que tem o conteúdo que você quer usar de template e copiar para a nova página que criar.
- Troque `your_notion_project_id>` pelo id do projeto que desejar extrair o relatório de burndown.
- Troque `your_notion_board_id>` pelo id do board que desejar extrair o relatório de burndown.

```bash
export NOTION_BASE_URL=<your_notion_workspace_url>
export NOTION_API_KEY=<your_notion_api_key>
export NOTION_DATABASE_ID=<your_notion_database_id>
export NOTION_TEMPLATE_PAGE_ID=<your_notion_template_page_id>
export NOTION_PROJECT_ID=<your_notion_project_id>
export NOTION_BOARD_ID=<your_notion_board_id>
```

### Configurando variáveis de ambiente do Jira
Ainda não acabou. No mesmo esquema das variáveis acima, você também vai precisar de algumas
relacionadas ao Jira para que isso aqui possa funcionar.
Rode os comandos a seguir alterando o que está depois de `=` por seus respectivos valores:
- Troque `<your_jira_workspace_name>` pelo nome do seu workspace (você encontra ele na *url do seu jira* - é o nominho que fica entre o `https://` e `.atlassian.net`)
- Troque `<your_jira_dashboard_id>` pelo id da sua dash do jira (é o último número na url da sua dashboard tipo `https://tokyodrift.atlassian.net/jira/dashboards/<AQUI>`)
- O valor de `<your_jira_cloud_session_cookie>` é mais chatinho de encontrar. Você precisa:
  - Estar logado no Jira através de um browser
  - Pegar os cookies do seu browser
  - Separar o valor do cookie chamado `cloud.session.token` e usá-lo aqui (é uma string grandinha mesmo)
```bash
export JIRA_WORKSPACE_NAME=<your_jira_workspace_name>
export JIRA_DASHBOARD_ID=<your_jira_dashboard_id>
export JIRA_CLOUD_SESSION_TOKEN=<your_jira_cloud_session_cookie>
```

### Configurando variáveis de ambiente da AWS
Para conseguirmos salvar os screenshots do Jira e salvá-los no Notion, precisamos de um
bucket da AWS que seja *publicamente acessível*.
Então para isso:
- Crie seu bucket e um usuário com acesso a ele (você pode usar [esse tutorial da aws para isso](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/create-bucket-overview.html) 
- Configure sua máquina com as infos do seu usuário para que as requisições para os serviços da aws consigam ser autenticadas,
você pode usar [esse tutorial para isso](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
- Com o nome do buscket que criou em mãos, configure essa variável de ambiente substituindo o valor de `<your_bucket_name>`:
  ```bash
  export BUCKET_NAME=<your_bucket_name>
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
