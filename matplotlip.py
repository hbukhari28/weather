#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')


# In[47]:


temp_data = [80,90,77,79,75,75,73,81,77,81,95,93,95,97,98,99,97,92,94,92,83,83,83,81]
wind_data = [12,10,12,8,12,12,12,13,17,18,18,7,25,10,10,0,16,9,9,9,5,7,4,3]
time_hrs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
humidity_data = [73,76,78,81,81,84,84,79,71,68,58,55,51,46,48,53,60,67,69,73,66,55,87,67]
precipitation_data = [36,88,74,47,26,42,69,48,26,21,58,69,74,53,79,53,79,53,58,26,74,95,69,58]


# In[29]:


plt.figure(figsize=(8,4))
plt.subplots_adjust(hspace=.25)
plt.subplot(1,2,1)
plt.title('Temp')
plt.plot(time_hrs,temp_data,color = 'b' , linestyle='-',linewidth=1)
plt.subplot(1,2,2)
plt.title('wind')
plt.plot(time_hrs,wind_data,color='r',linestyle='-',linewidth=1)


# In[48]:


plt.figure(figsize=(6,6))
plt.subplots_adjust(hspace=.25)
plt.subplot(2,1,1)
plt.title('Humidity')
plt.plot(time_hrs,humidity_data,color='b',linestyle='-',linewidth=1)
plt.subplot(2,1,2)
plt.title('Precipitation')
plt.plot(time_hrs,precipitation_data,color='r',linestyle='-',linewidth=1)
plt.show()


# In[50]:


plt.figure(figsize=(9,9))
plt.subplots_adjust(hspace=.3)
plt.subplot(2,2,1)
plt.title('Temp (f)')
plt.plot(time_hrs,temp_data,color = 'b' , linestyle='-',linewidth=1)
plt.subplot(2,2,2)
plt.title('wind(MPH)')
plt.plot(time_hrs,wind_data,color='r',linestyle='-',linewidth=1)
plt.subplot(2,2,3)
plt.title('Humidity(%)')
plt.plot(time_hrs,humidity_data,color='b',linestyle='-',linewidth=1)
plt.subplot(2,2,4)
plt.title('Precipitation(%)')
plt.plot(time_hrs,precipitation_data,color='r',linestyle='-',linewidth=1)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




