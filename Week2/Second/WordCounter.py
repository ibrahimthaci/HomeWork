from collections import Counter
from matplotlib import pyplot as plt

file = open('TextFile.txt','r').read() #readfile
words= file.lower().replace('?','').replace('.','').replace(',','').split() #make all lowercase and replace , . ? etc to '' to make split
counter=Counter(words) #create counter to count how many times they are used
topfive=counter.most_common(5) # find 5 mos common words
b=dict(topfive) #convert to dictionaries, to use keys and values on plot bar as keys and values
print(b.values())

# keys=['it','at','or','he','to']
# values=[5,4,4,4,4]

plt.bar(b.keys(),b.values()) #p
plt.title("TOP 5 MOST USED WORDS")
plt.ylabel("WORDS FREQUENCY")
plt.xlabel("WORDS")
plt.show()
