#oilpython.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup

opt = webdriver.ChromeOptions()
opt.add_argument('headless') #hidden mode of chrome driver
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=opt) #create driver

url = 'http://www.pttor.com/oilprice-capital.aspx'

driver.get(url) #open web
time.sleep(3) #waiting 3 seconds

page_html = driver.page_source
driver.close()
data = soup(page_html,'html.parser') #scan data
table = data.findAll('table',{'id':'tbData'})
table = table[0].findAll('tbody')
rows = table[0].findAll('tr')
todayprice = rows[0].findAll('td')
#print(todayprice)

oiltitle = ['วันที่',
            'Diesel Premium',
            'Diesel',
            'DieselB10',
            'DieselB20',
            'Benzene',
            'Gasohol95',
            'Gasohol91',
            'GasoholE20',
            'GasoholE85',
            'NGV']
oilprice = []


for ol in todayprice:
    oilprice.append(ol.text)


result = {}

for t,o in zip(oiltitle,oilprice):
    result[t] = o

print(result)

from songline import Sendline

token = '1K37reP1tOCJfUjDdtjEb5sLjyjJth8TFVXkVvJR3Cj'
#token ไปออกเองในเว็บ https://notify-bot.line.me/my/

messenger = Sendline(token)
messenger.sendtext('ราคาดีเซลวันนี้: ' + result['Diesel'] + ' บาท')
messenger.sticker(12,1)




                           
