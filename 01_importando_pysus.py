# IMPORTANDO PACOTES 
import pandas as pd   

from ftplib import FTP
from pysus.online_data.SIH import download

#DEFININDO VARIÁVEIS
vars = ["MORTE", "CID_MORTE", "DIAG_PRINC", "DI_INTER", "ANO_CMPT", "MES_CMPT", "DIAG_SECUN",  "IDADE", "SEXO", "UF_ZI", "DIAS_PERM", "NUM_FILHOS", "INSTRU", "MARCA_UTI", "INFEHOSP"]
ufs = ['ac', 'al', 'ap', 'am','ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to']
anos = [2022] #[2017, 2018, 2019, 2020, 2021]
meses = [1, 2, 3, 4] #, 5, 6, 7, 8, 9, 10, 11, 12]
cids = ["J130", "J140", "J153", "J154", "J158", "J159", "J181"]

#IMPORTANDO DADOS
for uf in ufs:
    for ano in anos:
        for mes in meses:
            df = download(uf, ano, mes)
            df = df.filter(vars)
            df = df[df['DIAG_PRINC'].isin(cids)]
            df.to_csv("sih_pneumonia_1721.csv", mode='a', index=False, header=False)
            print(f"O arquivo do mês {mes} de {ano} do estado {uf.upper()} foi filtrado")

