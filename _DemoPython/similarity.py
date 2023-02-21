#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cosine_similarity(input1,input2):
    
    # dot product (A . B)
    
    dot_product = (input1[0] * input2[0]) + (input1[1] * input2[1]) + (input1[2] * input2[2])
    
    # magnitude ||A||
    
    
    #create muna empty list for container
    squared_numbers_A=[]
    for num in input1:
        """ issquare natin per item sa list then isquare-root yung total nila
        """
        squared_num = num ** 2
        squared_numbers_A.append(squared_num)
       
    total = sum(squared_numbers_A)
    magnitude_A = total ** 0.5
    
    # magnitude ||B||
    
    #create muna empty list for container
    squared_numbers_B=[]
    for num in input2:
        squared_num = num ** 2
        squared_numbers_B.append(squared_num)
       
    total = sum(squared_numbers_B)
    magnitude_B = total ** 0.5
    
    return dot_product / (magnitude_A*magnitude_B)
    

