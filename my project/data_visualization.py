from matplotlib import pyplot as plt
import seaborn as sns


def plot(data):
    sns.distplot(data, kde=False)
    plt.show()

