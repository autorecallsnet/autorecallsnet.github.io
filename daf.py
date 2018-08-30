import requests
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains

recall_titles = []
recall_shortDescs = []
lasttitle = ""
url = ""
cnt = 0

chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(chrome_options=chrome_options)  
urlDirec = 'https://www.nhtsa.gov/vehicle/'
paneltitles = ["recalls404-heading","recalls414-heading","recalls424-heading","recalls434-heading","recalls444-heading","recalls454-heading","recalls464-heading","recalls474-heading","recalls484-heading","recalls494-heading"]
action = action_chains.ActionChains(driver)

def recallSort():
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find('body').encode("ascii")
    # file = open("output.txt","w") 
    # file.write(str(body) )
    # file.close()
    recall_list = soup.find(id='recalls')
    recall_img = soup.find(class_='vehicle-base-details--hero')
    recall_img = recall_img.get('src')
    recall_items = recall_list.find_all(class_='panel-title-caption')

    flop = True
    for block in recall_items:
        recalls = block.find_all(string=True)   
        for item in recalls:
            if flop:
                if item.find("\n\t             "):
                    item = item[:len(item)-20]
                recall_titles.append(item)
                flop = False
            else: 
                recall_shortDescs.append(item)
                flop = True

    print(recall_img)
                
def getRecalls(url):
    driver.get(url)
    time.sleep(5)

    recallSort()

    # for i in range(2):  #It seems like this only works sometimes, have to debug. until then, only get first page of recalls
        # action.send_keys(Keys.TAB)
        # action.perform()
    # action.send_keys(Keys.TAB)    
    # action.send_keys(Keys.ENTER)
    # action.perform()

    # recallSort()        

    #print(recall_titles)


def getYears():

    driver.get("https://www.nhtsa.gov/vehicle")
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    year_list = soup.find(class_='container-fluid available-vehicle-links available-vehicle-links-type-modelYears')
    year_strings = year_list.find_all(string=True) #Years in string
    year_items = year_list.find_all('a') #For hypertext links

    for item in year_items:
        year_hrefs = "https://www.nhtsa.gov/vehicle" + item.get('href')
        print(year_hrefs)

    driver.close()
    
def getMake(Y):
    
    url = urlDirec + str(Y)
    print(url)
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    year_list = soup.find(class_='container-fluid available-vehicle-links available-vehicle-links-type-makes')
    year_strings = year_list.find_all(string=True) #Years in string
    year_items = year_list.find_all('a') #For hypertext links
    j = 0
    for item in year_items:
        year_hrefs = "https://www.nhtsa.gov" + item.get('href')
        getModel(Y, item.get('title'), year_hrefs)
        j = j + 1
    
    # for item in year_strings:
        # f.writerow([Y, item])
    
    
    
def getModel(Y, M, url):

    print(url)
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    year_list = soup.find(class_='container-fluid available-vehicle-links available-vehicle-links-type-models')
    try:
        year_strings = year_list.find_all(string=True) #Years in string
        year_items = year_list.find_all('a') #For hypertext links
    
        for item in year_items:
            href = "https://www.nhtsa.gov" + item.get('href')
            f.writerow([Y, M, item.get('title'), href])
    except:
        f.writerow([Y, M, "", ''])


def getVariant():

    driver.get("https://www.nhtsa.gov/vehicle/2012/CHRYSLER/200")
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    year_list = soup.find(class_='vehicle-detail vehicle-detail--multiple-choice container-fluid')
    year_strings = year_list.find_all(string=True) #Years in string
    year_items = year_list.find_all('a') #For hypertext links

    for item in year_items:
        year_hrefs = "https://www.nhtsa.gov/vehicle" + item.get('href')
        print(year_hrefs)

    driver.close()

# StartYear = 2010
# EndYear = 2013
# Year = StartYear
# YearList = []
# rest = 10
# while Year <= EndYear:
    # YearList.append(Year)
    # Year = Year + 1

# f = csv.writer(open('2010-2013VehDB_YMML_AUG18.csv', 'w'))
# f.writerow(['Year', 'Make', 'Model', 'Link'])

# for Y in YearList:
    # if cnt < rest:
        # cnt = cnt + 1
    # else:
        # cnt = 0
        # time.sleep(60)
    # getMake(Y)
getRecalls('https://www.nhtsa.gov/vehicle/2012/CHRYSLER/300/4%252520DR/AWD#recalls')    

driver.close()