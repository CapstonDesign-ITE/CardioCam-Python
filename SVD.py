# SVD module for CardioCam

import numpy as np

A = [[i**2,i,1] for i in range(1930,2020,10)]

# numpy Array 로 변환
matA = np.array(A).astype(np.float64)

# svd 함수 사용하여 3개 반환값 저장
U, s, V = np.linalg.svd(matA, full_matrices=True)

# s = matA의 eigenvalue list
# svd 이용한 근사 결과를 원본가 비교위해 s를 유사대각행렬로 변환
S = np.zeros(matA.shape)
for i in range(len(s)):
    S[i][i] = s[i]

# 근사한 결과 계산
appA = np.dot(U, np.dot(S,V))
print(matA-appA)
