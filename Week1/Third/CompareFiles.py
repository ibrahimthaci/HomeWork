file1 = open('Text1.txt', 'r').read().lower().replace('.', '').replace(',', '').split()
file2 = open('Text2.txt', 'r').read().lower().replace('.', '').replace(',', '').split()
SetFile1 = (set(file1)) #Sets
SetFile2= (set(file2)) #Sets

print(SetFile1)#Reading whole file after creation of sets
print(SetFile2)#Reading whole file after creation of sets
print("")

SameWords = SetFile1.intersection(SetFile2) #FindingSameWordsOnSETS
print ('Printing same words from two different files: ')
for i in SameWords:
    print(i, end=" ")







#.replace('?','') , replace(',','') we can and in first line more
# replace functions to replace words we think we
#can find