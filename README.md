# Predicted-number-of-corona-infections
### 東京都の日別感染者数と平均気温、降水量、全国に占める割合、死者数を表示します
※2021年3月時点の結果

![graph](https://user-images.githubusercontent.com/79778717/192128727-4fc5604e-a9da-481f-847f-9f403455d7b5.png)

### 感染症数理モデル（SIRモデル）を用い今後の感染者数を予測します
※2021年3月時点の結果

![graph2](https://user-images.githubusercontent.com/79778717/192128766-7d0653d9-ba55-4bbb-8ad3-0b5c064d14a7.png)

#### main_data.py
weather_dlから気象情報を取得
infection_numberから感染者数を取得
recovery_numから回復した人数を取得
データのグラフ化
SIRモデルによる予測

#### weather_dl.py
東京都の気象情報を気象庁のページから取得

#### infection_number.py
コロナ感染者数死者数　国内データをNHKのページから取得

#### recovery_num.py
コロナ回復者数　国内データを厚生労働省のページから取得
