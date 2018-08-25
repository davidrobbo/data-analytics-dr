from sklearn.base import BaseEstimator, TransformerMixin

class DummyTransform(BaseEstimator, TransformerMixin):
    def __init__(self, add_boolean_field = True):
        self.add_boolean_field = add_boolean_field
    def fit(self, X, y = None):
        return self
    def transform(self, X, y = None):
        if (self.add_boolean_field):
            print(True)
        return None