import matplotlib.pyplot as plt
from generator import generate_original_dataset
from generator import generate_similar_dataset

def simple_similarity_check(original_df, new_df):
    """A simpler way to check if datasets are similar"""

    # Check if averages are close (within 10%)
    avg1_orig = original_df['Value1'].mean()
    avg1_new = new_df['Value1'].mean()
    difference_percent = abs(avg1_orig - avg1_new) / avg1_orig * 100

    print(f"Original average: {avg1_orig:.2f}")
    print(f"New average: {avg1_new:.2f}")
    print(f"Difference: {difference_percent:.1f}%")

    if difference_percent < 10:
        print("✅ Averages are similar!")
    else:
        print("❌ Averages are too different!")

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
    original_df = generate_original_dataset()
    new_df = generate_similar_dataset()
    simple_similarity_check(original_df, new_df)
