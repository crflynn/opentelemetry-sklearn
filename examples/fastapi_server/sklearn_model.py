from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

sklearn_model = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("normal", Normalizer()),
        ("class", RandomForestClassifier(n_estimators=10)),
    ]
)


sklearn_model.fit(X_train, y_train)
