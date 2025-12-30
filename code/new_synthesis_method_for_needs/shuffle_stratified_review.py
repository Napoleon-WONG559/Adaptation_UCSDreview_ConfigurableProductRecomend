import pandas as pd

# Input / output paths
input_csv = "reviews_more_than_40_words.csv"
output_csv = "reviews_more_than_40_words_stratified_shuffled.csv"

# Load CSV
df = pd.read_csv(input_csv)

# Identify first 5 columns as stratification labels
strat_cols = df.columns[:5].tolist()

# Multi-column stratified shuffle
df_stratified_shuffled = (
    df.groupby(strat_cols, group_keys=False)
      .apply(lambda x: x.sample(frac=1, random_state=42))
      .reset_index(drop=True)
)

# Save result
df_stratified_shuffled.to_csv(output_csv, index=False)

print("Multi-column stratified shuffling completed.")
print(f"Saved to: {output_csv}")
