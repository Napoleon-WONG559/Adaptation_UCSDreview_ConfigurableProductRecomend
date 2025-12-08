import csv
import time
from openai import OpenAI
import os

client = OpenAI(api_key="",\
    base_url="https://api.deepseek.com",)

INPUT_CSV = "./car_seat/split_data/merge_attr_review_part1.csv"
OUTPUT_CSV = "./car_seat/split_data/output.csv"
MODEL_NAME = "deepseek-chat"

SYSTEM_PROMPT = """
You are an assistant that converts customer review text into customer needs text. 
Given a review, express the review in the form of a needs in a random tone or style. 
Do not repeat the original text. Directly output the needs. 
The review is :
"""

def review_to_needs(review_text):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": review_text}
        ]
    )
    return response.choices[0].message.content.strip()


def count_existing_rows(file_path):
    """Counts how many rows already exist in the output file."""
    if not os.path.exists(file_path):
        return 0

    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def transform_csv():
    processed_rows = count_existing_rows(OUTPUT_CSV)
    print(f"Existing rows in output: {processed_rows}")

    with open(INPUT_CSV, "r", newline="", encoding="utf-8") as infile, \
         open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # 1. Always read and store the header
        header = next(reader)

        # 2. If output file is empty, write the header
        if processed_rows == 0:
            writer.writerow(header)
            print("Wrote header to output.")

        # 3. Skip already-processed rows in the input
        rows_to_skip = processed_rows - 1  # minus header
        print(f"Skipping {rows_to_skip} processed data rows.")

        for _ in range(rows_to_skip):
            next(reader, None)

        # 4. Process the remaining rows
        for i, row in enumerate(reader, start=processed_rows):
            review = row[6]

            try:
                needs_text = review_to_needs(review)
            except Exception as e:
                print(f"Error on row {i}: {e}")
                needs_text = ""

            new_row = row[:6] + [needs_text]
            writer.writerow(new_row)

            print(f"Processed row {i}")
            time.sleep(0.2)  # optional to avoid rate limits
            #if(i==7):
            #    break

    print("Processing complete.")


if __name__ == "__main__":
    transform_csv()
