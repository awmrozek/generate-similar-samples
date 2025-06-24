import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def verify_similarity(original_df, new_df):
    """Check if the new dataset is similar to the original"""
    print("=== Similarity Verification ===\n")

    # 1. Check letter frequencies
    print("Letter Frequencies:")
    print("Original:", dict(original_df['Category1'].value_counts(normalize=True).round(3)))
    print("New:     ", dict(new_df['Category1'].value_counts(normalize=True).round(3)))
    print()

    # 2. Check number statistics
    print("Value1 Statistics:")
    print(f"Original - Average: {original_df['Value1'].mean():.2f}, Spread: {original_df['Value1'].std():.2f}")
    print(f"New      - Average: {new_df['Value1'].mean():.2f}, Spread: {new_df['Value1'].std():.2f}")
    print()

    print("Value2 Statistics:")
    print(f"Original - Average: {original_df['Value2'].mean():.2f}, Spread: {original_df['Value2'].std():.2f}")
    print(f"New      - Average: {new_df['Value2'].mean():.2f}, Spread: {new_df['Value2'].std():.2f}")
    print()

    # 3. Statistical tests (explained simply)
    _, p_value1 = stats.ks_2samp(original_df['Value1'], new_df['Value1'])
    _, p_value2 = stats.ks_2samp(original_df['Value2'], new_df['Value2'])

    print("Statistical Similarity (higher is better, >0.05 is good):")
    print(f"Value1 similarity score: {p_value1:.3f}")
    print(f"Value2 similarity score: {p_value2:.3f}")

    # 4. Visual comparison
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Letter frequencies
    original_counts = original_df['Category1'].value_counts().sort_index()
    new_counts = new_df['Category1'].value_counts().sort_index()

    x = np.arange(len(original_counts))
    width = 0.35

    axes[0, 0].bar(x - width/2, original_counts, width, label='Original', alpha=0.8)
    axes[0, 0].bar(x + width/2, new_counts, width, label='New', alpha=0.8)
    axes[0, 0].set_xlabel('Letters')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].set_title('Letter Distribution Comparison')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(original_counts.index)
    axes[0, 0].legend()

    # Value1 distributions
    axes[0, 1].hist(original_df['Value1'], bins=30, alpha=0.5, label='Original', density=True)
    axes[0, 1].hist(new_df['Value1'], bins=30, alpha=0.5, label='New', density=True)
    axes[0, 1].set_xlabel('Value1')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Value1 Distribution')
    axes[0, 1].legend()

    # Value2 distributions
    axes[1, 0].hist(original_df['Value2'], bins=30, alpha=0.5, label='Original', density=True)
    axes[1, 0].hist(new_df['Value2'], bins=30, alpha=0.5, label='New', density=True)
    axes[1, 0].set_xlabel('Value2')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Value2 Distribution')
    axes[1, 0].legend()

    # Scatter plot
    axes[1, 1].scatter(original_df['Value1'], original_df['Value2'], alpha=0.5, label='Original', s=10)
    axes[1, 1].scatter(new_df['Value1'], new_df['Value2'], alpha=0.5, label='New', s=10)
    axes[1, 1].set_xlabel('Value1')
    axes[1, 1].set_ylabel('Value2')
    axes[1, 1].set_title('Value1 vs Value2 Relationship')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('similarity_comparison.png')
    plt.show()

