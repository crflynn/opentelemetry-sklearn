import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import Normalizer, StandardScaler

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)


def pipeline():
    """A dummy model that has a bunch of components that we can test."""
    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("normal", Normalizer()),
            (
                "union",
                FeatureUnion(
                    [
                        ("pca", PCA(n_components=1)),
                        ("svd", TruncatedSVD(n_components=2)),
                    ],
                    n_jobs=1,  # parallelized components won't generate spans
                ),
            ),
            ("class", RandomForestClassifier(n_estimators=10)),
        ]
    )
    model.fit(X_train, y_train)
    return model


def random_input():
    """A random record from the feature set."""
    rows = X.shape[0]
    random_row = np.random.choice(rows, size=1)
    return X[random_row, :]
