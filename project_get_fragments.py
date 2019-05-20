#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random

def create_random_fragment(sequence, length, substitution_rate, possible_base_symbols):
    assert len(sequence) >= length
    start_max = len(sequence) - length
    start = random.randint(0, start_max)
    return substitute_base(sequence[start:start + length], substitution_rate, possible_base_symbols)


# In[19]:


res = ""
with open("Downloads/seq4.fasta", "r") as f:
    for line in f:
        if ">" not in line:
            new_line = line.strip()
            res = res + new_line


# In[22]:


create_random_fragment(res, 100, 0.00, 4)


# In[23]:


with open("seq4.txt", "w") as f:
    f.write(create_random_fragment(res, 100, 0.00, 4))

