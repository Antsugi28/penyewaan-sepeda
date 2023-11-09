import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

bike_df = pd.read_csv("https://raw.githubusercontent.com/Antsugi28/penyewaan-sepeda/main/dashboard/main_day.csv")

bike_df.rename(columns={'instant':'rec_id','dteday':'datetime','yr':'year','mnth':'month','weathersit':'weather_condition','hum':'humidity','cnt':'total_count'},inplace=True)

st.title('Dashboard Penyewaan Sepeda')

st.subheader('penyewaan sepeda perbulan berdasarkan musim')
fig,ax=plt.subplots(figsize=(16,8))
sns.set_style('darkgrid')

sns.barplot(
    x='month',
    y='total_count',
    data=bike_df[['month','total_count','season']],
    hue='season',
     ax=ax
)
ax.set_title('penyewaan sepeda perbulan berdasarkan musim')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write(
        """Dari plot di atas, kita dapat mengamati bahwa jumlah penyewaan sepeda meningkat 
        pada musim semi dan musim panas dan kemudian jumlah penyewaan sepeda turun pada musim 
        gugur dan musim dingin. \n
    1: spring, 
    2: summer, 
    3: fall, 
    4: winter
        """
    )

st.subheader('kondisi cuaca saat penyewaan sepeda dalam jumlah total bulanan')
fig,ax=plt.subplots(figsize=(16,8))
sns.set_style('darkgrid')

sns.barplot(
   x='weather_condition',
   y='total_count',
   data=bike_df[['month','total_count','weather_condition']],
   ax=ax
)
ax.set_title('kondisi cuaca saat penyewaan sepeda dalam jumlah total bulanan')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write(
        """Dari diagram batang di atas, kita dapat mengamati bahwa pada saat cuaca cerah dan 
        berawan sebagian, jumlah penyewaan sepeda paling tinggi dan tertinggi kedua pada saat 
        cuaca berawan kabut dan diikuti oleh tertinggi ketiga pada saat cuaca salju ringan dan 
        hujan ringan.\n
    1: Clear, Few clouds, Partly cloudy, Partly cloudy
    2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
        """
    )
