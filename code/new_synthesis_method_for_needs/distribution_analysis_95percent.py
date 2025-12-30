import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("reviews_more_than_40_words.csv")
review_texts = df.iloc[:, 6].astype(str)
#review_lengths = review_texts.apply(len)
review_lengths = review_texts.apply(lambda x: len(x.split()))

print("Review Length Statistics:")
print(review_lengths.describe())

# Compute percentile cutoff
percentile_cutoff = 95
x_max = np.percentile(review_lengths, percentile_cutoff)

print("Review Length Statistics:")
print(review_lengths.describe())

# Plot
plt.figure(figsize=(8, 5))
plt.hist(review_lengths, bins=50, range=(0, x_max))
plt.xlabel("Review Length (characters)")
plt.ylabel("Frequency")
plt.title(f"Review Length Distribution (up to {percentile_cutoff}th percentile)")
plt.tight_layout()

# Save plot
plt.savefig("review_40words_more_length_distribution_95pct.pdf", dpi=300)
plt.close()
