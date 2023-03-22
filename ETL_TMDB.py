"""

"""

from datetime import datetime
import requests
import json
import pandas
from datamodel.DBconfig import DBConnHandler
from datamodel.entidades import CinemaBr


def getData(endpoint:str, api_key:str, startDate:str, endDate:str):
    """
    Essa é uma função geradora. Seu objetivo é fazer requisições consecutivas
    a API do TMDB e entregar a resposta de dados para a função transformData(). 
    """
    
    base_url = endpoint
    params = {'api_key': api_key,
          'language': 'pt-BR',
          'region' : 'BR', # lembrando que o objetivo são dados de filmes que foram lançados no BR. 
          'release_date.gte': startDate,
          'release_date.lte': endDate,
          'page' : 1 # sempre inicia pela pagina 1.
        }
    
    while True:

        response = requests.get(url=base_url, params=params)

        if response.status_code == 200:
            payload = response.json()
            datalist = payload['results']
            if datalist and params['page'] <= 5: # implicit booleanness of empty list (bem legal)
                yield datalist
                params['page'] += 1
            elif not datalist and params['page'] < payload['total_pages']:
                # por algum motivo o payload esta vazio, mas, ainda ha paginas a percorrer
                params['page'] += 1
            else:
                # payload esta vazio, provalmente, ultima pagina
                print('=== Dados extraidos com sucesso. ===')
                break
        else:
            print(f"[ERROR] Unable to retrieve data from page {params['page']}...") #[log it somewhere later!]
            params['page'] += 1


def transformData(api_params:dict):
    """
    Essa função invoca getData(), recebe os dados servidos pela API, parseia os objetos
    para extrair um subconjunto de interesse, mas tambem mantem uma copia dos dados brutos da API.
    """

    data_map = {
        "id" : [],
        "titulo_br" : [],
        "titulo_original" : [],
        "data_estreia" : [],
        "rating" : [],
        "num_avaliacoes" : []
    } # estrutura intermediaria para entao escrever do SGBD via pandas+SQLAlchemy 

    def parser(movie:dict):
        data_map['id'].append(movie['id'])
        data_map['titulo_br'].append(movie['title'])
        data_map['titulo_original'].append(movie['original_title'])
        data_map['data_estreia'].append(movie['release_date'])
        data_map['rating'].append(movie['vote_average'])
        data_map['num_avaliacoes'].append(movie['vote_count'])
    
    #data_mass = list() # lista gigante com todos os objs retornados pela API

    for datalist in getData(api_params['endpoint'], api_params['key'], api_params['startDate'], api_params['endDate']):
        #data_mass += datalist
        for movie in datalist:
            parser(movie)
    
    dataset = pandas.DataFrame(data=data_map, columns=list(data_map.keys()))

    return dataset
    

def loadData(dbparams:dict, api_params:dict):
    ''' A ideia aqui é escrever os dados num formato mais estruturado no banco
    relacional, num diretorio local ou em cloud (coming) '''

    # iniciando conexao com BD
    connectionDB = DBConnHandler(dbparams)
    connectionDB.addTableDB()
    print('[=== Metadados das entidades atualizados no BD ===]\n')
    
    engineDB = connectionDB.engine
    sessionDB = connectionDB.session

    # obtendo dados formatados para escrita do BD
    df_towrite = transformData(api_params)

    try:
        df_towrite.to_sql(name=CinemaBr.__tablename__,con=engineDB,if_exists='append', index=False)
        print("[=== Os dados foram escritos no banco de dados ===]\n")
    except Exception as e:
        print(f"[=== Falha ao escrever dados no banco ===]")
        print(f'erro: {e}')
        print("[=== Uma cópia em formato CSV do conjunto de dados sera salva localmente ===]")
        filename = f"copy-load-data-failed-in{datetime.now()}"
        with open(file=filename, mode='w', encoding='utf-8') as file:
            file.write(df_towrite.to_csv()) # note: check to_cvs() params for better perfomance/data quality

    sessionDB.commit()
    sessionDB.close()

    print("[=== Conexao com banco de dados encerrada ===]\n")

    return

    