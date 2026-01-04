import pandas as pd
import numpy as np

# -----------------------------
# Configuration
# -----------------------------
INPUT_CSV = "processed_reviews_with_needs_filter.csv"
SAMPLED_CSV = "train_set.csv"
REMAINING_CSV = "test_set.csv"

TARGET_SIZE = 1267
RANDOM_STATE = 42

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv(INPUT_CSV)

# First 5 columns used for stratification
strat_cols = df.columns[:5].tolist()

# Add a temporary unique row ID (important!)
df["_row_id"] = np.arange(len(df))

# -----------------------------
# Compute sampling fraction
# -----------------------------
sampling_fraction = TARGET_SIZE / len(df)

# -----------------------------
# Stratified sampling (proportional)
# -----------------------------
sampled_df = (
    df.groupby(strat_cols, group_keys=False)
      .apply(lambda x: x.sample(
          n=max(1, int(len(x) * sampling_fraction)),
          random_state=RANDOM_STATE
      ))
)

# If oversampled, downsample globally to exact size
if len(sampled_df) > TARGET_SIZE:
    sampled_df = sampled_df.sample(
        n=TARGET_SIZE,
        random_state=RANDOM_STATE
    )

# -----------------------------
# Split remaining samples
# -----------------------------
sampled_ids = set(sampled_df["_row_id"])
remaining_df = df[~df["_row_id"].isin(sampled_ids)]

# -----------------------------
# Final shuffle (optional but recommended)
# -----------------------------
sampled_df = sampled_df.sample(frac=1, random_state=RANDOM_STATE)
remaining_df = remaining_df.sample(frac=1, random_state=RANDOM_STATE)

# -----------------------------
# Cleanup and save
# -----------------------------
sampled_df = sampled_df.drop(columns=["_row_id"])
remaining_df = remaining_df.drop(columns=["_row_id"])

sampled_df.to_csv(SAMPLED_CSV, index=False)
remaining_df.to_csv(REMAINING_CSV, index=False)

print(f"Sampled set saved: {len(sampled_df)} rows → {SAMPLED_CSV}")
print(f"Remaining set saved: {len(remaining_df)} rows → {REMAINING_CSV}")

assert len(sampled_df) + len(remaining_df) == len(df)
assert set(sampled_df.index).isdisjoint(set(remaining_df.index))
print("Split verified: no overlap, no loss.")
