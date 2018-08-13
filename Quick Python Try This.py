
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy = True')


# In[21]:


#Suppose you have a list where each element is in turn a list,[[1,2,3] , [2,1,3], [4,0,1]] . 
#If you wanted to sort this list by the second element in each list so that the result would: [[4,0,1], [2,1,3], [1,2,3]], what function would you write to pass as the key value to the sort() method

a = [[1,2,3] , [2,1,3], [4,0,1]]


def compare_arg2(x):
    return x[1]

    
a.sort(key = compare_arg2)
assert a == [[4,0,1], [2,1,3], [1,2,3]]
print('The sorted list is: ', a)

