from collections import Counter
from matplotlib import pyplot as plt

file = open('TextFile.txt','r').read()
words= file.lower().replace('?','').replace('.','').replace(',','').split()
counter=Counter(words)
topfive=counter.most_common(5)
print(topfive)

keys=['it','at','or','he','to']
values=[5,4,4,4,4]

plt.bar(keys,values)
plt.title("Fjalët më të shpeshta")
plt.ylabel("Numri i përseritjeve")
plt.xlabel("Fjalët")
plt.show()
