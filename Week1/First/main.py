import json

myRecord={                    #Creatin dictionaries
    'name': 'Ibrahim',
    'lastName': 'Thaci',
    'Age':'23',
    'University': 'Ukshin Hot'
}

j= json.dumps(myRecord)                     #convert dc to json, open,write and close
with open('MyRecord.json', 'w') as f:
 f.write(j)
 f.close()


myRecord = json.load(open('MyRecord.json'))  #load json and print
print(myRecord)

with open('MyRecord.json') as jsonFile: #json Read file
    data=json.load(jsonFile)            #Convert json to dc
    #print("Type", type(data))          #Testing type of data

print(data)                             #printing
print(data['lastName'])                 #prining only lastname
