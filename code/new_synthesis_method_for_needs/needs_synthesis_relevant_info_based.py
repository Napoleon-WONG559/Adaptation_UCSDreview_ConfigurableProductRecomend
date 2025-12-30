import pandas as pd
import time
import os
from openai import OpenAI

# -----------------------------
# Configuration
# -----------------------------
INPUT_CSV = "./extracted_relevant_info/reviews_40+_words_strat_shuffle_split_3k.csv"
OUTPUT_CSV = "./synthesized_needs/processed_reviews_with_needs.csv"

RELEVANT_FLAG_COL = 8   # 9th column (0-based)
RELEVANT_INFO_COL = 9   # 10th column (0-based)

MODEL_NAME = "deepseek-chat"
SLEEP_SECONDS = 0.1

#client = OpenAI(api_key="YOUR_API_KEY")
client = OpenAI(api_key="sk-089c25df7bec40f2a83a377aa243af74",\
    base_url="https://api.deepseek.com",)

# -----------------------------
# System Prompt
# -----------------------------
SYSTEM_PROMPT = """
You are an expert in customer needs analysis.

You will be given product attribute–related information extracted from customer reviews.
The product is a child car seat.

Your task:
- Convert the information into clear customer needs statements.

Rules:
1. If the information describes positive advantages or desirable features,
   express them directly as customer needs.
2. If the information describes problems, complaints, limitations, or negative issues,
   express them as customer needs indicating that these issues are acceptable or tolerable.
3. Do NOT propose fixes, improvements, or solutions for negative issues.
4. Do NOT mention attributes explicitly unless necessary.
5. Do NOT add explanations, metadata, or headings.
6. Output ONLY the synthesized customer needs text.
"""

def synthesize_needs(relevant_info: str) -> str:
    """Call LLM to synthesize customer needs."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
The attribute-related information is:

\"\"\"
{relevant_info}
\"\"\"
"""
            }
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# -----------------------------
# Load data (resume-safe)
# -----------------------------
df_input = pd.read_csv(INPUT_CSV)

# Add output column if not present
NEEDS_COL = "Synthesized_Customer_Needs"
if NEEDS_COL not in df_input.columns:
    df_input[NEEDS_COL] = ""

# If output CSV exists, restore progress
if os.path.exists(OUTPUT_CSV):
    print("Existing output found. Restoring progress...")
    df_existing = pd.read_csv(OUTPUT_CSV)
    if NEEDS_COL in df_existing.columns:
        df_input[NEEDS_COL] = df_existing[NEEDS_COL]

df = df_input

# -----------------------------
# Main Loop
# -----------------------------
for idx, row in df.iterrows():
    #print(idx)
    if(idx==3000):
        print("hjh check break")
        break
        
    # Skip if no relevant info
    if str(row.iloc[RELEVANT_FLAG_COL]).strip() != "Yes":
        #print("Not Yes: ",idx)
        continue

    # Skip if already processed (non-null and non-empty)
    #if str(row[NEEDS_COL]).strip() != "":
    if pd.notna(row[NEEDS_COL]) and str(row[NEEDS_COL]).strip() != "":
        #print("Not empty: ",idx)
        #print("content: ",str(row[NEEDS_COL]).strip())
        continue

    relevant_info = str(row.iloc[RELEVANT_INFO_COL]).strip()
    if not relevant_info or relevant_info.lower() == "no" or relevant_info.lower() == "material":
        #print("hjh check No.",idx," : ", relevant_info.lower())
        continue

    try:
        needs_text = synthesize_needs(relevant_info)
    except Exception as e:
        print(f"Error at row {idx}: {e}")
        continue

    df.at[idx, NEEDS_COL] = needs_text

    # Save progress after each row
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"Processed row {idx}/{len(df)}")
    
    time.sleep(SLEEP_SECONDS)

    #break
    
print("Needs text synthesis completed.")
print(f"Saved to: {OUTPUT_CSV}")
