'''
@Author: Komoriii
@email: c2VuZXZhbkBmb3htYWlsLmNvbQ==
'''
from numpy import *

# calculate Euclidean distance
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

# create cluster centroids
def randCent(dataset, k):
    n = shape(dataset)[1]
    centroids = mat(zeros(k,n))
    for j in range(n):
        minJ = min(dataset[:, j])
        rangeJ = float(max(dataset[:, j] - minJ))
        centroids[:, j] = minJ + rangeJ * random.rand(k,1)
    return centroids

def kMeans(dataset, k):
    m = shape(dataset)[0]
    cluster_assess = mat(zeros((m,2))
    centroids = randCent(dataset, k)
    cluster_change = True
    while cluster_change:
        cluster_change = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distEclud(centroids[j, :], dataset[i, :])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if cluster_assess[i, 0] != minIndex:
                cluster_change = True
            cluster_assess[i, :] = minIndex, minDist**2
    print(centroids)
    for cent in range(k):
        pts_in_clust = dataset[nonzero(cluster_assess[:, 0].A==cent)[0]]
        centroids[cent, :] = mean(pts_in_clust, axis=0)
    return centroids, cluster_assess