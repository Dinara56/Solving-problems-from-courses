from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator, TransformerMixin


CONSTANT = # константны, можно сюда писать паттерны - опционально

class YourClassNumber(BaseEstimator, TransformerMixin):
    def __init__(self, pattern ** kwargs):
        self.pattern = pattern
        super().__init__(**kwargs)

    def fit(self, X, y=None):
        return self

    def preprocessing(self, data: str):
        ###
        return #

    def transform(self, X, y=None):
        result = csr_matrix(X.apply(self.preprocessing)).T
        return result

    def get_feature_names(self):  # опционально
        return #
        
        
class YourClassText(BaseEstimator, TransformerMixin):

    def preprocessing(self, s):
        #
        return  #

    def to_desc(self, s):
        return self.preprocessing(s)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.apply(self.to_desc)