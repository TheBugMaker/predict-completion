import logging

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series, params: dict) -> RandomForestClassifier:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Column transformer for preprocessing
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, params[ "numerical_features" ]),
        ('cat', categorical_transformer, params[ "categorical_features"])
    ])

    # Creating pipeline with RandomForestClassifier
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    pipeline.fit(X_train, y_train)

    return pipeline


def evaluate_model(
    model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, float]:
    """Evaluates model.

    Args:
        regressor: Trained model.
        X_test: Testing data of  features.
        y_test: Testing data for .
    """
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    logging.info(f"Model accuracy: {accuracy}")
    recall = recall_score(y_test, y_pred)
    logging.info(f"Model recall: {recall}")
    precision = precision_score(y_test, y_pred)
    logging.info(f"Model precision: {precision}")
    f1 = f1_score(y_test, y_pred)
    logging.info(f"Model f1: {f1}")

    return {"accuracy": accuracy, "recall": recall, "precision": precision, "f1": f1}

def run_inference(model: Pipeline, data: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """Runs inference using the trained model.

    Args:
        model: Trained model.
        data: Data to run inference on.

    Returns:
        Predictions from the model.
    """
    data["pred"] =  model.predict(data)
    return data
