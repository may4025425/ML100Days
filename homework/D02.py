import numpy as np

#1將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
array1 = array1.reshape((5,6),order="F")
print(array1)

#2.呈上題的array，找出被6除餘1的數的索引

#如果元素值為被6除餘1的數的話就用 "Y" 來替代，反之則是 "N"
print(np.where(array1 % 6 == 1,"Y","N"))



