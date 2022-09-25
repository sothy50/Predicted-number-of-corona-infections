import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import japanize_matplotlib

#気象情報　取得
import weather_dl

weather_df = pd.read_csv('data.csv',encoding='shift_jis',header=2)
weather_df = weather_df[['降水量の合計(mm)','平均気温(℃)']]
weather_df = weather_df[1:]
weather_df.reset_index(inplace=True,drop=True)

#感染者数　取得
import infection_number

df_domestic = infection_number._df_domestic
df_domestic.reset_index(inplace=True,drop=True)
df_prefectures = infection_number._df_prefectures
df_tokyo = infection_number._df_tokyo
df_tokyo.reset_index(inplace=True,drop=True)
#df_hokkaido = infection_number._df_hokkaido
#df_osaka = infection_number._df_osaka

#回復した人数
import recovery_num
recovery = recovery_num.num

#取得したデータの結合
combine = [df_domestic,weather_df,df_tokyo]
df = pd.concat(combine,axis = 1)

x1 = df['日付']
y1 = df['国内の感染者数_1日ごとの発表数']
y2 = df['降水量の合計(mm)']
y3 = df['平均気温(℃)']
y4 = df['各地の感染者数_1日ごとの発表数']
y5 = df['国内の死者数_累計']
y6 = df['国内の感染者数_累計']

#グラフ化
plt.figure(figsize=(14,6))
plt.subplots_adjust(wspace=0.6, hspace=0.5)

#日付-感染者数(全国,東京)
plt.subplot(232)
plt.bar(x1,y1,label='全国')
plt.bar(x1,y4,color='orange',label='東京都')
plt.xlabel('日付')
plt.ylabel('感染者数(人)')
plt.ylim(0,8000)
plt.vlines(['2020/1/16'],0,8000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2020/4/7'],0,8000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2020/5/25'],0,8000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2021/1/7'],0,8000,'red',linestyles='dashed',alpha=0.5)
plt.xticks(['2020/1/16','2020/4/7','2020/5/25','2021/1/7'],['1/16','4/7 ',' 5/25','2021/1/7'])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=8)

#日付-感染者数,気温
ax1 = plt.subplot(234)
ax1.bar(x1,y4,color='orange')
ax1.set_xticks([])
ax2 = ax1.twinx()
ax2.plot(x1,y3,color='blue',alpha=0.7,linewidth=0.5)
ax1.set_ylim(0,2500)
ax1.vlines(['2020/1/16'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2020/4/7'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2020/5/25'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2021/1/7'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.set_xticks(['2020/1/16','2020/4/7','2020/5/25','2021/1/7'])
ax1.set_xticklabels(['1/16','4/7 ',' 5/25','2021/1/7'])
ax2.set_ylim(-10,40)
ax1.set_xlabel('日付')
ax1.set_ylabel('東京都 感染者数(人)')
ax2.set_ylabel('東京都 平均気温(℃)')

#日付-感染者数,降水量
ax1 = plt.subplot(235)
ax1.bar(x1,y4,color='orange')
ax1.set_xticks([])
ax2 = ax1.twinx()
ax2.bar(x1,y2,color='blue',alpha=0.7)
ax1.set_ylim(0,2500)
ax1.vlines(['2020/1/16'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2020/4/7'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2020/5/25'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.vlines(['2021/1/7'],0,2500,'red',linestyles='dashed',alpha=0.5)
ax1.set_xticks(['2020/1/16','2020/4/7','2020/5/25','2021/1/7'])
ax1.set_xticklabels(['1/16','4/7 ',' 5/25','2021/1/7'])
ax1.set_xlabel('日付')
ax1.set_ylabel('東京都 感染者数(人)')
ax2.set_ylabel('東京都 降水量の合計(mm)')

#日付-感染者数,死者数
plt.subplot(236)
plt.plot(x1,y6,label='感染者数')
plt.plot(x1,y5,label='死者数')
plt.xlabel('日付')
plt.ylabel('人数(人)')
plt.ylim(0,500000)
plt.vlines(['2020/1/16'],0,500000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2020/4/7'],0,500000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2020/5/25'],0,500000,'red',linestyles='dashed',alpha=0.5)
plt.vlines(['2021/1/7'],0,500000,'red',linestyles='dashed',alpha=0.5)
plt.xticks(['2020/1/16','2020/4/7','2020/5/25','2021/1/7'],['1/16','4/7 ',' 5/25','2021/1/7'])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=8)

plt.show()
df.to_csv('export.csv',encoding='shift_jis')
os.remove("data.csv")


df_fu = df.set_index('日付')
yesterday = weather_dl.yesterday_data
death = df_fu.loc[yesterday,'国内の死者数_累計']
infection = df_fu.loc[yesterday,'国内の感染者数_累計']

#SIRモデル
#変数　var[0],var[1],var[2]
#var[0] 未感染者S
#var[1] 感染者数I
#var[2] 回復者，死者R
#r=0.1 #回復率
#b=0.1 #感染率

import numpy as np
from scipy.integrate import odeint
import matplotlib.ticker as ptick
from matplotlib.ticker import ScalarFormatter

def func(var, t, b, r):
    dSdt = -b * var[0] * var[1]
    dIdt = b * var[0] * var[1] - r * var[1]
    dRdt = r * var[1]

    return [dSdt, dIdt, dRdt]

total = 125620000.0 #定数

S = float(total - infection)
I = float(infection)
R = float(recovery + death)

var_init=[S,I,R]#初期値
t_list = np.linspace(0,100,1000)#離散化

#基本再生産数　R0 = N(初期集団サイズ)*b/r =1.5~2.5(2)

r=0.5 #回復率
b=1/125620000.0 #感染率
np.set_printoptions(formatter={'float': '{:.1f}'.format})
var_list =odeint(func,var_init,t_list,args=(b,r))

plt.plot()
plt.plot(var_list)
plt.gca().ticklabel_format(style="plain",  axis="y")
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.xlabel('日数(日)')
plt.ylabel('人数(人)')

plt.show()
