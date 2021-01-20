import numpy as np

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a = np.arange(0,21,1)
print(a)
#2.呈上題，將以上數列取出偶數。
for i in a:
    if i%2 == 0:
        print("數列中的偶數： "+str(i))
#3.呈1題，將數列取出3的倍數。
for i in a:
    if i%3 == 0:
        print("數列中3的倍數： "+str(i))