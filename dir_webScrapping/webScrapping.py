
from os import close
from bs4 import BeautifulSoup
import requests as rq
import csv

# open a file using content manager
# with open('dir_webScrapping\scrapping.csv','w') as csv_file: # w stands for writting in a file and if we want to read a file we will pass in r
#     csv_writter = csv.writer(csv_file)
#     csv_writter.writerow('Title','Tag')

csv_file = open('dir_webScrapping\scrapping.csv','w')
csv_writter = csv.writer(csv_file)
csv_writter.writerow(['Title','Tag'])
csv_file.close()

def getContent():
    result = rq.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    soup = BeautifulSoup(result.text,'lxml')
    #content = soup.prettify()
    #content = soup.title
    # content = soup.title.text
    # content = soup.div  # this is going to give us the first div
    content = soup.find('div',{'id':'detailed-forecast-body'})
    for x in content:
        for y in x.div:
            for z in y.div:
                print(z.b)
    # content = text.b
    # content = soup.find_all('div',{'id':'detailed-forecast'}).prettify()




    #print(content)



getContent()

    

