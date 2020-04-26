#!/usr/bin/env python
# coding: utf-8

# In[2]:


def function_check(a):
    b = a.isna()
    c = b.sum()
    return c;


# In[2]:


def function_summary(a,b,c):
    d = a.describe(include='all')
    e = b.describe(include='all')
    f = c.describe(include='all')
    return d,e,f;

