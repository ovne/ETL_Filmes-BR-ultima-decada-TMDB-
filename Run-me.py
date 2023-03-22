import config as cfg
from ETL_TMDB import loadData


if __name__ == '__main__':

    ''' dada a estrutura funcional que optei no programa ETL basta invocar a ultima funcao
    do pipeline e esta vai requerir das outras até o fim do processo. '''

    loadData(cfg.BD_PARAMS, cfg.API_PARAMS)