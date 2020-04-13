#from similarity import similarity_matrix
from training_data import training_data
from efficiency_check import rms
from sklearn.metrics.pairwise import pairwise_distances
from pandas import *
from numpy import *

training_data_copy = training_data[:100, :100].copy()
training_data_copy2 = training_data[:100, :100].copy()
test_data = training_data_copy[70:, 70:].copy()
training_data_copy[70:, 70:] = 0
predicted_items = []
similarity_matrix = read_csv("sim.csv")
similarity_matrix = array(similarity_matrix)
similarity_matrix = delete(similarity_matrix, 0, 1)
f = open("Course-List.txt", 'r')
courses = [i.rstrip() for i in f.readlines()]
f.close()
#item_similarity_matrix = pairwise_distances(training_data_copy,metric='cosine')
#user_similarity_matrix = pairwise_distances(training_data_copy,metric='cosine')
total_avg = sum(sum(training_data_copy[:, :])) / count_nonzero(training_data_copy)

def baseline_estimate(user_id, movie_id):
    u_sum = sum(training_data_copy[:, user_id])
    m_sum = sum(training_data_copy[movie_id, :])
    u_count = count_nonzero(training_data_copy[:, user_id])
    m_count = count_nonzero(training_data_copy[movie_id, :])
    user_deviation = u_sum/u_count - total_avg
    movie_deviation = m_sum/m_count - total_avg
    return total_avg + user_deviation + movie_deviation



def similar(movie_id):
    similar_movie = {}
    for i in range(100):
        if 0.6 < similarity_matrix[movie_id][i] < 1:
            similar_movie[i] = similarity_matrix[movie_id][i]
    similar_movie = {k: v for k, v in sorted(similar_movie.items(), key=lambda item: item[1], reverse=True)}
    if len(similar_movie) > 10:
        sim_matrix = {}
        x = 0
        for i in similar_movie:
            if x == 10:
                break
            sim_matrix[i] = similar_movie[i]
            x += 1
        return sim_matrix
    else:
        return similar_movie



def rating(user_id, movie_id):
    item_similarity = similar(movie_id)
    dn_sum = sum(list(item_similarity.values()))

    if dn_sum != 0:
        nu_sum = 0.0
        for i in item_similarity:
            b = baseline_estimate(user_id, i)
            nu_sum += item_similarity[i]*(training_data[i][user_id] - b)
        return nu_sum/dn_sum
    else:
        return 0




def old_user():
    rows, cols = training_data_copy.shape
    for user_id in range(cols):
        for i in range(rows):
            if training_data_copy[i][user_id] == 0:
                b = baseline_estimate(user_id, i)
                #print("i=%d  b=%f" % (i, b))
                training_data_copy[i][user_id] = b + rating(user_id, i)


if __name__ == "__main__":
    print(1)
    old_user()
    print(training_data_copy[70:, 70:])
    print(test_data)
    print(rms(training_data_copy[70:, 70:], test_data))
    print("rms")
    x = test_data - training_data_copy[70:, 70:]
    sim_matrix = similarity_matrix[70:, 70:]
    DataFrame(x/sim_matrix).to_csv("test-train.csv")
#print(count_nonzero(training_data)/training_data.size)
