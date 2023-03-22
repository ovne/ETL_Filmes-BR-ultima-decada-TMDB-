# Batch ETL process: Filmes lançados no Brasil 

![esquema-arquitetura](https://github.com/ovne/ETL_Filmes-BR-ultima-decada-TMDB-/blob/main/docs/arquitetura-1.0.png)

Este projeto é um processo de ETL (Extração, Transformação e Carregamento) de dados em lote. Totalmente programado em Python, esse processo extrai dados da API do site TheMovieDatabase, utiliza a ORM SQLAlchemy para modelar em uma estrututa tabular e por fim armazena os dados em um banco relacional MySQL e salva uma copia bruta dos dados localmente.

# Pré-requisitos

Antes de executar o projeto, certifique-se de que tenha o Python 3.x instalado em seu ambiente e tenha instalado os seguintes pacotes:

- requests
- urllib3
- SQLAlchemy
- pandas
- PyMySQL

Você também pode instalá-los de uma vez executando o seguinte comando em seu terminal:

>`pip install -r requirements.txt`


# Configuração
Para executar o projeto, você precisa fornecer suas próprias chaves de API do TheMovieDatabase e configurar o banco de dados MySQL.

Altere o arquivo config.py na raiz do projeto e defina os valores nos dicionarios:

- BD_PARAMS
- API_PARAMS

Crie um banco de dados MySQL com o mesmo nome definido na variável DB_PARAMS['database']
Executando o projeto
Para executar o projeto, execute o seguinte comando em seu terminal:

>`python Run-me.py`

O processo ETL começará a extrair os dados da API do TheMovieDatabase, transformá-los e carregá-los no banco de dados MySQL.

# Contribuição
Se você quiser contribuir para este projeto, sinta-se à vontade para enviar um pull request. Sua contribuição é bem-vinda.

# Licença
Este projeto é licenciado sob a licença MIT.