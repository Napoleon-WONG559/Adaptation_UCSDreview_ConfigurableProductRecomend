import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
# Replace with your actual file path
file_path = "merged_attribute_review_data_final.csv"
df = pd.read_csv(file_path)

# 2. Extract the 7th column (index 6)
# Assumes the 7th column contains review text
review_texts = df.iloc[:, 6].astype(str)

# 3. Compute review lengths
# You can use len(text) for character length
# or len(text.split()) for word count
#review_lengths = review_texts.apply(len)
review_lengths = review_texts.apply(lambda x: len(x.split()))

# 4. Basic statistics
print("Review Length Statistics:")
print(review_lengths.describe())

# 5. Plot distribution (histogram)
plt.figure(figsize=(8, 5))
plt.hist(review_lengths, bins=50)
plt.xlabel("Review Length (characters)")
plt.ylabel("Frequency")
plt.title("Distribution of Review Text Lengths")
#plt.tight_layout()

output_path = "review_length_distribution.pdf"
plt.tight_layout()
plt.savefig(output_path, dpi=300)

plt.show()
