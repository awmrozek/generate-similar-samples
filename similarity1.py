import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def similarity_check(original_df, new_df, column):
    avg_orig = original_df[column].mean()
    avg_new = new_df[column].mean()
    difference_percent = abs(avg_orig - avg_new) / avg_orig * 100

    print(f"Original average: {avg_orig:.2f}")
    print(f"New average: {avg_new:.2f}")
    print(f"Difference: {difference_percent:.1f}%")

    if difference_percent < 10:
        print("Averages are similar!")
    else:
        print("Averages are too different!")


def simple_similarity_check(original_df, new_df):
    """A simpler way to check if datasets are similar"""

    # Check if averages are close (within 10%)
    similarity_check(original_df, new_df, 'Value1')
    similarity_check(original_df, new_df, 'Value2')

    # Check if spread is close
    spread1_orig = original_df['Value1'].std()
    spread1_new = new_df['Value1'].std()

    print(f"\nOriginal spread: {spread1_orig:.2f}")
    print(f"New spread: {spread1_new:.2f}")

    # Visual check - overlay histograms
    plt.hist(original_df['Value1'], bins=30, alpha=0.5, label='Original')
    plt.hist(new_df['Value1'], bins=30, alpha=0.5, label='New')
    plt.legend()
    plt.title('Do these look similar?')
    plt.show()

if __name__ == "__main__":
    original_df = pd.read_csv('original_dataset.csv')
    new_df = pd.read_csv('new_similar_dataset.csv')
    simple_similarity_check(original_df, new_df)
