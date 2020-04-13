from numpy import *


def pearson_similarity(v1, v2):
    v1_sum = sum(v1)/count_nonzero(v1)
    v2_sum = sum(v2)/count_nonzero(v2)
    for i in range(len(v1)):
        if v1[i] != 0:
            v1[i] = v1[i] - v1_sum
    for i in range(len(v2)):
        if v2[i] != 0:
            v2[i] = v2[i] - v2_sum
    sim = dot(v1,v2)/(linalg.norm(v1)*linalg.norm(v2))
    #print(v2)
    return sim