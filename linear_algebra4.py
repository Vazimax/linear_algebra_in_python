import numpy as np

M = np.round(5*np.random.randn(2,2))
print(M)
print('')
MT = M.T
print(MT)
print('')
MTT = MT.T
print(MTT)

M1 = np.random.randn(4,5)
M2 = np.random.randn(4,5)
print(np.matmul(M1,M2.T))
print('')
print(M1@M2.T)