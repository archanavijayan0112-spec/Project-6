
from sklearn.ensemble import IsolationForest
def build_model():
    return IsolationForest(contamination=0.1)
