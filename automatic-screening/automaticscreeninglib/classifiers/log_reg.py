from automaticscreeninglib.classifiers.base_clf import Base_Classifier

from sklearn.linear_model import LogisticRegression
import numpy as np



class Log_Reg_Classifier(Base_Classifier):

    def __init__(self, C = 0.001, random_state=101, n_jobs=1) -> None:
        super(Log_Reg_Classifier, self).__init__()
        self.C = C

        self._model = LogisticRegression(
            solver='liblinear',
            C=C,
            n_jobs=n_jobs,
            penalty='l1',
            random_state=random_state)
    
    def get_grid_space(self):
        param_grid = {
            'clf__C': np.logspace(-3,3,7),
            'clf__max_iter': [100, 500, 1000]
        }

    def fit(self):
        pass

    def predict(self):
        pass

