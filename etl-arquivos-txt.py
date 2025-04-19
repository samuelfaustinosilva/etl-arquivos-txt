#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas

# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# ### Extração

# In[26]:


df = pd.read_csv('NYNEWYOR.txt', delim_whitespace=True, header=None)


# In[27]:


df


# In[28]:


df.rename(columns={0: 'mês',
                  1: 'dia',
                  2: 'ano',
                  3: 'temperatura'},
         inplace=True)


# In[29]:


df


# ### Extração

# In[30]:


df.dtypes


# In[31]:


df.count()


# In[32]:


df.temperatura.value_counts()


# In[35]:


plt.figure(figsize=(30, 10))
sns.lineplot(x=df.index, y=df.temperatura)
plt.show()


# In[36]:


df.describe()


# In[37]:


df.temperatura = df.temperatura.replace(-99, np.nan)


# In[38]:


df['elemento_anterior'] = df.temperatura.shift(1)


# In[39]:


df['elemento_posterior'] = df.temperatura.shift(-1)


# In[40]:


df.head()


# In[41]:


df[df.temperatura.notnull() == False]


# In[42]:


df['back_fill'] = df.temperatura.bfill(axis=0)


# In[43]:


df['foward_fill'] = df.temperatura.ffill(axis=0)


# In[44]:


df.head()


# In[47]:


df['substituição'] = (df.temperatura.shift(1).ffill(axis=0) + df.temperatura.shift(-1).bfill(axis=0))/2


# In[48]:


df.head()


# In[51]:


df[df.temperatura.notnull() == False]


# In[52]:


df.temperatura = np.where(df.temperatura.notnull() == False,
                          df.substituição,
                          df.temperatura
                         )


# In[53]:


df


# In[54]:


plt.figure(figsize=(30, 10))
sns.lineplot(x=df.index, y=df.temperatura)
plt.show()


# In[55]:


df.describe()


# In[56]:


df['temperatura_celsius'] = (df.temperatura - 32)*(5/9)


# In[57]:


df.describe()


# In[ ]:




