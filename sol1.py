import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from generator import generate_original_dataset
from generator import generate_dataset
from similarity1 import simple_similarity_check
from similarity2 import verify_similarity

def get_distribution_params(data, column_name):
    column_data = data[column_name]
    mean = np.mean(column_data)
    std_deviation = np.std(column_data, ddof=1)
    variance = np.var(column_data, ddof=1)
    return {'mean': mean, 'std_deviation': std_deviation, 'variance': variance}

if __name__ == "__main__":
    # Generate datasets
    original_df = generate_original_dataset()

    params = get_distribution_params(original_df, "Value1")
    average = params['mean']
    std_dev = params['std_deviation']

    # Get category probabilities
    category_probs = original_df['Category1'].value_counts(normalize=True).sort_index().tolist()
    print(f"Category probabilities: {category_probs}")
    counted_nums = original_df['Category1'].value_counts(normalize=False).sort_index().tolist()
    print("Category probabilities: ")
    print(' '.join(str(x / 500) for x in counted_nums))

    # Get parameters for Value2
    params2 = get_distribution_params(original_df, "Value2")

    # Generate new dataset with similar parameters
    # category_probs = [1, 0, 0, 0, 0]
    new_df = generate_dataset(
        seed=123,  # Different seed for variation
        num_samples=1000,
        p=category_probs,
        avg1=average,
        avg2=params2['mean'],
        std_dev1=std_dev,
        std_dev2=params2['std_deviation']
    )
    print("New category distribution: ")
    print(new_df['Category1'].value_counts(normalize=True).sort_index().tolist())

    # Save both datasets
    original_df.to_csv("original_dataset.csv", sep=";", index=False)
    new_df.to_csv("new_dataset.csv", sep=";", index=False)

    # Verify similarity
    simple_similarity_check(original_df, new_df)
    verify_similarity(original_df, new_df)

