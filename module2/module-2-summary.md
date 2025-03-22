# DSC 215: Probability and Statistics for Data Science
## Module 2 Summary: Summarizing Data

## 1. Visualizing Numerical Data

### Scatterplots
- **Purpose**: Visualize relationships between two numerical variables
- **Features**:
  - Each point represents a single case with coordinates (x, y)
  - Help identify associations (positive, negative, or none)
  - Reveal whether relationships are simple (linear) or complex (non-linear)
- **Example**: A scatterplot of total income versus loan amount shows that borrowers with higher incomes tend to take larger loans, though the relationship isn't perfectly linear.

### Histograms
- **Purpose**: Visualize the distribution of a single numerical variable
- **Features**:
  - Data values are grouped into bins (intervals)
  - Height of bars represents frequency or density
  - Higher bars indicate where data are more common
  - Provide a view of data density across the range of values
- **Example**: A histogram of interest rates for loans might show that most loans have rates between 5-10%, with fewer loans having rates above 15%.

## 2. Shape of Distributions

### Skewness
- **Right-skewed (Positively Skewed)**:
  - Data trail off to the right with a longer right tail
  - Mean is typically greater than median
  - Example: Income distributions, home prices
  
- **Left-skewed (Negatively Skewed)**:
  - Data trail off to the left with a longer left tail
  - Mean is typically less than median
  - Example: Age-at-death distributions, exam scores with ceiling effects
  
- **Symmetric**:
  - Data show roughly equal trailing off in both directions
  - Mean and median are approximately equal
  - Example: Height distributions in adult populations

### Modality
- **Unimodal**: One prominent peak (most common)
- **Bimodal**: Two prominent peaks (suggests two subpopulations)
- **Multimodal**: More than two prominent peaks
- **Uniform**: No peaks, approximately equal frequency across all values

## 3. Measures of Center

### Mean (Average)
- **Definition**: Sum of all values divided by number of observations
- **Formula**: 
  $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \ldots + x_n}{n}$$
- **Properties**:
  - Useful for comparisons between groups
  - Affected by all values in the dataset
  - Not resistant to outliers (non-robust)
  - Appropriate for symmetric distributions
- **Example**: For interest rates of 10.9%, 9.92%, ..., 6.08% across 50 loans, the mean is 11.57%.

### Median
- **Definition**: Middle value when data are ordered
- **Calculation**:
  - If n is odd: middle value
  - If n is even: average of two middle values
- **Properties**:
  - Robust statistic (resistant to outliers)
  - Better measure of center for skewed distributions
  - Not affected by extreme values
- **Example**: For the ordered data {1, 5, 6, 7, 10}, the median is 6. For {1, 5, 6, 7}, the median is (5+6)/2 = 5.5.

### Mode
- **Definition**: Value with a prominent peak in the distribution
- **Properties**:
  - Can have multiple modes
  - Useful for categorical data
  - Less commonly used for numerical data
- **Example**: In the dataset {2, 3, 3, 4, 5, 5, 5, 6, 7}, the mode is 5.

## 4. Measures of Spread

### Variance
- **Definition**: Average squared deviation from the mean
- **Formula**: 
  $$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$
- **Properties**:
  - Measures how much data deviates from the mean
  - Units are squared (making interpretation difficult)
  - Not resistant to outliers
- **Example**: For the data {2, 4, 6, 8, 10}, the mean is 6, and the variance is:
  $$s^2 = \frac{(2-6)^2 + (4-6)^2 + (6-6)^2 + (8-6)^2 + (10-6)^2}{5-1} = \frac{16 + 4 + 0 + 4 + 16}{4} = \frac{40}{4} = 10$$

### Standard Deviation
- **Definition**: Square root of variance
- **Formula**: 
  $$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$
- **Properties**:
  - Same units as original data
  - Useful for considering how far data are distributed from the mean
  - Approximately 68% of data falls within 1 standard deviation of mean in normal distributions
  - Not resistant to outliers
- **Example**: For the data {2, 4, 6, 8, 10}, the standard deviation is $\sqrt{10} = 3.16$.

### Range
- **Definition**: Difference between maximum and minimum values
- **Formula**: Range = max(x) - min(x)
- **Properties**:
  - Simple to calculate
  - Highly sensitive to outliers
  - Provides limited information about distribution
- **Example**: For the data {2, 4, 6, 8, 10}, the range is 10 - 2 = 8.

### Quartiles and IQR
- **First quartile (Q₁)**: 25% of data falls below this value
- **Second quartile (Q₂)**: Median (50% of data falls below)
- **Third quartile (Q₃)**: 75% of data falls below this value
- **Interquartile Range (IQR)**: Q₃ - Q₁ (range of middle 50% of data)
- **Properties**:
  - Robust statistics (resistant to outliers)
  - Useful for describing skewed distributions
  - Used to identify potential outliers
- **Example**: For the data {2, 4, 6, 8, 10, 12, 14}, Q₁ = 4, Q₂ = 8, Q₃ = 12, and IQR = 12 - 4 = 8.

## 5. Box Plots and Outliers

### Box Plots
- **Components**:
  - Box: Represents IQR (middle 50% of data)
  - Line inside box: Median
  - Whiskers: Extend to smallest/largest data points within 1.5×IQR of Q₁/Q₃
  - Individual points: Potential outliers beyond whiskers
- **Uses**:
  - Comparing distributions across groups
  - Identifying skewness and outliers
  - Summarizing key statistics visually

### Outliers
- **Definition**: Observations that appear extreme relative to the rest of the data
- **Common identification method**: Values beyond Q₁-1.5×IQR or Q₃+1.5×IQR
- **Importance**:
  - May indicate data collection or recording errors
  - Could represent important rare events
  - Can significantly affect non-robust statistics
  - Should be investigated, not automatically removed

