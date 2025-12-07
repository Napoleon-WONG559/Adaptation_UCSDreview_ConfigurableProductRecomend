import pandas as pd
from car_seat_cluster import clusters

# Load original CSV
df = pd.read_csv("./car_seat/car_seat_detail.csv", header=None)

# Read category names (first column)
category_names = df[0].tolist()

"""
Assume you have a dictionary like this:
Each key is a category name from column 0,
Each value is the cluster dictionary for that category.
"""

# Build a mapping for each category: raw_value → cluster_name
category_mappings = {}

for category, cluster_dict in clusters.items():
    mapping = {}
    for cluster_name, raw_values in cluster_dict.items():
        for value in raw_values:
            mapping[value] = cluster_name
    category_mappings[category] = mapping

Abnormal = set()

# Apply transformations
for row_idx, category in enumerate(category_names):
    
    # Skip categories not included in clusters dictionary
    if category not in category_mappings:
        print("not in mappings: ",category)
        continue
    
    mapping = category_mappings[category]
    
    # Replace values in all product columns (skip column 0)
    for col in df.columns[1:]:
        value = df.at[row_idx, col]
        if value in mapping:
            df.at[row_idx, col] = mapping[value]
        if pd.notna(value)==False:
            df.at[row_idx, col] = mapping["csv_na"]

        if value not in mapping:
            if pd.notna(value):
                #print("Abnormal: ",value)
                Abnormal.add(value)

print(Abnormal)

# Save transformed CSV
df.to_csv("./car_seat/car_seat_detail_transformed.csv", index=False, header=False)
