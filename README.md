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
|class number|5|3|5|4|6|

### Bike

There are 7 attributes for bike product. They are **Bike Type**, **Age Range**, **Wheel Size**, **Number of Speeds**, **Brake Style**, **Frame Material**, **Suspension Type**.

||Bike Type|Age Range|Wheel Size|Number of Speeds|Brake Style|Frame Material|Suspension Type|
|---|---|---|---|---|---|---|---|
|class number|4|4|4|5|4|4|3|

Based on our previous experience and insights gained from experiments in car seat product, we limited the class number for each attribute task under no more than 5 classes. Below is the label distribution for each attribute task.

|Bike Type distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|730|722|744|767|

|Age Range distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|407|397|213|1946|

|Wheel Size distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|615|655|1449|244|

|Number of Speeds distribution|0|1|2|3|4|
|---|---|---|---|---|---|
|sample number|1023|111|616|32|1181|

|Brake Style distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|783|714|229|1237|

|Frame Material distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|1246|1533|27|157|

|Suspension Type distribution|0|1|2|
|---|---|---|---|
|sample number|855|726|1382|

### Smart watch

There are 3 attributes for smart watch product. They are **Screen Size**, **Display Type**, **Battery Life**.

The other 3 information(**Special Features**, **Waterproof Rating**, **Target Audience**) in the dataset is not appropriate for the configuration task. The **Special Features** contains only free text without clustering pattern, the **Waterproof Rating** concentrates almost all samples in one class, and the **Target Audience** itself is not a configurable attribute.

||Screen Size|Display Type|Battery Life|
|---|---|---|---|
|class number|3|3|2|

The label distribution for each attribute is shown below:

|Screen Size distribution|0|1|2|
|---|---|---|---|
|sample number|710|1072|620|

|Display Type distribution|0|1|2|
|---|---|---|---|
|sample number|375|1088|939|

|Battery Life distribution|0|1|
|---|---|---|
|sample number|784|1618|

*Note: The data inconsistency issue exists in the dataset of the smart watch. Below is the relevant information occurrence times for each attribute.*

||Screen Size|Display Type|Battery Life|
|---|---|---|---|
|occurrence times of relevant information|680|521|2114|

*Besides, the relevant information of Battery Life often contains "long battery life" merely or neutral description about charging frequency(e.g. once a week).*

# Result

## Car seat
|model(Llama 3B)|Seat Type|Weight Range|Installation Type|Harness Type|Material|
|---|---|---|---|---|---|
|LoRA|38.4|51.5|66.5|64.0|35.2|
|LoRA + soft ensemble|39.4|51.8|67.2|65.8|36.3|

### Breakdown of car seat attribute

#### Attribute 1: seat type: *39.4%*

|label distribution|0|1|2|3|4|
|---|---|---|---|---|---|
|sample number|852|934|654|69|491|

#### Attribute 2: weight range: *51.8%*

|label distribution|0|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|---|
|sample number|75|49|118|809|1435|330|3|181|

#### Attribute 3: installation type: *67.2%*

|label distribution|0|1|2|3|4|
|---|---|---|---|---|---|
|sample number|1879|775|28|104|214|

#### Attribute 4: harness type: *65.8%*

|label distribution|0|1|2|3|
|---|---|---|---|---|
|sample number|1798|732|464|6|

#### Attribute 5: material: *36.3%*

|label distribution|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|sample number|944|372|314|820|37|513|

### Conclusion from the breakdown

**Conclusion**: The more dispersed the label distribution, namely the more difficult the attribute task, the worse the performance.

### Investigation & Analysis

We found that the performance relates to the dispersal degree of label distribution, which is equivalent to the difficulty of the attribute task. Below is the analysis of this conclusion.

One of the reasons is that the customer needs text data samples are similar in semantics. We notice that many needs text revolves around some common points, but has very different labels, which implies inconsistency in dataset.

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

