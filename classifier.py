from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pickle

""" (list, list) -> KNeighborsClassifier
Returns a trained KNN model on the list of floats (similarities) and their labels (strings). 
"""
def train_model(similarities, labels):
    label_encoder = preprocessing.LabelEncoder() # not used if numeric_labels is not used
    
    #may not be necessary, only if following is given as a non-number
    # numeric_labels = label_encoder.fit_transform(labels)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(similarities, labels)
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

model = train_model([[1.1, 5.2]], [[1, 0]]) # sample values for now

# Save model to disk
pickle.dump(model, open('model.pkl','wb'))