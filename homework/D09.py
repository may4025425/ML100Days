import pandas as pd

#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
bosto_data = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
bosto_data.to_excel('my_boston.xlsx')
print(bosto_data)
