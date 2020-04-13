from numpy import *
from pearson import pearson_similarity
from scipy.stats import pearsonr
rating = array([[1,0,3,0,0,5,0,0,5,0,4,0], [0,0,5,4,0,0,4,0,0,2,1,3], [2,4,0,1,2,0,3,0,4,3,5,0], [0,2,4,0,5,0,0,4,0,0,2,0], [0,0,4,3,4,2,0,0,0,0,2,5], [1,0,3,0,3,0,0,2,0,0,4,0]], dtype=float)
rating_copy = rating.copy()
similarity = zeros((6,6),dtype=float)

for i in range(6):
    v1 = rating[i, :]
    for j in range(6):
        v2 = rating[j,:]
        similarity[i][j] = pearson_similarity(v1, v2)
print(similarity)

for i in similarity:
    for j in i:
        if 0.5 < j < 0.9:
            print(j)
n_sim = {}

for i in range(6):
    if 1 > similarity[0][i] > 0.4:
        n_sim[i] = similarity[0][i]
#print(n_sim)
for i in n_sim:
    rating_copy[0][4] += n_sim[i]*rating_copy[i][4]
rating_copy[0][4] /= (n_sim[2]+n_sim[5])
print(rating_copy[0][4])