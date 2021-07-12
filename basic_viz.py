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

# bars
fig, ax = plt.subplots()
ax.bar(ozone, wind) # barh() horizontal
ax.set_xlabel('ozone')
ax.set_ylabel('wind')
plt.show()

# scatterplot
slope, intercept, r, *__ = scipy.stats.linregress(solar, ozone)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

fig, ax = plt.subplots()
ax.plot(solar, ozone, linewidth=0, marker='s', label='Data points')
ax.plot(solar, intercept + slope * solar, label=line)
ax.set_xlabel('solar')
ax.set_ylabel('ozone')
ax.legend(facecolor='white')
plt.show()

