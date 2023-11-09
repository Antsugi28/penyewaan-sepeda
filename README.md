# My Dashboard Submission for Data Analyst Project (Dicoding) ✨

## Data Set Information
```
Data yang digunakan dalam projek ini yaitu data perhari (day.csv) yang mana memiliki beberapa kolom:
➜ instant: record index
➜ dteday : date
➜ season : season (1:springer, 2:summer, 3:fall, 4:winter)
➜ yr : year (0: 2011, 1:2012)
➜ mnth : month ( 1 to 12)
hr : hour (0 to 23)
➜ holiday : weather day is holiday or not (extracted from [Web Link])
➜ weekday : day of the week
➜ workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
➜ weathersit :
    1: Clear, Few clouds, Partly cloudy, Partly cloudy
    2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
➜ temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
➜ atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
➜ hum: Normalized humidity. The values are divided to 100 (max)
➜ windspeed: Normalized wind speed. The values are divided to 67 (max)
➜ casual: count of casual users
➜ registered: count of registered users
➜ cnt: count of total rental bikes including both casual and registered
```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas matplotlib seaborn jupyter streamlit
```

## Run steamlit app on local
```
streamlit run dashboard.py
```

## Run steamlit app on websitie
```
[Dashboard APP on streamlit website here](https://www.dicoding.com/academies/51/)
```