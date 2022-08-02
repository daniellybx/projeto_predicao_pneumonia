#IMPORTANDO PACOTES 
library(read.dbc)
library(tidyverse)

#DIRECIONANDO PARA A PASTA COM OS ARQUIVOS 
files <- cbind(paste0("D:/SIH/", list.files("D:/SIH")))

#DEFININDO CID DE PNEUMONIA SENSIVEL À APS
pneumonia <- c("J13", "J14", "J15.3", "J15.4", "J15.8", "J15.8", "J18.1")

#CRIANDO ESTRUTURA DE FILTRAGEM DOS DADOS
dados_fn <- NULL

for(file in 1:length(files)){
  
    dados_temp <- read.dbc(files[file])
    dados_temp <- dados_temp %>%
        filter(DIAG_PRINC %in% pneumonia) %>%
        select(MORTE, IDADE, SEXO, UF_ZI, DIAS_PERM, NUM_FILHOS, INSTRU, 
        MARCA_UTI, INFEHOSP)
    dados_fn = data.frame(rbind(dados_fn, dados_temp))
    print(files)

    }

#ESCREVENDO UM ARQUIVO COM OS DADOS FILTRADOS
write.csv2(dados_fn, "pneumonia_brasil.csv", row.names = F)