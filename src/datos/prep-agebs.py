#!/usr/bin/env python
# coding: utf-8

# # Transformando los datos de AGEBS
# 
# Tomando datos del marco geoestadistico de INEGI creamos un .zip con solo los agebs rurales y urbanos por estado. 
# 
# La meta de este notebook es juntar todos estos agebs en un solo documento.

# In[1]:


import geopandas as gpd
from zipfile import ZipFile
from pathlib import Path
import pandas as pd


# In[4]:


THIS_FILE = Path.cwd()
THIS_FILE


# In[5]:


DATOS_PROCESADOS = THIS_FILE.joinpath("../../datos/procesados/")


# In[6]:


archivo = ZipFile(DATOS_PROCESADOS / 'AGEBS.zip')


# In[7]:


archivo.filelist


# In[8]:


archivo.extractall(DATOS_PROCESADOS)


# In[9]:


archivos_shp = DATOS_PROCESADOS.joinpath("AGEBS_/").glob("*.shp")


# In[13]:


datos = pd.concat((gpd.read_file(file) for file in archivos_shp), ignore_index = True)


# In[14]:


datos.head()


# In[15]:


datos.info()


# In[16]:


datos_limpios = datos[['CVEGEO', 'geometry']].copy()


# In[17]:


datos_limpios.head()


# In[18]:


datos_limpios.to_file(DATOS_PROCESADOS / 'AGEBS_limpio.shp', index = False)

