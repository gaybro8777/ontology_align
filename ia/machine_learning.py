import autosklearn.classification
from sklearn.model_selection import train_test_split

class learn:
    def __init__(self):
        self.cls = autosklearn.classification.AutoSklearnClassifier()

    def test_split(self, array_test_x, array_test_y):
        X_train, X_test, y_train, y_test = train_test_split(
            array_test_x, array_test_y, random_state=1)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def train_ia(self):
        self.cls.fit(self.X_train, self.y_train)

    def predict_test(self):
        self.cls.predict(self.X_test)
        self.cls.predict(self.y_test)

    def predict(self, element):
        return self.cls.predict(element)