import numpy as np
import time
import math

def ransac(matches, c1, c2):
    coordOne = c1[:2]
    coordTwo = c2[:2]
    maxInliers = -math.inf
    t = 12.7                    #np.sqrt(447 ** 2 + 241 **2) / 40
    for i in range(10000):
        firstIdx = np.random.randint(0, len(matches))
        secondIdx = np.random.randint(0, len(matches))
        xone = coordOne[0][firstIdx]
        yone = coordOne[1][firstIdx]
        xonePrime = coordTwo[0][int(matches[firstIdx])]
        yonePrime = coordTwo[1][int(matches[firstIdx])]
        xtwo = coordOne[0][secondIdx]
        ytwo = coordOne[1][secondIdx]
        xtwoPrime = coordTwo[0][int(matches[secondIdx])]
        ytwoPrime = coordTwo[1][int(matches[secondIdx])]
        s = np.sqrt((xonePrime - xtwoPrime) ** 2 + (yonePrime - ytwoPrime) ** 2) / ( np.sqrt((xone - xtwo) ** 2 + (yone - ytwo) ** 2) + 0.00000000000001)
        tx = xonePrime - (s * xone)
        ty = yonePrime - (s * yone)
        inliers = []
        for j in range(len(matches)):
            xone = coordOne[0][j]
            yone = coordOne[1][j]
            xonePrime = coordTwo[0][int(matches[j])]
            yonePrime = coordTwo[1][int(matches[j])]
            euclid = (xone - ((xonePrime - tx) / (s + 0.00000000000001))) ** 2 + (yone - ((yonePrime - ty) / (s + 0.00000000000001))) ** 2
            if euclid < t:
                inliers.append(j)
        if len(inliers) > maxInliers:
            maxInliers = len(inliers)
            inliersArr = inliers.copy()
            transf = [tx, ty, s]
    print(len(inliersArr))
    print(transf)
    result = [inliersArr, transf]
    return result




