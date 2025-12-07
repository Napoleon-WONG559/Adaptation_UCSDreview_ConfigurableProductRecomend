import pandas as pd

# ---- Step 1: Read original CSV file ----
input_file = "./car_seat/unsplit_all_data/merged_attribute_review_data_final_1.csv"   # change this to your file name
df = pd.read_csv(input_file)

# ---- Step 2: Shuffle (randomize) the data samples ----
df_shuffled = df.sample(frac=1, random_state=None).reset_index(drop=True)

# ---- Step 3: Split the data (excluding header) ----
# Calculate the split index
split_index = 3000

# Two parts
df_part1 = df_shuffled.iloc[:split_index]      # first half
df_part2 = df_shuffled.iloc[split_index:]      # second half

# ---- Step 4: Save each part to a new CSV file (header included automatically) ----
df_part1.to_csv("./car_seat/split_data/merge_attr_review_part1.csv", index=False)
df_part2.to_csv("./car_seat/split_data/merge_attr_review_part2.csv", index=False)

print("Data shuffled, split and saved successfully!")
