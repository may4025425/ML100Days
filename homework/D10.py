import pandas as pd

#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
stock1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock2 = pd.read_csv('STOCK_DAY_0050_202010.csv')

#串聯
stock_data = pd.concat([stock1,stock2])

#找出open小於close的資料
stock_data[stock_data.open<stock_data.close]
