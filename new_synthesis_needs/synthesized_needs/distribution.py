import pandas as pd

# 1. Load CSV file
csv_path = "train_set_transformed.csv"   # <-- change this
df = pd.read_csv(csv_path)

# 2. Select the first 5 columns (label columns)
label_cols = df.columns[:5]

# 3. Count label distribution for each column
label_distribution = {}

for col in label_cols:
    label_distribution[col] = df[col].value_counts().sort_index()

# 4. Display results
for col, counts in label_distribution.items():
    print(f"\nLabel distribution for column '{col}':")
    print(counts)
