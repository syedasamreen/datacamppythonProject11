import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline
# Reading and sorting by rows and count..
df1 = pd.read_csv(r"C:\Users\RAGHAVENDRA KATAKAM\Desktop\datacamp python\datacamp datasets\btc_06122017.csv")
market_cap = df1[['id','market_cap_usd']]
print(market_cap.count())
# Removing NAn and count
cap = market_cap.query('market_cap_usd> 0')
print(cap.count())
# Bar plot for crypto
TOP_cap_title = "Top 10 market capitalization"
TOP_cap_ylabel ='% of total cap'
cap10= cap[:10].set_index('id')
cap10 = cap10.assign(market_cap_perc = lambda x:(x.market_cap_usd /cap.market_cap_usd.sum())*100)
ax = cap10.market_cap_perc.plot.bar(title= TOP_cap_title)
ax.set_ylabel(TOP_cap_ylabel);
# plt.show()
COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']
ax = cap10.market_cap_usd.plot.bar(title=TOP_cap_title,logy=True,color = COLORS)
ax.set_ylabel('USD')
ax.set_xlabel('');
# plt.show()
#  volatility in crypto

volatility = df1[['id','percent_change_24h','percent_change_7d']]
volatility = volatility.set_index('id').dropna()
volatility = volatility.sort_values('percent_change_24h')
# print(volatility.head())

#  Top 10 gainers and loosers

def top10_subplot(volatility_series,title):
    fig,axes = plt.subplots(nrows=1,ncols=2,figsize =(10,6))
    ax= volatility_series[:10].plot.bar(color ="darkred",ax=axes[0])
    fig.suptitle(title)
    ax.set_ylabel('% change')
    ax= volatility_series[:-10].plot.bar(color ="darkblue",ax=axes[1])
    return fig,ax
Dtitle= "24 hours top losers and winners"
fig,ax = top10_subplot(volatility.percent_change_24h,Dtitle)
# plt.show()

volatility7d = volatility.sort_values('percent_change_7d')
Wtitle = 'Weekly top losers and winners'
fig,ax = top10_subplot(volatility7d.percent_change_24h,Wtitle)
# plt.show()

# largest crypto
largcaps = cap.query('market_cap_usd> 10000000000')
print(largcaps.head())

#counting diff market caps usinf func

def capcount(query_string):
    return  cap.query(query_string).count().id
labels = ['biggish','micro','nano']
biggish = capcount("market_cap_usd > 3E+8")
micro = capcount("market_cap_usd >= 5E+7 & market_cap_usd < 3E+8")
nano =  capcount("market_cap_usd < 5E+7")
values = [biggish,micro,nano]
plt.bar(range(len(values)),values,tick_label=labels)
plt.show()