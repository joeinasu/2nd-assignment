#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def Sort_Tuple(tup):  
       
    a = len(tup)  
    for i in range(0, a):  
            
        for j in range(0, a-i-1):  
            if (tup[j][-1] > tup[j + 1][-1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
        return tup  
    
    
tup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
          
print(Sort_Tuple(tup))


# In[ ]:


#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
a = {'a':'97','b':'98','c':'99','d':'100','e':'101','f':'102','g':'103','h':'104','i':'105','j':'106','k':'107','l':'108','m':'109','n':'110','o':'111','p':'112','q':'113','r':'114','s':'115','t':'116','u':'117','v':'118','w':'119','x':'120','y':'121','z':'122'}
print(a) 

