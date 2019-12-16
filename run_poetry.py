import preprocessor
import knn
data = preprocessor.Data("all.csv", 1,3)

data.extract()
model = knn.KNN(data.classified)
accuracy= model.evaluate(10,5)
print(accuracy)