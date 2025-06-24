import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def generate_dataset(seed, num_samples, p, avg1, avg2, std_dev1, std_dev2):
    print(f"Generate dataset: {p}")
    np.random.seed(seed)
    df = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"],
                                      num_samples, p=p),
        "Value1": np.random.normal(avg1, std_dev1, num_samples),
        "Value2": np.random.normal(avg2, std_dev2, num_samples)})
    return df

def generate_original_dataset():
    """Generate the original dataset as specified"""
    np.random.seed(42)
    num_samples = 500
    df = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"], 
                                    num_samples, p=[0.2, 0.4, 0.2, 0.1, 0.1]),
        "Value1": np.random.normal(10, 2, num_samples),
        "Value2": np.random.normal(20, 6, num_samples),
    })
    return df


if __name__ == "__main__":
    # Generate datasets
    original_df = generate_original_dataset()
    original_df.to_csv("original_dataset.csv", sep=";", index=False)

