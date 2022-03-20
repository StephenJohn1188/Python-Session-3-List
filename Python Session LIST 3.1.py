#!/usr/bin/env python
# coding: utf-8

# # Negative Indexing

# In[7]:


fruitlist=['Apple','Orange','Kiwi','Strawberry','Mango', 'Cherry']


# In[18]:


fruitlist[-6]


# In[9]:


len(fruitlist)


# In[17]:


fruitlist[-5]


# In[10]:


fruitlist[-5]


# In[11]:


fruitlist[-1]


# In[12]:


fruitlist[-2]


# In[14]:


fruitlist[-3]


# In[16]:


fruitlist[-4]


# Negative Slicing

# In[22]:


fruitlist[-2:-1]


# In[24]:


fruitlist[-3:-1]


# In[25]:


fruitlist[:]


# In[26]:


fruitlist[0:]


# In[27]:


fruitlist[:-1]


# Predefined Methods in List

# In[28]:


planetlist=['Mercury','Venus','Earth']


# In[29]:


planetlist


# In[30]:


planetlist.append('Mars')


# In[31]:


planetlist


# In[32]:


planetlist.append('saturn')


# In[34]:


planetlist


# In[35]:


planetlist.insert(1,'pluto')


# In[36]:


planetlist


# In[38]:


planetlist.index('pluto')


# In[39]:


planetlist.sort()


# In[40]:


planetlist


# In[41]:


planetlist.reverse()


# In[42]:


planetlist


# In[44]:


planetlist.extend(['uranus','neptune'])


# In[45]:


planetlist


# In[46]:


planetlist.pop()


# In[47]:


planetlist.index('Mercury')


# In[48]:


planetlist.pop(3)


# In[49]:


planetlist


# In[50]:


planetlist.remove('pluto')


# In[51]:


planetlist


# In[52]:


del planetlist


# Tuples

# In[54]:


t1=(1,2,3,4,5)


# In[55]:


t1


# In[57]:


t1[2]


# In[ ]:





# In[ ]:




