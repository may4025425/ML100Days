import numpy as np

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
inverse_array = np.linalg.inv(array1)
new_array = inverse_array * array1
print(new_array)
#2. 運用上列array計算特徵值、特徵向量?
eigenvalues, eigenvectors = np.linalg.eig(array1)
print("特徵值:",eigenvalues,"\n特徵向量：",eigenvectors)
#3. 運用上列array計算SVD?
u, s, v = np.linalg.svd(array1)
print("array U:",u,'\narray S:',s,'\narray V:',v)