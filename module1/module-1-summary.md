# DSC 215: Probability and Statistics for Data Science
## Module 1 Summary: Introduction to Data

## 1. Introduction to Statistics

### What is Statistics?
- **Definition**: A discipline that focuses on the collection, analysis, and interpretation of data
- **Applications**: Used in various fields including:
  - "Hard" Sciences (physics, chemistry, biology)
  - Social Sciences (politics, economics, education)
  - Medicine
  - Business and industry

### Types of Data
- **Numerical Data**: Quantitative measurements
  - **Discrete**: Countable values (e.g., number of students in a class)
  - **Continuous**: Measurements on a continuous scale (e.g., height, weight)
- **Categorical Data**: Qualitative classifications
  - **Nominal**: Categories with no natural ordering (e.g., dog breeds, political party)
  - **Ordinal**: Categories with a natural ordering (e.g., education level, satisfaction ratings)

## 2. Data Organization

### Data Matrix Structure
- **Observations/Cases**: Individual entities being measured (rows in a data matrix)
- **Variables**: Characteristics being measured for each observation (columns)

**Example**: Dog Breed Study
```
| Dog ID | Breed     | Weight (kg) | Height (cm) | Fur Length (cm) |
|--------|-----------|-------------|-------------|-----------------|
| 1      | Husky     | 25          | 58          | 5               |
| 2      | Bulldog   | 22          | 40          | 2               |
| 3      | Chihuahua | 2.5         | 20          | 3               |
```

In this example:
- Each row represents one dog (an observation/case)
- The variables are Breed (categorical), Weight (numerical-continuous), Height (numerical-continuous), and Fur Length (numerical-continuous)
- There are 3 categorical levels for the Breed variable: Husky, Bulldog, and Chihuahua

## 3. Relationships Between Variables

### Types of Associations
- **Positive Association**: Variables increase or decrease together
  - Example: House size and price tend to increase together
- **Negative Association**: One variable increases as the other decreases
  - Example: Homeownership rate decreases as percentage of multi-unit structures increases
- **No Association**: No discernible pattern between variables

### Variable Roles
- **Explanatory Variable**: Variable that might affect or explain changes in another variable
  - Also called independent variable or predictor
- **Response Variable**: Variable that may be affected by the explanatory variable
  - Also called dependent variable or outcome

**Important Note**: Association does not imply causation

### Visualizing Relationships
- **Scatterplots**: Used to visualize relationships between two numerical variables
  - Each point represents a single observation
  - Pattern of points indicates type and strength of relationship

**Example**: Homeownership and Multi-Unit Structures
```
The scatterplot shows a negative association between homeownership rate and 
percentage of multi-unit structures in counties. As the percentage of multi-unit 
structures increases, the homeownership rate tends to decrease.
```

## 4. Data Collection Methods

### Observational Studies
- **Definition**: Data collected without interference in how variables arise
- **Characteristics**:
  - Good for identifying natural associations
  - Cannot establish causation
  - Subject to confounding variables
- **Applications**: Surveys, existing records, cohort studies

### Experiments
- **Definition**: Designed investigations where researchers control variables
- **Characteristics**:
  - Can establish causal connections
  - Involves treatment and control groups
  - Uses randomization to control for confounding variables
- **Key Components**:
  - **Treatment Group**: Receives the intervention being studied
  - **Control Group**: Provides a baseline for comparison

## 5. Sampling Principles

### Population vs. Sample
- **Population**: The entire set of cases about which we want to draw conclusions
- **Sample**: A subset of the population from which we collect data
- **Sampling Frame**: List of cases from which the sample is drawn

### Sampling Methods
- **Simple Random Sampling**: Each case has an equal probability of selection
  - Formula for probability of selection: $P(\text{selection}) = \frac{n}{N}$
  - Where n = sample size, N = population size
- **Stratified Sampling**: Population divided into groups, then random sampling within groups
- **Cluster Sampling**: Population divided into clusters, then entire clusters selected

### Sampling Bias
- **Non-response Bias**: When certain types of subjects are less likely to respond
  - Example: Only 30% of people respond to a survey, potentially skewing results
- **Convenience Sampling**: Using easily accessible subjects (often leads to bias)
  - Example: Surveying only people walking in a particular neighborhood
- **Voluntary Response Bias**: When sample consists of self-selected volunteers
  - Example: Online product reviews typically come from very satisfied or very dissatisfied customers

## 6. Experimental Design

### Key Principles
- **Control**: Managing differences between treatment and control groups
- **Randomization**: Random assignment to account for uncontrollable variables
- **Replication**: Using more cases for better estimation
- **Blocking**: Subdividing based on variables that may affect response

### Reducing Bias in Human Experiments
- **Blind Studies**: Participants unaware of their treatment status
- **Double-Blind Studies**: Both participants and researchers unaware of treatment status
- **Placebos**: Fake treatments given to control groups
  - Helps account for the placebo effect (improvement due to expectation)

### Example of Experimental Design
```
Study: Effect of a sleeping pill on people with trouble sleeping

Design elements:
- 80 participants with trouble sleeping
- Blocking variable: Age (40 people >50 years old, 40 people <50 years old)
- Random assignment within blocks to treatment or control
- Treatment: One sleeping pill per week
- Control: Placebo pill
- Blinding: Participants don't know which pill they received (single-blind)
- Duration: 10 weeks
- Response variable: Quality of sleep
```

## 7. Drawing Valid Conclusions

### Correlation vs. Causation
- Association between variables does not imply causation
- Causation can only be established through well-designed experiments
- Observational studies can suggest but not prove causal relationships

### Generalizability
- Results from a sample can only be generalized to the population it represents
- Random sampling improves generalizability
- External validity refers to how well results apply to other situations

### Example: Valid and Invalid Conclusions
```
Study: Survey of 50 students in a statistics class about voluntary work participation

Valid conclusion: "X% of students in this specific statistics class participate in 
voluntary work."

Invalid conclusion: "Studying statistics causes students to participate in voluntary 
work." (Correlation doesn't imply causation)

Invalid conclusion: "X% of all university students participate in voluntary work." 
(Cannot generalize beyond the specific class)
```

## 8. Key Formulas and Concepts

### Simple Random Sampling
- Each case has equal probability of selection: $P(\text{selection}) = \frac{n}{N}$
- Where n = sample size, N = population size

### Randomization in Experiments
- Random assignment helps ensure treatment and control groups are comparable
- Helps control for confounding variables
- Can be done using random number generators, coin flips, etc.

## 9. Common Misconceptions

1. **Correlation implies causation**: Just because two variables are associated doesn't mean one causes the other.

2. **Larger samples are always better**: While larger samples generally provide more precision, a large biased sample is worse than a small unbiased sample.

3. **Statistical significance equals practical importance**: A statistically significant result may not be practically meaningful.

4. **Anecdotal evidence is reliable**: Individual stories or experiences are not statistically valid evidence.

5. **All studies are equally valid**: The design and methodology of a study greatly affect the validity of its conclusions.