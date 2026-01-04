import pandas as pd

# Input and output file paths
input_csv = "processed_reviews_with_needs.csv"
output_csv = "processed_reviews_with_needs_filter.csv"

# Load the CSV file
df = pd.read_csv(input_csv)

# 10th column (0-based index = 9)
col_index = 9

# Filter rows
df_filtered = df[~df.iloc[:, col_index].isin(["No", "Material"])]

# Save to new CSV
df_filtered.to_csv(output_csv, index=False)

print(f"Filtered CSV saved to: {output_csv}")
