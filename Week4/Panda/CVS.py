import pandas as pd


#df = pd.read_csv('Sample100.csv') #takes cvs file
df = pd.read_csv('text.txt') #takes txt file
print(df.to_string())



#-----------------
import pandas as pd 
mydataset = {
  'cars':
      ["BMW", "Volvo", "Ford"],
  'passings':
      [3, 7, 2]
}

df = pd.DataFrame(mydataset)
print(df.to_string())
