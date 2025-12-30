import pandas as pd

# Input and output file paths
input_csv = "reviews_more_than_40_words.csv"
output_csv = "reviews_more_than_40_words_shuffled.csv"

# Load the CSV file
df = pd.read_csv(input_csv)

# Shuffle the data samples (rows)
# frac=1 means shuffle all rows
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled data to a new CSV file
df_shuffled.to_csv(output_csv, index=False)

print(f"Shuffled CSV saved to: {output_csv}")
