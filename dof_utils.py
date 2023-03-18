#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:38:11 2023

@author: robsondeoliveira
"""

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_data_dof(uf_origem, anos):
  '''
  Função para extrair dados dos DOF, retornando como um Pandas dataframe.
  Podem ser incluídos multiplos anos e multiplas UFs de origem.
  uf_origem: lista de UFs de onde partiu a madeira.
  anos: lista com os anos de emissão do DOF a serem pesquisados.
  '''
  df = pd.DataFrame()
  for uf in uf_origem:
    for ano in anos:
      url = 'https://dadosabertos.ibama.gov.br/dados/DOF/' + str(uf) + '/transporte/' + str(ano) + '.csv'
      print(url)
      df_temp = pd.read_csv(url, sep=";", decimal=",", low_memory=False)
      df = pd.concat([df, df_temp])
      print("Dados do ano {} Importados".format(ano))
    print("Dados da UF {} Importados".format(uf))
  print("Importação de dados concluída")
  return df

def get_cnpj_s(text):
    return text[0:10]