Furthermore, we found that several data samples with the same needs text have different label annotation. This is directly threatening data consistency for model learning.

|Needs|Review|attr1|attr2|attr3|attr4|attr5|
|---|---|---|---|---|---|---|
|I need a product that consistently meets my expectations without any flaws.|Perfect|2|4|0|0|1|
|I need a product that consistently meets my expectations without any flaws.|Perfect|2|3|0|0|3|
|I need a product that consistently meets my expectations without any flaws.|Perfect|0|5|0|0|0|
|I need a product that consistently meets my expectations without any flaws.|Perfect|1|4|1|1|0|

**Analysis insight**: In this case, we realize that *directly transforming review text into needs text* can cause a problem. The problem is the generated needs text will become very similar in semantics. In addition, although many data samples have different label annotations, but the needs text of these samples revolves around some common points, incurring **inconsistency** which prevents model from effectively learning.

In this case, it is unlikely for the model to learn effectively because the learning signals are not consistent. Moreover, even the model has learned from the data in the finetuning set, it can be useless to make prediction for test set based on the learned parameters since the similar/same needs text data may correspond to a completely different label annotattion set.

This makes distinguishing the needs text challenging and furthermore, makes *classifying the non-distinguishable needs text into correct attribute specification* very difficult.

**Conclusion**: In summary, the current synthesis method for needs text will lead to *inconsistency* in needs text dataset. The inconsistency in needs text dataset will prevent model from effectively learning. Furthermore, the inconsistency makes the testing result meaningless because the testing result doesn't reflect how well the model has learned (The reason is the data in testing set may contain a similar needs text in finetuning set, but a completely different label from the one in finetuning set).

## Bike
|model(Llama 3B)|Bike Type|Age Range|Wheel Size|Number of Speeds|Brake Style|Frame Material|Suspension Type|
|---|---|---|---|---|---|---|---|
|LoRA|58.6|77.7|66.5|59.7|55.2|70.3|51.6|
|LoRA + soft ensemble|60.0|78.0|66.2|59.8|55.1|70.7|53.4|

## Smart watch

|model(Llama 3B)|Screen Size|Display Type|Battery Life|
|---|---|---|---|
|LoRA|43.1|46.4|66.7|
|LoRA + soft ensemble|44.2|47.5|66.8|


# Progress Record

**2025.12** Develop the data processing framework for adaptation of UCSD review dataset to configurable product recommendation.

**2025.12** Synthsize 3000 customer needs text data for car seat product based on customer review data. Adopt 1500:1500 data for finetuning and test respectively. Finetune Llama-3.2-3B model on car seat dataset.

**2025.12** The results of attribute *seat type* and *material* are obviously lower than the other three attributes. We investigate the reason from the generated needs text data and record the analysis insights in this document. The conclusion is: *directly transforming review text into needs text* makes distinguishing the needs text challenging and furthermore, makes *classifying the non-distinguishable needs text into correct attribute specification* very difficult.

**2025.12** Due to the inconsistency issue occurred during data processing, we propose a new synthesis method to deal with the problem of inconsistency. The design of the new synthesis method is recorded and documented in the "*README.md*" under the directory of "*new_synthesis_needs*".

**2025.12** With the new synthesis method for needs generation, we re-generate the customer needs for car seat product. We run experiments on the newly generated datasets. The experiment results show that the new synthesis method can merely alleviate the inconsistency issue to some extent for some attributes, but cannot entirely solve the inconsistency problem. In this case, we still obtain improvement in overall performance.

**2026.1** To further improve the performance of attribute task of *Weight Range*, we merge the classes in *Weight Range* for car seat product. The class number is reduced from 8 to 3. The merge of classes significantly improved the performance of *Weight Range*, while keeping the other attributes' performance unchange.

**2026.1** Process the data of bike product. The bike product has totally 7 attribute tasks. We adopt the new synthesis method to extract the relevant information in the review text data and leverage LLM to generate the customer needs text based on the relevant information.