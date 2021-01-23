import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
#1.有多少學生英文成績比數學成績高?
print(str(english_score > math_score).count("False",0))
#解答1
en_greater_ma = np.greater(english_score,math_score)
print(en_greater_ma)
#Use sum() to count True elements in a NumPy array
print(np.sum(en_greater_ma)) #運用觀念:True is equal to 1
#Use count_nonzero() to count True elements in NumPy array
count = np.count_nonzero(en_greater_ma)
print(count)
#2.是否全班同學最高分都是國文?
if(str(np.greater(chinese_score,english_score)).find("True",0) and str(np.greater(chinese_score,math_score)).find("True",0)):
   print("全班同學最高分都是國文")
#解答2
ch_greater_ma = np.greater(chinese_score,math_score)
ch_greater_en = np.greater(chinese_score,english_score)
print(np.logical_and(ch_greater_ma,ch_greater_en))
#運用觀念：any()函數用於判定給定的可疊代參數是否全部為False,是的話返回False,如果其中有一個是True，則返回True
print(np.logical_and(ch_greater_ma,ch_greater_en).any())