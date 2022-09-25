from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())

#コロナから回復した人数の取得
url='https://www.mhlw.go.jp/stf/covid-19/kokunainohasseijoukyou.html'
driver.get(url)
sleep(2)

num = driver.find_element_by_xpath('//*[@id="current_situation"]/table/tbody/tr[1]/td[5]')
num = num.text
num = num.split('\n')[0]
num = num.replace(',','')
num = float(num)
driver.quit()