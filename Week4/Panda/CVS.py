import pandas as pd


#df = pd.read_csv('Sample100.csv')
df = pd.read_csv('text.txt')
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