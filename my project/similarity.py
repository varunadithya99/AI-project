from training_data import training_data
from pearson import pearson_similarity
from numpy import *
from pandas import *


training_data_copy = training_data[:100, :100].copy()
print(training_data_copy.shape)
test_data = training_data_copy[70:, 70:].copy()
training_data_copy[70:, 70:] = 0
print(test_data.shape)
training_data_copy = training_data_copy.astype('float')
similarity_matrix = zeros((100, 100), dtype=float)

for i in range(100):
    v1 = training_data_copy[i, :].copy()
    for j in range(100):
        v2 = training_data_copy[j, :].copy()
        similarity_matrix[i][j] = pearson_similarity(v1, v2)



similarity_matrix = DataFrame(similarity_matrix)
similarity_matrix.to_csv("sim.csv")
print(similarity_matrix)