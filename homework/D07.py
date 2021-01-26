import numpy as np

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
inverse_array = np.linalg.inv(array1)
new_array = inverse_array * array1
print(new_array)
#解答
#是，雖然算出來沒有完全等於[[1,0],[0,1]]，因為反矩陣計算浮點數的關係所以不會完全等於!!!
array1 = np.array([[10, 8], [3, 5]])
array1_inv = np.linalg.inv(array1)
print(np.dot(array1_inv,array1)) #dot():點積，也可用matmul()做矩陣程法/@也可當作矩陣乘法的運算子
print(np.matmul(array1_inv,array1))
print(array1_inv @ array1)
#2. 運用上列array計算特徵值、特徵向量?
eigenvalues, eigenvectors = np.linalg.eig(array1)
print("特徵值:",eigenvalues,"\n特徵向量：",eigenvectors)
#3. 運用上列array計算SVD?
u, s, v = np.linalg.svd(array1)
print("array U:",u,'\narray S:',s,'\narray V:',v)