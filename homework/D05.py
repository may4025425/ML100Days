import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])
#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?

#各科成績平均
print(np.mean(english_score))
print(np.nanmean(math_score))
print(np.mean(chinese_score))
#最大值
print(np.max(english_score))
print(np.nanmax(math_score))
print(np.max(chinese_score))
#最小值
print(np.min(english_score))
print(np.nanmin(math_score))
print(np.min(chinese_score))
#標準差
print(np.std(english_score))
print(np.nanstd(math_score))
print(np.std(chinese_score))
#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score = np.array([60,85,60,68,55,60])
#成績平均
print(np.mean(math_score))
#最大值
print(np.max(math_score))
#最小值
print(np.min(math_score))
#標準差
print(np.std(math_score))

#解答
math_score[4] = 55
print("補考數學分數後 ","平均",np.nanmean(math_score),"最大值",np.nanmax(math_score),"最小值",np.nanmin(math_score),"標準差",np.nanstd(math_score))
#3. 用補考後資料找出與國文成績相關係數最高的學科?

#correlate():是計算兩個一維序列的互相關，並非計算相關係數!
en_ch_corr = np.correlate(english_score,chinese_score)
ma_ch_corr = np.correlate(math_score,chinese_score)
if(en_ch_corr > ma_ch_corr):
    print("英文成績與國文成績的相關係數最高")
else:
    print("數學成績與國文成績的相關係數最高")
#解答
ch_ma_corr = np.corrcoef(chinese_score,math_score)
ch_en_corr = np.corrcoef(chinese_score,english_score)
print("國文與數學相關係數",ch_ma_corr)
print("國文與英文相關係數",ch_en_corr)
if(str(ch_en_corr > ma_ch_corr)):
    print("英文成績與國文成績的相關係數最高")
else:
    print("數學成績與國文成績的相關係數最高")
