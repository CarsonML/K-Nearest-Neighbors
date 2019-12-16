# K-Nearest-Neighbors
Use of K Nearest Neighbors algorithm to classify the genre of poetry and lyrics.

# Processing
The preprocessing.py file processes the raw data, reading the csv's and stemming the words, removing punctuation, and removing/reformatting bad data. The KNN.py file contains the KNN class used. It vectorizes the lyric/poetry data by using Scikitlearn Count Vectorizer.

# Classification
The run_lyrics.py and run_poetry.py classify the lyrics and poetry respectivley. They use a K Nearest Neigbors algorithm, that is taking the most common classification among the k points nearest to a given point, in order to classify a given lyric/poem. The overall accuracy result is an average of accuracy on several different folds.

# Data
The lyrics.csv and all.csv file hold the lyrics and poetry data respetively. The data is somewhat dirty, hence the need for preprocessing.py
