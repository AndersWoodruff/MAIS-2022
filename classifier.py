from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

""" (list, list) -> KNeighborsClassifier
Returns a trained KNN model on the list of floats (similarities) and their labels (strings). 
"""
def train_model(similarities, labels):
    label_encoder = preprocessing.LabelEncoder()
    
    #may not be necessary, only if following is given as a non-number
    numeric_labels = label_encoder.fit_transform(labels)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(similarities, numeric_labels)
    return model

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
