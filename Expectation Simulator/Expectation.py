
# coding: utf-8

# In[1]:


import csv


# In[2]:


# 0: Source -1: Target
Nodes = {-1:None}
Total_Node = 0


# In[3]:


class Node:
    def __init__(self, my_ID, num_link_to, to_list, prob_list):
        self.ID = my_ID
        self.num_link = num_link_to
        self.to_list = to_list
        self.prob_list = prob_list
        


# In[4]:


F = open('test_1.graph','r')
CF = csv.reader(F)
for line in CF:
    num_node = (int)((len(line)-1)/2)
    to_list = []
    prob_list = []
    ID = (int)(line[0])
    for i in range(num_node):
        to_list.append((int)(line[2*i+1]))
        prob_list.append((float)(line[2*i+2]))
        
    Nodes[ID] = Node(ID,num_node, to_list, prob_list)
    Total_Node += 1

F.close()


# In[5]:


# Simulation
Prob_Graph = [[1.0]]
for i in range(Total_Node-1):
    Prob_Graph.append([]) # Source
print(Total_Node)


# In[6]:


# Starting Node(s)
Now_At = set([0])


# In[7]:


def Simulate_Node(NowAt):
    global Nodes, Prob_Graph
    next_At = set([])
    for i in NowAt:
        if i == -1:  # ending in target node
            continue
        for tar in range(Nodes[i].num_link):
            Prob_Graph[Nodes[i].to_list[tar]].append(0.0)
            Prob_Graph[Nodes[i].to_list[tar]][-1] +=                 Nodes[i].prob_list[tar] * Prob_Graph[i][-1]
            
            next_At.add(Nodes[i].to_list[tar])
        
    # Update to the next step
    return next_At


# In[8]:


while len(Prob_Graph[-1]) < 10:
    Now_At = Simulate_Node(Now_At)


# In[9]:


Prob_Graph


# In[10]:


P = 0
for d in Prob_Graph[-1]:
    P += d

print(P)

