import pandas as pd
import time
import os
from openai import OpenAI

# -----------------------------
# Configuration
# -----------------------------
INPUT_CSV = "./shuffle_stratified_split/reviews_more_than_40_words_3000_stratified.csv"
OUTPUT_CSV = "./extracted_relevant_info/reviews_40+_words_strat_shuffle_split_3k.csv"

REVIEW_COLUMN_INDEX = 6  # 7th column (0-based)
MODEL_NAME = "deepseek-chat"
SLEEP_SECONDS = 0.1

#client = OpenAI(api_key="YOUR_API_KEY")
client = OpenAI(api_key="sk-089c25df7bec40f2a83a377aa243af74",\
    base_url="https://api.deepseek.com",)

# -----------------------------
# Prompt
# -----------------------------
SYSTEM_PROMPT = """
You are an expert product analyst.

The product is a child car seat.
The product has exactly five attributes:
1. Seat Type (examples: Rear Facing, Forward Facing, Convertible, Right Handle, etc.)
2. Weight Range of Child
3. Installation Type (examples: Clicktight, Seat Belt, Latch, Snaps, etc.)
4. Harness Type
5. Material

Your task:
- Read the review text.
- Determine whether it contains any information related to ANY of the five attributes.

Response rules (STRICT):
1. If there is NO relevant information, reply exactly:
   No
2. If there IS relevant information:
   - Group information under the corresponding attribute names.
   - Only include attributes mentioned in the review.
   - Do NOT include explanations or extra text.

Review text:
"""

def analyze_review(review_text: str) -> str:
    #print("hjh check user prompt: \n",f'The review text is:\n"""\n{review_text}\n"""')
    #print("\n\n")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            #{"role": "user", "content": review_text}
            {"role": "user", "content": f'The review text is:\n"""\n{review_text}\n"""'}
        ],
        temperature=0
    )
    #print(response)
    return response.choices[0].message.content.strip()

# -----------------------------
# Load Input CSV (always)
# -----------------------------
df_input = pd.read_csv(INPUT_CSV)

# Ensure output columns exist
df_input["Has_Relevant_Attribute_Info"] = ""
df_input["Attribute_Related_Content"] = ""

# -----------------------------
# If output CSV exists, merge progress
# -----------------------------
if os.path.exists(OUTPUT_CSV):
    print("Existing output found. Loading progress...")
    df_output = pd.read_csv(OUTPUT_CSV)

    for col in ["Has_Relevant_Attribute_Info", "Attribute_Related_Content"]:
        if col in df_output.columns:
            df_input[col] = df_output[col]

df = df_input

# -----------------------------
# Main Loop (skip processed)
# -----------------------------
for idx, row in df.iterrows():
    #print('hjh check index id: ',idx)
    if(idx==3000):
        break
    if str(row["Has_Relevant_Attribute_Info"]).strip() in ["Yes", "No"]:
        continue

    review_text = str(row.iloc[REVIEW_COLUMN_INDEX])

    try:
        result = analyze_review(review_text)
    except Exception as e:
        print(f"Error at row {idx}: {e}")
        continue  # leave row unprocessed

    if result.lower() == "no":
        df.at[idx, "Has_Relevant_Attribute_Info"] = "No"
        df.at[idx, "Attribute_Related_Content"] = "No"
    else:
        df.at[idx, "Has_Relevant_Attribute_Info"] = "Yes"
        df.at[idx, "Attribute_Related_Content"] = result

    # Save progress after each row
    df.to_csv(OUTPUT_CSV, index=False)
    
    print(f"Processed row {idx}/{len(df)}")

    time.sleep(SLEEP_SECONDS)
    
    #break
    
print("Processing complete.")
