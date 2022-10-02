from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pickle

""" (list, list) -> NoneType
Pickles a trained KNN model on the list of similarities (floats) and their labels (ints) into model.pkl. 
"""
def train_model(similarities, labels):
    model = KNeighborsClassifier(n_neighbors=2) # should be 5, but is 2 because data set is small.
    model.fit(similarities, labels)

    with open("model.pkl", "wb") as model_pickle:
        pickle.dump(model, model_pickle)

""" (KNeighborsClassifier, list, list) -> float
Returns the accuracy of the model's predictions for the given float similarities and strings labels.
"""
def test_accuracy(model, similarities, labels):
    predictions = model.predict(similarities)
    return metrics.accuracy_score(labels, predictions)

""" (KNeighborsClassifier, float) -> int 
Returns the integer representation of whether or not the pair is likely to follow each other.
"""  
def make_prediction(model, similarity):
    return model.predict([similarity])
