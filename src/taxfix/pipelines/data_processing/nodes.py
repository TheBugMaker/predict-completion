import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(data: pd.DataFrame):
    """Split the dataset into train and inference sets."""
    train, inference = train_test_split(data, test_size=0.3, random_state=42)
    return train, inference
