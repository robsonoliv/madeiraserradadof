#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:37:16 2023

@author: robsondeoliveira
"""

import pandas as pd
import gc
import dof_utils
import dof_constants as dofc


#importar os dados do dof
anos = ['2021']
uf_origem = ['PA', 'RO', 'AP', 'AM']
df = dof_utils.get_data_dof(uf_origem, anos)
gc.collect()
#importar os dados do dof

#////////////tratamento dos dados

#Transforma os dados
df['remetente'] = df['CPF/CNPJ do Remetente'].apply(dof_utils.get_cnpj_s)
df['destinatario'] = df['CPF/CNPJ do Destinatário'].apply(dof_utils.get_cnpj_s)
df['concessionaria'] = 0
df['tipo_concessao'] = 'indefinido'
df['nome_popular'] = df['Nome Popular'] 
df['uf_origem'] = df['UF de Origem'] 
df['uf_destino'] = df['UF de Destino'] 
df['tipo'] = df['Tipo de Origem']
df['pm3'] = df['Valor (R$)'] / df['Volume']
df['parte_relacionada'] = df['remetente'] == df['destinatario']
df['interestadual'] = df['UF de Origem'] != df['UF de Destino']
print(len(df))
#realiza os primeiros filtros
df = df[df['Valor (R$)'].notna()] #exclui linhas com o campo valor nulo
df = df[df['Valor (R$)']!=0] #exclui linhas com o campo valor zerado
df = df[df['Valor (R$)']>0] #exclui linhas com o campo valor negativo
df = df[df['Última Transação']=="Recebido"] #exclui linhas com quem tenha status diferente de recebido
df = df[df['Produto'].isin(dofc.PP)] #filtra apenas as madeiras de primeiro processamento
gc.collect()
print(len(df))
#////////////tratamento dos dados



#///////marcar transações concessionárias
df.loc[df["remetente"].isin(dofc.CNPJS_JHM), 'concessionaria'] = 1
for i, row in dofc.concessionarias.iterrows():  
  df.loc[df['Nome/Razão Social do Remetente'].str.contains(row['empresa-t']), 
            'concessionaria'] = 1
  df.loc[df['Nome/Razão Social do Remetente'].str.contains(row['empresa-t']), 
            'tipo_concessao'] = row['Tipo']

expressoes = ['Floresta Nacional', 'Flona', 'Floresta Estadual', 'Flota']

df['concessao_federal'] = 0

for i, row in df[(df['Nome do Pátio de Origem'].str.contains('Flona', 
                                                              na=False, 
                                                              case=False)) | 
   (df['Nome do Pátio de Origem'].str.contains('Floresta Nacional', 
                                                na=False, case=False)) ].iterrows():
    df.at[i, 'concessao_federal'] = 1
gc.collect()    
#///////marcar transações concessionárias




#filtra ano, estado origem e produto ecarrega em outro dataframe 'data' | passo não necessário

data = df

##exclui dados com valores extraordinários e zerados em cada grupo (concessionário e não)
data_c = data[data['concessionaria']==1]
data_nc = data[data['concessionaria']==0]
qntl = 0.999
qcs = data_c["pm3"].quantile(qntl)
qncs = data_nc["pm3"].quantile(qntl)
qci = data_c["pm3"].quantile(1-qntl)
qnci = data_nc["pm3"].quantile(1-qntl)
data_c = data_c[(data_c['pm3']<qcs) & (data_c['pm3']>qci)]
data_nc = data_nc[(data_nc['pm3']<qncs) & (data_nc['pm3']>qnci)]
gc.collect()
data = pd.DataFrame()
data = data.append(data_c)
data = data.append(data_nc)
#print(data['pm3'].max())
#print(data['pm3'].min())
print(data_c['Valor (R$)'].sum() / data_c['Volume'].sum())
data.to_excel('check_final_precos_2021_todos.xlsx') #exporta resultados para planilha excel para conferência manual

#removendo dados com valores extraordinários e zerados em cada grupo


#RESULTADOS

#cria um datafrane com os resultados do valor médio da madeira serrada, concessionária e não concessioária

p_grupo = data[['concessionaria', 'Valor (R$)', 'Volume' ]] \
                                        .groupby(['concessionaria']).sum() \
                                        .reset_index() \
                                        .sort_values(['concessionaria'], 
                                         ascending=True)                                      
p_grupo['m'] = p_grupo['Valor (R$)'] / p_grupo['Volume']

p_grupo.to_excel('resultados_medias.xlsx') #exporta resultados para planilha excel para conferência manual
vl_medio_concessionarias = float(p_grupo[p_grupo['concessionaria']==1]['m'])

#cria dataframe com os valores por cgrupo a serem utilizados no modelo

jat = pd.DataFrame(dofc.GRUPO_JAT) #tabelas com grupos e preços da pesquisa de campo de jatuarana
pr_cas = pd.DataFrame(dofc.GRUPO_PR_CAS) #tabelas com grupos e preços da pesquisa de campo de pau-rosa e castanho

base_medias = jat.merge(pr_cas, on='Grupo')
base_medias['media'] = base_medias[['Tora Jatuarana', 'Tora castanho']].mean(axis=1)
base_medias['fator_conversao_grupos'] = (base_medias['media'] / base_medias['media'].mean())
base_medias['valor_madeira_serrada'] = base_medias['fator_conversao_grupos'] * vl_medio_concessionarias
base_medias.to_excel('resultados_finais_modelo.xlsx') #exporta resultados para planilha excel para conferência manual

#RESULTADOS


