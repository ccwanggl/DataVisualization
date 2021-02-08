import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

def read_plot_with_pandas(filename):
    data = pd.read_csv(filename)

    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages = []
    popularity = []

    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

    languages.reverse()
    popularity.reverse()

    plt.barh(languages, popularity)
    plt.title("Most Popular Languages")
    # plt.ylabel('Programming Languages')
    plt.xlabel('Number Of People Who Use')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    read_plot_with_pandas('../data/data.csv')