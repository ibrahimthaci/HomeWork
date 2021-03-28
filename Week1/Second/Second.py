from collections import Counter
import json

with open("File.txt", "w") as f:   # Opens file(create and write)and casts as f
    f.write("This is my new text on this text file and the name of file is: " + f.name)

file = open('File.txt', 'r').read() #ReadingFile
counter = Counter(file.lower().split()) #Splitting words
#print(counter)

counterToDic = {i : counter[i] for i in counter} #ConvertCounterToDic
print(counterToDic)
Json = json.dumps(counterToDic) #toJson
with open('JsonFile.json', 'w') as outfile:
    json.dump(Json, outfile) #WriteToFile



#TheOtherForm to Convert Counter to Dictonaries
#import pandas as pd

#Counter = Counter({"nan": 2, 'Hello': 6, 'blabla': 1})
#Test = pd.DataFrame.from_dict(repeaters, orient='index')
#print Test

# Rez :
# nan           2
# Hello         6
# blabla        1