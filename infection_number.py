import requests
import pandas as pd
import io

#コロナ感染者数死者数　国内データ
target_url = 'https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_domestic_daily_data.csv'
target = requests.get(target_url).content
_df_domestic = pd.read_csv(io.BytesIO(target),sep=',')
#_df_domestic = _df_domestic[['日付','国内の感染者数_1日ごとの発表数','国内の死者数_1日ごとの発表数']]

#コロナ感染者数死者数　都道府県別データ
target_url = 'https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv'
target = requests.get(target_url).content
_df_prefectures = pd.read_csv(io.BytesIO(target),sep=',')
_df_prefectures = _df_prefectures[['都道府県名','各地の感染者数_1日ごとの発表数','各地の死者数_1日ごとの発表数']]

_df_tokyo =_df_prefectures[_df_prefectures['都道府県名']=='東京都']
_df_tokyo = _df_tokyo[['各地の感染者数_1日ごとの発表数','各地の死者数_1日ごとの発表数']]
#_df_hokkaido =_df_prefectures[_df_prefectures['都道府県名']=='北海道']
#_df_osaka =_df_prefectures[_df_prefectures['都道府県名']=='大阪府']

