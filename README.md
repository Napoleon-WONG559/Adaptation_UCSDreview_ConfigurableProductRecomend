# Adaptation_UCSDreview_ConfigurableProductRecomend
This repository includes the implementation work of adapting UCSD's review dataset for configurable product recommendation.

## Data processing framework
### Step 1 : Extraction of all specifications under all attributes for each product

In this step, the file of "*./code/extract_specification.py*" conduct the extraction of all specifications under all attributes for each product. This is prerequisite step for mapping specification to trainable or learnable label outputs.

### Step 2 : Cluster the extracted specifications for each attribute

We record the clusters of specifications for each attribute in the file of "*code/product_cluster.py*"(e.g. "*code/car_seat_cluster.py*"). This is necessary to specify that each specification should be mapped to which label.

**Note: This step formalizes each attribute as a multi-class classification task.**

The file of "*code/product_cluster.py*" looks like below:

    Cluster = {
     "Seat Type": {
        #rear_facing_only
         "0": ["Rear Facing", "Rear forward facing"],

         #forward_facing_only
         "1": ["Forward Facing", "Front-Facing"],
         ...
     },
    
     "Weight Range": {
         "0": [...],
         "1": [...],
         ...
     }
    }

### Step 3 : Map the specification to label

In this step, the file of "./code/map_spec_to_label.py" will map all attribute specifications to labels for all products based on the cluster mentioned in **Step 2**.

### Step 4 : Concatenate the review text with labels of corresponding product's all attributes

The file of "*./code/concat_review_attribute.py*" will concatenate the review text with the labels of corresponding product's all attributes. This step finally outputs a csv file.

The format of output csv file looks like below:

| review | attribute_1 | attribute_2 | attribute_3 | ... |
|----|----|----|----|----|
| Good product! ... | label_1_1 | label_1_2 | label_1_3 | ...|
| Nice! ... | label_2_1 | label_2_2 | label_2_3 | ...|
| ... | ... | ... | ... | ...|

### Step 5 : Split the dataset into smaller part for later "Review-to-Needs" Transformation

The file of "*./code/split_review_data.py*" splits the whole dataset from **Step 4** into smaller parts. The smaller parts will serve as the source data which will then be transformed into the needs text data.

### Step 6 : "Review-to-Needs" Transformation

The file of "*./code/review_to_needs_transform_update.py*" transforms the review text into the needs text through intructing LLM by prompting.

## Processed data

### Car seat

There are 5 attributes for car seat. They are **Seat Type**, **Weight Range**, **Installation Type**, **Harness Type**, **Material**.

||Seat Type|Weight Range|Installation Type|Harness Type|Material|
|---|---|---|---|---|---|
|class number|5|8|5|4|6|

# Progress Record

**2025.12** Develop the data processing framework for adaptation of UCSD review dataset to configurable product recommendation.