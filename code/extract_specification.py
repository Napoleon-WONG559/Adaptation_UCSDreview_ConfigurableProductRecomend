import pandas as pd

# Load CSV (no header row in file)
df = pd.read_csv("./car_seat/car_seat_detail.csv", header=None)

# The first column contains row category labels
category_labels = df[0].tolist()

# We only want rows 2–7 (last 6 categories)
selected_rows = list(range(2, 8))  # [2,3,4,5,6,7]

# Create a dictionary of sets, one for each category
category_sets = {category_labels[r]: set() for r in selected_rows}

# Loop through each product column (starting from column index 1)
for col in df.columns[1:]:
    for r in selected_rows:
        value = df.at[r, col]
        if pd.notna(value):
            category_sets[category_labels[r]].add(value)
        #category_sets[category_labels[r]].add(value)

# Now you have 6 sets:
# category_sets["Seat Type"], category_sets["Weight Range"], ...
# Print them to verify
for category, values in category_sets.items():
    print(f"\n=== {category} ===")
    print(values)
