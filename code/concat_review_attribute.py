import pandas as pd

# --------------------------------------------------------------
# 1) Load files
# --------------------------------------------------------------
attributes_df = pd.read_csv("./car_seat/car_seat_detail_transformed.csv", header=None)
#reviews_df = pd.read_excel("./car_seat/template_review_data.xlsx", header=None)
#reviews_df = pd.read_csv("./car_seat/template_review_data.csv", header=None)
reviews_df = pd.read_csv("./result/UCSD/car_seat_data/car_seat_data.csv", header=None, dtype=str)

# --------------------------------------------------------------
# 2) Extract product IDs
# --------------------------------------------------------------
# File A (attributes): second row (index 1)
attribute_ids = attributes_df.iloc[1, 1:].tolist()

# File B (reviews): first row (index 0)
review_ids = reviews_df.iloc[0, 1:].tolist()
#print(review_ids)
# --------------------------------------------------------------
# 3) Map product_id → column index for both files
# --------------------------------------------------------------
attribute_col_index = {pid: idx+1 for idx, pid in enumerate(attribute_ids)}
review_col_index = {pid: idx+1 for idx, pid in enumerate(review_ids)}

# --------------------------------------------------------------
# 4) Extract category names (first column)
# --------------------------------------------------------------
category_names = attributes_df.iloc[2:8, 0].tolist()   # 6 categories, rows 2–7

# --------------------------------------------------------------
# 5) Build combined rows
# --------------------------------------------------------------
output_rows = []
output_columns = category_names + ["Review"]

# For each product ID that appears in BOTH files
common_ids = set(attribute_ids).intersection(set(review_ids))
#print(common_ids)
for pid in common_ids:

    # Column numbers
    attr_col = attribute_col_index[pid]
    rev_col = review_col_index[pid]

    # Extract 6 category values for this product
    categories = attributes_df.iloc[2:8, attr_col].tolist()

    # Extract all reviews for this product (skip row 0)
    product_reviews = reviews_df.iloc[1:, rev_col].dropna().tolist()

    # Build output rows
    for review in product_reviews:
        output_rows.append(categories + [review])

# --------------------------------------------------------------
# 6) Save output
# --------------------------------------------------------------
out_df = pd.DataFrame(output_rows, columns=output_columns)
out_df.to_csv("./car_seat/merged_attribute_review_data_final_1.csv", index=False)
