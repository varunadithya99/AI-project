from pandas import *
from numpy import *


similarity_matrix = read_csv("sim.csv")
similarity_matrix = array(similarity_matrix)
similarity_matrix = delete(similarity_matrix, 0, 1)

for i in range(100):
    count = 0
    for j in range(100):
        if 0.1<similarity_matrix[i][j]<1:
            count += 1
    print(count)
'''from training_data import training_data
from pearson import pearson_similarity
from numpy import *
#from pandas import *


training_data_copy = training_data[:, :1000].copy()
print(training_data_copy.shape)
test_data = training_data_copy[100:, 950:].copy()
training_data_copy[100:, 950:] = 0
print(test_data.shape)
training_data_copy = training_data_copy.astype('float')
similarity_matrix = zeros((1000, 1000), dtype=float)

for i in range(1000):
    v1 = training_data_copy[i, ].copy()
    for j in range(1000):
        v2 = training_data_copy[:, j].copy()
        similarity_matrix[i][j] = pearson_similarity(v1, v2)'''