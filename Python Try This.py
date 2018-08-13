
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


# In[11]:


# concatenating dataframes where some axis differ

import pandas  as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
 
    

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                      'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                       'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

frames = [df1, df2, df3]
result = pd.concat(frames)
print(result)


# In[22]:


# concatenating dataframes on Axis 0, ignore index wipe out the original index

import pandas  as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 7])
 
    

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[0, 1, 2, 11])

frames = [df1, df2, df3]
result = pd.concat(frames, ignore_index = True)
print(result)


# In[23]:


# concatenating dataframes on Axis 1, eliminiate indicies that do no intersect (join='inner')

import pandas  as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 5, 6])
 
    

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                      'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                       'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[0, 1, 2, 10])

frames = [df1, df2, df3]
result = pd.concat(frames, axis=1, join='inner')
print(result)


# In[28]:


# seriously! uses only the indicies that are named and ignore the others

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
 
    

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                      'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                       'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

pieces = {'x': df1, 'y': df2, 'z': df3}
result = pd.concat(pieces, keys=['z', 'y'])
print(result)
result.index.levels