## 6. Summarizing Categorical Data

### Tables for Categorical Data
- **Frequency Tables**: Count occurrences of each category
- **Relative Frequency Tables**: Show proportion or percentage in each category
- **Contingency Tables**: Summarize data for two categorical variables
  - Each cell represents the number of times a particular combination occurred
  - Can be modified to show proportions (row, column, or overall)

### Example of a Contingency Table
```
                 homeownership
                 rent  mortgage  own   Total
app_type individual 3496   3839    1170  8505
         joint      362    950     183   1495
         Total     3858   4789    1353  10000
```

### Row and Column Proportions
- **Row proportions**: Each count divided by its row total
  - Example: 3496/8505 = 0.411 (41.1% of individual applicants rent)
- **Column proportions**: Each count divided by its column total
  - Example: 3496/3858 = 0.906 (90.6% of renters applied as individuals)

### Visualizing Categorical Data
- **Bar Plots**:
  - Display counts or proportions for categories
  - Bars should be separated (unlike histograms)
  - Height represents frequency or proportion
- **Variations**:
  - Stacked bar plots: Show composition within categories
  - Side-by-side bar plots: Compare groups directly
  - Standardized stacked bar plots: Show proportions within each category

## 7. Comparing Distributions

### Comparing Numerical Data Across Groups
- **Side-by-side Box Plots**:
  - Traditional tool for comparing distributions across groups
  - Allow comparison of center, spread, and outliers
- **Hollow Histograms**:
  - Outlines of histograms for each group on the same plot
  - Useful for comparing shapes of distributions

### Comparing Categorical Data Across Groups
- **Side-by-side Bar Plots**: Compare frequencies across groups
- **Stacked Bar Plots**: Compare composition within categories
- **Mosaic Plots**: Area represents frequency in contingency tables

## 8. Statistical Transformations

### Linear Transformations
- **Adding a constant (x + c)**:
  - Changes center but not spread
  - Mean increases by the constant: $\bar{x}_{new} = \bar{x} + c$
  - Median increases by the constant: $\text{median}_{new} = \text{median} + c$
  - Range and standard deviation remain unchanged
  - Example: Converting Celsius to Fahrenheit (F = C + 32)

- **Multiplying by a constant (c × x)**:
  - Changes both center and spread
  - Mean is multiplied by the constant: $\bar{x}_{new} = c \times \bar{x}$
  - Median is multiplied by the constant: $\text{median}_{new} = c \times \text{median}$
  - Range and standard deviation are multiplied by |c|
  - Example: Converting inches to centimeters (cm = 2.54 × inches)

### Example of Transformations
For the data {10, 20, 30, 40, 50}:
- Original: mean = 30, median = 30, range = 40, standard deviation ≈ 15.81
- After adding 5: {15, 25, 35, 45, 55}
  - New mean = 35, new median = 35, range = 40, standard deviation ≈ 15.81
- After multiplying by 2: {20, 40, 60, 80, 100}
  - New mean = 60, new median = 60, range = 80, standard deviation ≈ 31.62

## 9. Practical Examples

### Example 1: Analyzing Loan Interest Rates
A dataset contains interest rates for 50 loans with the following statistics:
- Mean: 11.57%
- Median: 9.93%
- Standard Deviation: 5.05%
- Range: 21.9% (from 5% to 26.9%)
- Q₁: 7.5%
- Q₃: 15%
- IQR: 7.5%

The histogram shows a right-skewed distribution, indicating that most loans have rates under 15%, with a few loans having rates above 20%. Since the distribution is skewed, the median (9.93%) is a better measure of central tendency than the mean (11.57%).

### Example 2: Comparing Student Quiz Scores
A class of students took a quiz, and the 5-number summaries are given for 18 freshmen and 15 sophomores:

```
Summary   Min  Q1   Median  Q3   Max
Freshmen   3   4.5   6.5    8.5  9.5
Sophomores 4   6     7.5    9    10
```

Observations:
- Sophomores have the highest score (10 > 9.5)
- Freshmen have a greater range (6.5 > 6)
- Freshmen have a greater IQR (4 > 3)
- If the mean of freshmen scores is 6.5 and sophomores is 7, the overall mean is:
  $$\text{Overall Mean} = \frac{6.5 \times 18 + 7 \times 15}{33} = \frac{117 + 105}{33} = \frac{222}{33} = 6.73$$

### Example 3: Effect of Salary Changes on Statistics
If an employee with the lowest salary in a company of three employees becomes part-time and has a salary reduction:

- **Effect on measures of center**:
  - Mean will decrease
  - Median will not change (since the lowest value remains the lowest)
  
- **Effect on measures of spread**:
  - Range will increase
  - Standard deviation will increase (the data points become more spread out from the mean)
  - IQR may not change (depends on whether the lowest salary is below Q₁)

## 10. Key Takeaways

1. Different statistics are appropriate for different types of data and distributions:
   - For skewed distributions, median is often more representative than mean
   - For symmetric distributions, mean and median are similar

2. Robust statistics (median, IQR) are less affected by outliers than non-robust statistics (mean, standard deviation)

3. Visualizations help identify patterns and outliers in data:
   - Histograms show the shape of distributions
   - Box plots summarize key statistics and identify outliers
   - Scatterplots show relationships between variables

4. Categorical data requires different analysis approaches than numerical data:
   - Contingency tables and bar plots for categorical data
   - Proportions often more informative than raw counts

5. When comparing groups, consider both measures of center and spread:
   - Side-by-side box plots or hollow histograms for numerical comparisons
   - Stacked or side-by-side bar plots for categorical comparisons

6. Transformations affect statistics in predictable ways:
   - Adding a constant shifts the center but doesn't change the spread
   - Multiplying by a constant changes both center and spread