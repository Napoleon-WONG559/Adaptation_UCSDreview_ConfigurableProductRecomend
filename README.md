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

# Result

## Car seat
|Accuracy|Seat Type|Weight Range|Installation Type|Harness Type|Material|
|---|---|---|---|---|---|
|LoRA|38.4|51.5|66.5|64.0|35.2|
|LoRA + soft ensemble|39.4|51.8|67.2|65.8|36.3|

### Breakdown of car seat attribute

#### Attribute 1: seat type: *39.4%*

||0|1|2|3|4|
|---|---|---|---|---|---|
|sample number|852|934|654|69|491|

#### Attribute 2: weight range: *51.8%*

||0|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|---|
|sample number|75|49|118|809|1435|330|3|181|

#### Attribute 3: installation type: *67.2%*

||0|1|2|3|4|
|---|---|---|---|---|---|
|sample number|1879|775|28|104|214|

#### Attribute 4: harness type: *65.8%*

||0|1|2|3|
|---|---|---|---|---|
|sample number|1798|732|464|6|

#### Attribute 5: material: *36.3%*

||0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|sample number|944|372|314|820|37|513|

### Conclusion from the breakdown

**Conclusion**: The more dispersed the label distribution, namely the more difficult the attribute task, the worse the performance.

### Analysis of the conclusion

We found that the performance relates to the dispersal degree of label distribution, which is equivalent to the difficulty of the attribute task. Below is the analysis of this conclusion.

One of the possible reasons is that the customer needs text data samples are similar in semantics. We notice that many needs text revolves around some common points, but has very different labels.

For example, we show some needs text and their labels below:

|Needs|attr1|attr2|attr3|attr4|attr5|
|---|---|---|---|---|---|
|"I need a product that consistently performs well without any issues."|4|4|1|1|0|
|"I need a product that consistently meets my expectations without any flaws."|2|4|0|0|1|
|"I need a product that consistently meets my expectations and brings me joy."|2|3|0|0|3|
|"I need products to consistently meet my expectations, arriving on time or even early, and in perfect condition to ensure the recipient's delight."|1|4|1|1|5|
|"I need products that consistently deliver excellent quality and exceed my expectations."|4|4|0|0|2|
|"I need products that consistently deliver outstanding quality and exceed my expectations."|1|4|1|0|3|

We check the original review text that corresponds to these needs text as below:

|Needs|Review|
|---|---|
|"I need a product that consistently performs well without any issues."|"Works great!"|
|"I need a product that consistently meets my expectations without any flaws."|"Perfect"|
|"I need a product that consistently meets my expectations and brings me joy."|"Love it!!"|
|"I need products to consistently meet my expectations, arriving on time or even early, and in perfect condition to ensure the recipient's delight."|"Product was as expected arrived a day early in great condition. Grandson loves it."|
|"I need products that consistently deliver excellent quality and exceed my expectations."|"Great"|
|"I need products that consistently deliver outstanding quality and exceed my expectations."|"Excellent"|

Furthermore, we found that several data samples with the same needs text have different label annotation.

|Needs|Review|attr1|attr2|attr3|attr4|attr5|
|---|---|---|---|---|---|---|
|I need a product that consistently meets my expectations without any flaws.|Perfect|2|4|0|0|1|
|I need a product that consistently meets my expectations without any flaws.|Perfect|2|3|0|0|3|
|I need a product that consistently meets my expectations without any flaws.|Perfect|0|5|0|0|0|
|I need a product that consistently meets my expectations without any flaws.|Perfect|1|4|1|1|0|

**Analysis insight**: In this case, we realize that *directly transforming review text into needs text* can cause a problem. The problem is the generated needs text will become very similar in semantics. In addition, many data samples have different label annotations, but the needs text of these samples revolves around some common points.

This makes distinguishing the needs text challenging and furthermore, makes *classifying the non-distinguishable needs text into correct attribute specification* very difficult.

# Progress Record

**2025.12** Develop the data processing framework for adaptation of UCSD review dataset to configurable product recommendation.