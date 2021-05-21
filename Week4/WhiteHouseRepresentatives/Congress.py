from bs4 import BeautifulSoup
import requests

url = "https://www.house.gov/representatives"
html = requests.get(url).text
soup = BeautifulSoup(html,'html5lib')
p = soup.find_all('td', {'class': 'views-field-text-11'})
for i in p:
    print(i.text) #this prints only text inside td, which are td>a> this is text<a<td
    #print(str(i)[135:-17]) # prints all html tags of that class
    #print(i)





#table = soup.find_all('td', {'class': 'views-field'}) ##just a test
#for row in table.find_all("a"):
#print(str(row))





############################
#Prints all text from website(webpage)
#test=BeautifulSoup(html,'html5lib')
#for row in test.find_all():
    #print(row) #if we let only print(row) will display html tree



################ another method but it works finding only first td>a element
# test=BeautifulSoup(html,'html5lib')
# table = test.find('td', {'class':'views-field-text-11'})
# for i in table.find_all('a'):
#     #print(i.text)