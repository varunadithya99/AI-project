from training_data import training_data

normalized_matrix = training_data.copy()

for i in range(150):
    avg = sum(normalized_matrix[:, i])/4500
    normalized_matrix[:, i] -= avg

