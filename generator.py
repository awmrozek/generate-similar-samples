import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def generate_dataset(seed, num_samples, p, med1, med2, std_dev1, std_dev2):
    np.random.seed(seed)
    df = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"],
                                      num_samples, p)
        "Value1": np.random.normal(med1, std_dev1, num_samples)
        "Value2": np.random.normal(med2, std_dev2, num_samples)
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

def generate_similar_dataset(num_samples=750):
    """Generate a new dataset with similar characteristics but different parameters"""
    np.random.seed(123)  # Different seed for different random numbers

    # Similar probabilities but slightly different
    # Original: [0.2, 0.4, 0.2, 0.1, 0.1]
    # New: [0.25, 0.35, 0.2, 0.12, 0.08]
    new_df = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"], 
                                    num_samples, p=[0.25, 0.35, 0.2, 0.12, 0.08]),
        "Value1": np.random.normal(10.5, 2.2, num_samples),  # Center: 10.5, spread: 2.2
        "Value2": np.random.normal(19, 5.5, num_samples),    # Center: 19, spread: 5.5
    })
    return new_df

if __name__ == "__main__":
    # Generate datasets
    original_df = generate_original_dataset()
    new_df = generate_similar_dataset()

    # Save both datasets
    original_df.to_csv("original_dataset.csv", sep=";", index=False)
    new_df.to_csv("new_similar_dataset.csv", sep=";", index=False)

