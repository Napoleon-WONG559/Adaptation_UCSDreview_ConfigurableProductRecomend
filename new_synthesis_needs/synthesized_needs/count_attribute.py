import pandas as pd

# Input CSV file
input_csv = "processed_reviews_with_needs_filter.csv"

# Load CSV
df = pd.read_csv(input_csv)

# 10th column (0-based index = 9)
text_series = df.iloc[:, 9].dropna().astype(str)

# Attributes to count
attributes = [
    "Seat Type",
    "Weight Range",
    "Installation Type",
    "Harness Type",
    "Material"
]

# Count occurrences
counts = {}
for attr in attributes:
    counts[attr] = text_series.str.count(attr).sum()

# Print results
print("Attribute occurrence counts in 10th column:")
for attr, count in counts.items():
    print(f"{attr}: {count}")
