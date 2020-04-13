from pandas import *
from numpy import *



training_data = read_csv("temp.csv")
training_data = array(training_data, dtype=float)
training_data = delete(training_data, 0, 1)
training_data = training_data
#print(training_data.shape)
