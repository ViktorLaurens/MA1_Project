import numpy as np
from numpy.linalg import norm
from matplotlib import pyplot as plt
from random import random
from tools import *


def SmoothPath(P, obstacles, smoothiters):
    m = P.shape[0]
    l = np.zeros(m)
    for k in range(1, m):
        l[k] = norm(P[k, :] - P[k - 1, :]) + l[k - 1]  # find cumulative straight-line distances

    for _ in range(smoothiters):
        s1 = np.random.random() * l[m - 1]
        s2 = np.random.random() * l[m - 1]
        if s2 < s1:
            s1, s2 = s2, s1

        i = np.searchsorted(l, s1) - 1
        j = np.searchsorted(l, s2) - 1

        if j <= i:
            continue

        t1 = (s1 - l[i]) / (l[i + 1] - l[i])
        gamma1 = (1 - t1) * P[i, :] + t1 * P[i + 1, :]
        t2 = (s2 - l[j]) / (l[j + 1] - l[j])
        gamma2 = (1 - t2) * P[j, :] + t2 * P[j + 1, :]

        if not isCollisionFreeEdge(obstacles, gamma1, gamma2):
            continue

        P = np.vstack([P[:(i + 1), :], gamma1, gamma2, P[(j + 1):m, :]])
        m = P.shape[0]
        l = np.zeros(m)
        l[1:] = norm(P[1:, :] - P[:-1, :], axis=1)
        l = np.cumsum(l)

    P_smooth = P
    return P_smooth