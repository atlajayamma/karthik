from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris # import the load_iris function
from sklearn.linear_model import LogisticRegression # import the LogisticRegression class

# Load Iris dataset
iris = load_iris() # load the iris dataset and assign it to the variable iris

# Define leave-one-out cross-validation object
loo = LeaveOneOut()
# Train logistic regression model using leave-one-out cross-validation
scores = []
for train_index, test_index in loo.split(iris.data):
    x_train, x_test = iris.data[train_index], iris.data[test_index]
    y_train, y_test = iris.target[train_index], iris.target[test_index]
    clf = LogisticRegression().fit(x_train, y_train)
    y_pred = clf.predict(x_test) # this and the line below need to be indented to be inside the for loop
    scores.append(accuracy_score(y_test, y_pred))
# Compute average accuracy across all samples
score = sum(scores) / len(scores) # changed score_a to score
print(f"Accuracy: {score:.2f}")