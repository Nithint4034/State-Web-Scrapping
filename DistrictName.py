import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(executable_path=r"F:\web2\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://puducherry.s3waas.gov.in/")
time.sleep(2)

data = []
soup = BeautifulSoup(driver.page_source, 'html.parser')

showroom_entries = soup.find_all('div', 'dist-box')
for entry in showroom_entries:
    d = entry.find('span')
    # e = entry.find('p','cmp-locations-office-details__address-detail')
    # f = entry.find('a','cmp-locations-office-details__link cmp-locations-office-details__link--direction')
    # g = entry.find('div','cmp-locations-office-details__link cmp-locations-office-details__link--phone')

    row = []
    if d:
        row.append(d.text.strip())
    else:
        row.append('')

    # if e:
    #     row.append(e.text.strip())
    # else:
    #     row.append('')

    # if f:
    #     x = f.get('href')
    #     final = x.split('=')[2].replace('&lvl', '').replace('~', ',')
    #     row.append(final.strip())
    # else:
    #     row.append('')

    # if g:
    #     row.append(g.text.strip().replace('+91',''))
    # else:
    #     row.append('')

    data.append(row)

filename = 'Puducherry.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['DISTRICTS NAME'])  
    writer.writerows(data)

print('Data saved in', filename)

driver.quit()
