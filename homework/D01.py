import numpy as np

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a = np.arange(0,21,1)
print(a)

#2.呈上題，將以上數列取出偶數。

#第一種
for i in a:
    if i%2 == 0:
        print("數列中的偶數： "+str(i))
#第二種
even_array = a[::2]
print(even_array)

#3.呈1題，將數列取出3的倍數。

#第一種
for i in a:
    if i%3 == 0:
        print("數列中3的倍數： "+str(i))
#第二種
array_3 = a[3::3]
print(array_3)
#熟悉array用法
import numpy as np
x=np.array([[1,2,3],[5,6,7],[7,8,9]])
print(x[:,::5])