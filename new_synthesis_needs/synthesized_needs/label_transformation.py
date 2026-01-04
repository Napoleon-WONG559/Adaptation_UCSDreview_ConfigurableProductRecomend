import pandas as pd

# Input / output files
input_csv = "test_set.csv"
output_csv = "test_set_transformed.csv"

# Load CSV
df = pd.read_csv(input_csv)

# 2nd column (0-based index = 1)
label_col = df.columns[1]

# Define mapping function
def transform_label(x):
    if x in [0, 1, 2]:
        return 0
    elif x == 3:
        return 1
    elif x == 4:
        return 2
    elif x in [5, 6, 7]:
        return 2
    else:
        raise ValueError(f"Unexpected label value: {x}")

# Apply transformation
df[label_col] = df[label_col].apply(transform_label)

# Save result
df.to_csv(output_csv, index=False)

print("Label transformation completed.")
print(f"Saved to: {output_csv}")
