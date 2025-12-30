import pandas as pd

# Load the original CSV file
input_csv = "merged_attribute_review_data_final.csv"
df = pd.read_csv(input_csv)

# Extract the 7th column (review text) and ensure string type
review_texts = df.iloc[:, 6].astype(str)

# Compute word count for each review
word_counts = review_texts.apply(lambda x: len(x.split()))

print(word_counts.describe())

# Add word count as a temporary column (optional, but helpful)
df["review_word_count"] = word_counts

# Split the data
df_long = df[df["review_word_count"] > 40]
df_short = df[df["review_word_count"] <= 40]

# Save to separate CSV files
df_long.to_csv("reviews_more_than_40_words.csv", index=False)
df_short.to_csv("reviews_40_words_or_less.csv", index=False)

print(f"Saved {len(df_long)} samples with > 40 words")
print(f"Saved {len(df_short)} samples with ≤ 40 words")
