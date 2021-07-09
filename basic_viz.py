import io
import numpy as np
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import requests

download_url = "https://raw.githubusercontent.com/rpalloni/dataset/master/airquality.csv"
response = requests.get(download_url)
data = pd.read_csv(io.BytesIO(response.content), dtype={'Ozone': float,'SolarRay':float, 'Wind':float, 'Temp':float, 'Month':float, 'Day':float})
data.head()
data.describe()

print(plt.style.available)
plt.style.use('ggplot')

data = data.dropna() # remove nan

ozone = data['Ozone']
solar = data['SolarRay']
wind = data['Wind']

# boxplot
fig, ax = plt.subplots()
ax.boxplot((ozone, solar, wind), vert=False, showmeans=True, meanline=True,
           labels=('Ozone', 'SolarRay', 'Wind'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

# histogram
fig, ax = plt.subplots()
ax.hist(ozone, bins=20, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

fig, ax = plt.subplots()
ax.hist(ozone, bins=20, cumulative=True)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()
