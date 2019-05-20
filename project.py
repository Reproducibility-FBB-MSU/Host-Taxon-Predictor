import random


# Creating a list of 110 possible features
values = [i for i in range(110)]


dataset = []

# Number of samples
n = 10000 

for i in range(n):
    sample = []
    # 8 types of feature selection approaches were used 
    # 47 - the mean number of features chosen by one selection approach
    # One sample contains 8 lists
    # Each list contains 47 random features without repeats
    for i in range(8): 
        tmp = values[:]
        result = [tmp.pop(random.randrange(len(tmp))) for i in range(47)] 
        sample.append(result)
    
    # Counter conteins intersections of features among 8 lists in each sample
    
    counter = [set(sample[0]) & set(sample[1])]
    for i in sample:
         counter.append(counter[-1] & set(i))
    
    # Dataset contains lengths of intersections in all of the 10000 samples
    dataset.append(len(counter[-1]))

# final_data contains the approximate probability of getting intersection length = 0, 1 ...  
final_data = [dataset.count(i) / n for i in range(6)] 


import seaborn as sns
sns.set_style("darkgrid")
sns.set_palette("muted")


import matplotlib.pyplot as plt


height = final_data
bars = ('0', '1', '2', '3', '4', '5')
y_pos = [i for i in range(6)]
 
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)

plt.xlabel("Number of common elements in the intersection", size=10)
plt.ylabel("Fraction of intersections in each group", size=10)

plt.savefig("SF1.pdf")
plt.show()

