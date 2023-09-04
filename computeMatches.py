import numpy as np
import math

def computeMatches(f1, f2):
    matches = np.zeros((f1.shape[1], ))
    print(matches.shape)
    for i in range(f1.shape[1]):
        minDist = math.inf
        minIdx = 0
        for j in range(f2.shape[1]):
            sumSquared = np.sum((f1[:,i] - f2[:, j]) ** 2)
            #print(sumSquared)
            if sumSquared < minDist:
                minDist = sumSquared
                minIdx = j
        matches[i] = minIdx
    return matches
