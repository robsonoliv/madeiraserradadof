#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:42:16 2023

@author: robsondeoliveira
"""
import pandas as pd

# Constantes utilizadas no pipelane de dados

#Madeiras primeiro processamento
PP = [
        'Madeira serrada (caibro)',
        'Madeira serrada (prancha)',
        'Madeira serrada (pranchão desdobrado)',
        'Madeira serrada (tábua)',
        'Madeira serrada (viga)',
        'Madeira serrada (vigota)', 
        'Sarrafo'
        ]

#CNPJs das concessionárias
CNPJS_JH = ['10.372.884/0001-69',
            '15.294.432/0004-72',
            '05.769.858/0001-39',
            '04.342.370/0001-68',
            '13.860.459/0001-07',
            '04.119.669/0001-58',
            '04.420.254/0001-10',
            '15.294.432/0005-53']

CNPJS_JHM = []
for cn in CNPJS_JH:
    CNPJS_JHM.append(cn[0:10])


#Nomes das concessionárias
NOMES_CONCESSIONARIAS = {'Empresa': {0: 'Madeflona Industrial Madeireira Ltda.',
  1: 'Benevides Madeiras Ltda. - EPP',
  2: 'Brasadoc Timber Comércio de Madeiras Ltda.',
  3: 'Cemal Comércio Ecológico de Madeiras Ltda. - EPP',
  4: 'Ebata Produtos Florestais Ltda.',
  5: 'Golf Indústria, Comércio e Exploração de Madeireiras Ltda.',
  7: 'Patauá Florestal Ltda. - SPE',
  8: 'RRX Mineração e Serviços Ltda. - EPP',
  9: 'RRX Timber Export - EIRELI',
  10: 'RRX Timber Export - EIRELI\xa0',
  11: 'Samise Indústria, Comércio e Exportação Ltda.',
  12: 'Viviane Miyamura Loch - EPP',
  13: 'CEMAL COMeRCIO ECOLOGICO DE MADEIRAS LTDA. EPP',
  14: 'MADEIRAS SEGREDO LTDA. EPP',
  15: 'RRX MINERAÇÃO E SERVIÇOS LTDA - ME.',
  16: 'BLUE TIMBER CONSULTORI A E ASSESSORI A LTDA.',
  19: 'LN Guerra Indústria e Comércio de Madeiras Ltda.',
  20: 'Rondobel Indústria e Comércio de Madeiras Ltda',
  21: 'Amazônia Florestal Ltda',
  22: 'TRANSWOOD TRANSPOTE E LOGISTICA LTDA.'},
 'Tipo': {0: 'Federal',
  1: 'Federal',
  2: 'Federal',
  3: 'Federal',
  4: 'Federal',
  5: 'Federal',
  7: 'Federal',
  8: 'Federal',
  9: 'Federal',
  10: 'Federal',
  11: 'Federal',
  12: 'Federal',
  13: 'Estadual',
  14: 'Estadual',
  15: 'Estadual',
  16: 'Estadual',
  19: 'Estadual',
  20: 'Estadual',
  21: 'Estadual',
  22: 'Estadual'},
 'empresa-t': {0: 'MADEFLONA ',
  1: 'BENEVIDES ',
  2: 'BRASADOC T',
  3: 'CEMAL COMÉ',
  4: 'EBATA PROD',
  5: 'GOLF INDÚS',
  7: 'PATAUÁ FLO',
  8: 'RRX MINERA',
  9: 'RRX TIMBER',
  10: 'RRX TIMBER',
  11: 'SAMISE IND',
  12: 'VIVIANE MI',
  13: 'CEMAL COME',
  14: 'MADEIRAS SEGREDO',
  15: 'RRX MINERA',
  16: 'BLUE TIMBE',
  19: 'LN GUERRA ',
  20: 'RONDOBEL I',
  21: 'AMAZÔNIA F',
  22: 'TRANSWOOD '}}
concessionarias = pd.DataFrame(NOMES_CONCESSIONARIAS)



GRUPO_JAT = {'Grupo': {0: 'Grupo 1', 1: 'Grupo 2', 2: 'Grupo 3', 3: 'Grupo 4'},
 'Tora Jatuarana': {0: 369.71, 1: 256.23, 2: 202.87, 3: 135.85}}


GRUPO_PR_CAS = {'Grupo': {0: 'Grupo 1', 1: 'Grupo 2', 2: 'Grupo 3', 3: 'Grupo 4'},
 'Tora castanho': {0: 545.88, 1: 470.98, 2: 374.87, 3: 302.38}}

# Constantes utilizadas no pipelane de dados