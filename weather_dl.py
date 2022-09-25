from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory":r"C:\Users\Souta\Pycharm\Colona"})#保存先の指定
options.add_argument('--ignore-certificate-errors') #SSLエラー対策
driver =webdriver.Chrome(ChromeDriverManager().install(),chrome_options = options)

from selenium.webdriver.support.select import Select

import datetime
oneday = datetime.timedelta(days=1)
yesterday = datetime.date.today() - oneday
y_y = yesterday.year
y_m = yesterday.month
y_d = yesterday.day

main_url = 'https://www.data.jma.go.jp/gmd/risk/obsdl/index.php'#気象庁
driver.get(main_url)
sleep(1)

#東京都
elem_btn_prefecture = driver.find_element_by_id('pr44')
elem_btn_prefecture.click()
sleep(1)

elem_btn_station = driver.find_element_by_xpath('//*[@id="stationMap"]/div[9]/div')
elem_btn_station.click()
sleep(1)

#要素入力
elem_btn_element = driver.find_element_by_id('elementButton')
elem_btn_element.click()
sleep(1)

elem_btn_rain = driver.find_element_by_id('ui-id-3')
elem_btn_rain.click()
sleep(1)

elem_btn_rain_data = driver.find_element_by_id('降水量の合計')
elem_btn_rain_data.click()
sleep(1)

elem_btn_temp = driver.find_element_by_id('ui-id-2')
elem_btn_temp.click()
sleep(1)

elem_btn_temp_data = driver.find_element_by_id('平均気温')
elem_btn_temp_data.click()
sleep(1)
#時間
elem_btn_period = driver.find_element_by_id('periodButton')
elem_btn_period.click()
sleep(1)

elem_iniy = driver.find_element_by_name('iniy')
select = Select(elem_iniy)
select.select_by_index(1)

elem_inim = driver.find_element_by_name('inim')
select = Select(elem_inim)
select.select_by_index(0)

elem_inid = driver.find_element_by_name('inid')
select = Select(elem_inid)
select.select_by_index(15)

elem_endy = driver.find_element_by_name('endy')
select = Select(elem_endy)
select.select_by_index(y_y - y_y)


elem_endm = driver.find_element_by_name('endm')
select = Select(elem_endm)
select.select_by_index(y_m - 1)


elem_endd = driver.find_element_by_name('endd')
select = Select(elem_endd)
select.select_by_index(y_d - 1)


#ファイルダウンロード
elem_download = driver.find_element_by_id('csvdl')
elem_download.click()
sleep(1)

#ブラウザ閉
driver.quit()

#昨日の年月日取得
yesterday_data = str(y_y)+'/'+str(y_m)+'/'+str(y_d)