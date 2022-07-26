"""
The PLS algorithm
"""

import numpy as np



# def PLS00(XX, YY):
#     yyn = None
#     xX = None
#     for foo in range(YY.shape[0]):
#         for k in range(yy.shape[0]):
#             if foo != k:
#                 if yyn == None:
#                     yyn = 

def PLS01(XX, YY):
    yyn = YY
    for columns in range(YY.shape[0]-1):
        yyn = np.append(yyn, YY, axis=1)
    for ones in range(YY.shape[0]):
        yyn[ones][ones] = 1

    xX = XX[:, :, np.newaxis]
    tempxX = xX
    for z in range(YY.shape[0]-1):
        xX = np.append(xX, tempxX, axis=2)
    # xX = xX.transpose(1, 0, 2)
    # for x in range(YY.shape[0]):
    #     xX[x][x][:] = 0
    print(xX[0][0][0])
    print(xX[0][0][1])
    print(xX[0][0][2])
x = np.array([
    [1, 2, 3],
    [4, 5, 4],
    [7, 8, 5]
])

y = np.array([
    [10],
    [11],
    [12]
])

PLS01(x, y)