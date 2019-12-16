import preprocessor
import knn

data = preprocessor.Data("lyrics.csv", 5,4)

data.extract()
model = knn.KNN(data.classified)
accuracy= model.evaluate(10,5)
print(accuracy)