# New Synthesis Method for Needs

## 4-stage synthesis method

### Stage 1: Review length distribution analysis & Filter

output file of stage 1: *reviews_more_than_40_words.csv*

### Stage 2: Stratified shuffling and spliting

outputfile of stage 2: *reviews_more_than_40_words_3000_stratified.csv*

### Stage 3: Extract attribute-related information

**Attempt 1**: List the names of attributes only in the prompts.

**Result of Attempt 1**: Misunderstanding and hallucination occurs for some unclear attributes such as *Seat Type* and *Weight Range*.

**Attempt 2**: Attach several specification examples for the unclear attributes that need further clarification such as *Seat Type* and *Installation Type*.

**Result of Attempt 2**: Eliminate the misunderstanding and hallucination to great extent.

outputfile of stage 3: *reviews_40+_words_strat_shuffle_split_3k.csv*

### Stage 4: Needs synthesis based on relevant information

For positive information, express them directly as customer needs.

**Attempt 1**:

**Implication of Attempt 1**:
Inconsistency occurs if the needs directly fixes/solves the drawbacks or issues corresponding to the negative information. This is because the product actually has the negative drawbacks or issues, so the needs for the product should reflect or admit the drawbacks or issues instead of denying(fixing/solving) it.

**Attempt 2**:
For negative information, express them as customer needs indicating that these issues are acceptable or tolerable.

**Implication of Attempt 2**:
Eliminate the inconsistency since the needs admits the existence of the drawbacks or issues and states that they are acceptable and tolerable. In this case, the needs can consistently match the product with the negative drawbacks or issues.

outputfile of stage 3: *processed_reviews_with_needs.csv*