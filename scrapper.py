import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# open website in browser
browser = webdriver.Chrome("chrimedriver.exe")
browser.get("https://coinmarketcap.com/")

# find historical data
time.sleep(10)
browser.find_element(By.PARTIAL_LINK_TEXT, "Bitcoin").click()
time.sleep(10)
browser.find_element(By.PARTIAL_LINK_TEXT, "Historical Data").click()

# open previous records
time.sleep(10)
n = 1
while True or (n >= 200):
    try:
        browser.find_element(By.XPATH, '//button[text()="Load More"]').click()
        time.sleep(10)
        if (n % 10) == 0:
            print("Click N{} is over!".format(n))
        n += 1
    except:
        print("Scrapping Is Done")
        break

# grab html to parse
html = browser.page_source

# close browser
browser.close()

# prettify html & prepare for data extraction
soup1 = BeautifulSoup(html, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# find table & extract data
data = []
table = soup2.find(class_='sc-beb003d5-3 cxLkYn cmc-table').find('tbody').find_all('tr')
for row_num in range(len(table)):
    values = table[row_num].find_all('td')
    data.append([i.text.strip() for i in values])

# create pandas dataframe
df = pd.DataFrame(data)
# change column names
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

# save scrapped data as csv file in current directory
df.to_csv("data.csv", index=False)