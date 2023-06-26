#!/usr/bin/env python
# coding: utf-8

# # Python e Finanças
# 
# ### Uma das grandes aplicações do Python é para Finanças/Mercado Financeiro
# 
# ### Não é bem uma integração, pois usaremos bibliotecas que já conhecemos, só que aplicadas a ativos financeiros
# 
# 1. pandas
# 2. matplotlib
# 3. numpy
# 
# Essas são as 3 principais bibliotecas usadas. Então essencialmente é uma aplicação de tudo o que aprendemos nessas 3 bibliotecas.
# 
# Vamos instalar também o pandas_datareader para puxar cotações diretamente do yahoo finance. Use o pip para isso.

# ### Vamos analisar o IBOV

# In[12]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2022-12-01'
end_date = '2023-06-25'
ticker = '^BVSP'

cotacao_ibov = yf.download(ticker, start=start_date, end=end_date)
display(cotacao_ibov)


# ### Analisando o Gráfico

# In[14]:


cotacao_ibov['Adj Close'].plot(figsize=(15,5))


# ### Retorno do IBOV

# In[16]:


retorno_ibov = cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0] -1
print(f'Retorno IBOV: {retorno_ibov:.2%}')


# ### Analisando com Média Móvel

# In[24]:


cotacao_ibov['Adj Close'].plot(figsize=(15,5), label='IBOV')
cotacao_ibov['Adj Close'].rolling(21).mean().plot(label='MM21')
cotacao_ibov['Adj Close'].rolling(35).mean().plot(label='MM35')
plt.legend()
plt.show()


# In[ ]:




