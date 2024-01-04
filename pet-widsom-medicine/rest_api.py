#%%
!pip install alpha_vantage
#%%
from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import io
import config
api_key = config.API_KEY
stock_name = 'AAPL'
# %%
ts1 = TimeSeries(key = api_key)
# %%
ts1.get_monthly("AAPL")
# %%
# get weekly data for apple stock
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey='+str(api_key)
r = requests.get(url)
data = r.json()
print(data)

# %%
# put data into pandas dataframe
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey='+str(api_key)+'&datatype=csv'
r= requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode("utf-8")))

print(data)
# %%
apple1 , meta_data = ts1.get_intraday("AAPL")

# %%
df_apple1 = pd.DataFrame(apple1).transpose().reset_index()

# %%
