#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import plotly.express as px

# 1. Importanto base de dados
tabela = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')


# In[13]:


# deletando colunas inúteis
tabela = tabela.drop(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Critic_Count', 'User_Count', 'Developer', 'Year_of_Release', 'Critic_Score', 'User_Score', 'Publisher', 'Name'], axis=1)

# acertando informaçoes que estao reconhecidas erroneamente pelo python
#tabela['User_Score'] = pd.to_numeric(tabela['User_Score'], errors='coerce') = caso estivesse na base de dados

# corrigindo informaçoes vazias
tabela = tabela.dropna()
display(tabela)


# In[14]:


# analise dos dados filtrados com grafico 
for coluna in tabela.columns:
    # cria o grafico
    grafico = px.histogram(tabela, x=coluna, y='Global_Sales', histfunc='avg', text_auto=True)
    # exibe o grafico
    grafico.show()


# In[15]:


#print(tabela.info()) -> exibe as informaçoes da tabela
# o jogo ideal para uma desenvolvedora seria um shooter apenas para adultos de preferencia para as plataformas playstation e xbox


# In[ ]:




