#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:31:07 2023

@author: robsondeoliveira
"""

from statsmodels.formula.api import ols



# Utilizando-se o dataframe "data" do arquivo "madeira_serrada_tc.py"
#///////Regressões
result = ols(
    formula=" pm3 ~ nome_popular + Produto + uf_destino + concessionaria + parte_relacionada", 
    data=data).fit()
summary = str(result.summary())

#///////Regressões