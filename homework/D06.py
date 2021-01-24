import np as np
import numpy as np

#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
with open('multi_array.npz','wb') as f:
    np.savez(f,a=array1,b=array2)

a = np.load('multi_array.npz')
print(a['a'])
print(a['b'])
#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
with open('new_multi_array.npz','wb') as f:
    np.savez(f,a=array1,b=array2,c=np.array(range(10)))
b = np.load('new_multi_array.npz')
print(b['a'])
print(b['b'])
print(b['c'])
