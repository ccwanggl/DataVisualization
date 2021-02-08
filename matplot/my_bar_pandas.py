import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

with open('../data/data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

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
