# stock_price_predictor
A linear regression model that predicts stock prices 30 days into the future.

# Description
Uses the quandl API to scrape stock price data (up until April 11, 2018) for use as training and test sets.
A linear regression model is trained (using an 80, 20 training test split) on the resulting training and test sets.
The results are visualized using matplotlib with the predicited stock prices plotted (blue) over the historic stock prices (green).

# Models
### Scraped Stock Adj. Close Data
![Screen Shot 2022-04-03 at 1 38 54 PM](https://user-images.githubusercontent.com/89366190/161444176-5bb3fc77-ec74-48f8-8723-98d9e15c60c6.png)
### Plot of Scraped Stock Adj. Close Data
![Screen Shot 2022-04-03 at 1 38 08 PM](https://user-images.githubusercontent.com/89366190/161444181-dd858f67-f363-454a-a93e-1c7ad0cbee86.png)
### Stock Adj. Close Data + Prediction Training Set (y-data offset 30 days into the future)
![Screen Shot 2022-04-03 at 1 38 54 PM](https://user-images.githubusercontent.com/89366190/161444225-ffb095f5-b7f6-4ec1-bf6c-ab1b2302371e.png)
### List of Predicted Stock Prices 30 Days into the Future
![Screen Shot 2022-04-03 at 1 38 13 PM](https://user-images.githubusercontent.com/89366190/161444206-c7308518-0854-4b0a-82fa-1da25f66a843.png)
### Plot of Historic Stock Prices + Predicted Stock Prices
<img width="1186" alt="Screen Shot 2022-04-03 at 1 36 19 PM" src="https://user-images.githubusercontent.com/89366190/161444212-436456f9-50e7-4a94-bf63-dd6bb0449b2a.png">
