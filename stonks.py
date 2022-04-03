import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

#----- Gathering Financial Data -----#
# Setting API key
quandl.ApiConfig.api_key = 'INSERT API KEY HERE'

# Getting data frame (most accurate with tickers that grow ~linearly)
df = quandl.get('WIKI/AMZN')
df = df[['Adj. Close']]

# Plotting Adj. Close prices from 1997-2018
df['Adj. Close'].plot(figsize=(15,6), color='g')
plt.legend(loc='upper left')

#----- Processing Train and Test Data -----#
# Specifying forecast to be 30 days
forecast = 30

# Shifting y data 30 units into the future for training
df['Prediction'] = df[['Adj. Close']].shift(-forecast)

# Creating data sets
x = np.array(df.drop(['Prediction'], 1))

# Standardizing data ( setting mean and std. dev to 0, 1)
x = preprocessing.scale(x)

# splitting x into the last 30 days, and all prior days
x_forecast = x[-forecast:]
x = x[:-forecast]

# Splicing out the last 30 days of y
y = np.array(df['Prediction'])
y = y[:-forecast]

#----- Applying Linear Regression -----#
# Creating train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Creating linear regression model
classifier = LinearRegression()
classifier.fit(x_train, y_train)

# Scoring data
confidence = classifier.score(x_test, y_test)

# Predicting the next 30 days
forecast_predicted = classifier.predict(x_forecast)

#-----Visualizing Predicted Results-----#
# Creating a dates array for ther 30 days to be predicted
dates = pd.date_range(start="2018-03-28", end="2018-04-26")

# Plotting real and predicted data
plt.plot(dates, forecast_predicted, color='b')
df['Adj. Close'].plot(color='g')

# Setting an x limit to better view the results
plt.xlim(xmin=datetime.date(2017,4,26))
plt.xlim(xmax=datetime.date(2018,5,1))

# Visualizing Prediction
plt.show()