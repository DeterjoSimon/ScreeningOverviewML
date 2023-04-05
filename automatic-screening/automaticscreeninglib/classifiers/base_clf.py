from automaticscreeninglib.base_model import Base_Model

class Base_Classifier(Base_Model):

    def __init__(self) -> None:
        self._model = None

    def fit(self, X, y):
        return self._model.fit(X, y)
    
    def predict(self, X):
        return self._model.predict(X)
    
    def eval(self, df):
        return self._model.eval(df)
    
    def get_grid_space(self):
        return {}, {}