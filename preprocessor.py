import csv
import string
from nltk.stem import *
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle
class Data():
	def __init__ (self, file, data_row, feature_row):
		self.file = file
		self.data_row = data_row
		self.feature_row = feature_row
		self.classified = {}
	def extract(self):
		with open(self.file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			lable_list = []
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					pass
				else:
					lable_list.append(row[self.feature_row])
				line_count += 1
			lable_list = set(lable_list)
			lable_list = list(lable_list)
			data_lables = lable_list
			print(data_lables)
		with open(self.file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				binary = -1
				counter_for_lables = 0
				#print("got here")
				#print(len(data_lables))
				for item in data_lables:
					#print(row[self.feature_row])
					#print(item)
					if row[self.feature_row] == item:
						#print("match")
						binary = counter_for_lables
					counter_for_lables += 1
				exclude = set(string.punctuation)
				removed = ''.join(ch for ch in row[self.data_row] if ch not in exclude)
				removed = removed.lower()
				removed = removed.replace("\n\n", " ")
				removed = removed.replace("\n", " ")
				removed = ' '.join(removed.split())
				stemmer = PorterStemmer()
				split = removed.split(" ")
				stemmed = [stemmer.stem(item) for item in split]
				removed = ' '.join(stemmed)
				if len(removed) >= 45 and binary != -1:
					self.classified[removed] = binary
	'''def vectorize(self):
		new_dict = {}
		vectorizer = CountVectorizer()
		words = []
		for item in self.classified:
			words.append(item)
		print("making")
		vectorizer.fit(words)
		print("done making")
		counter = 0
		for item in self.classified:
			print(counter, end = " ")
			print("out of ", end = " ")
			print(len(self.classified))
			counter += 1
			new_dict[tuple(list(vectorizer.transform([item]).toarray().flatten()))] = self.classified[item]
		self.classified = new_dict

data = Data("short_lyrics.csv", 5,4)
data.extract()
data.vectorize()
result = data.classified
print(result)
#for item in result:
#	print(np.sum(np.array(list(item))))

'''