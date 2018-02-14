
# coding: utf-8

# In[1]:


import numpy


# In[28]:


def set_node(File, Node, out_list, prob_list):
    s = '%i'%(Node)
    Len = len(out_list)
    for i in range(Len):
        s += ',%i,%.2f'%(out_list[i], prob_list[i])
    
    F.write(s[:-1])
    F.write('\n')


# In[29]:


Data = []

outS = [1]
proS = [1.0]
Data.append([0,outS,proS])


# In[30]:


out = [2,3]
pro = [0.4,0.6]
Data.append([1,out,pro])

out = [3,-1]
pro = [0.2,0.8]
Data.append([2,out,pro])

out = [4,5,6]
pro = [0.3,0.2,0.5]
Data.append([3,out,pro])
#######################
out = [7,8]
pro = [0.35,0.65]
Data.append([4,out,pro])

out = [9,10]
pro = [0.55,0.45]
Data.append([5,out,pro])

out = [11,12]
pro = [0.5,0.5]
Data.append([6,out,pro])
#######################
out = [13]
pro = [1]
Data.append([7,out,pro])

out = [13]
pro = [1]
Data.append([8,out,pro])
#######################
out = [14]
pro = [1]
Data.append([9,out,pro])

out = [14]
pro = [1]
Data.append([10,out,pro])
#######################
out = [15]
pro = [1]
Data.append([11,out,pro])

out = [15]
pro = [1]
Data.append([12,out,pro])
#######################
out = [16]
pro = [1]
Data.append([13,out,pro])

out = [16]
pro = [1]
Data.append([14,out,pro])

out = [16]
pro = [1]
Data.append([15,out,pro])
#######################
out = [1]
pro = [1]
Data.append([16,out,pro])


# In[31]:


F = open('test_1.graph','w')

for d in Data:
    set_node(F,d[0],d[1],d[2])
F.write('-1')
F.close()

