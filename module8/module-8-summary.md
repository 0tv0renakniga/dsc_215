# DSC 215: Probability and Statistics for Data Science
## Module 8 Summary: Goodness of Fit Tests

## 1. Introduction to Goodness of Fit Tests

### Purpose and Applications
- **Definition**: Statistical procedures that determine whether observed data conform to a theoretical distribution or expected frequencies
- **Applications**:
  - Testing if a sample is representative of a population
  - Determining if data follow a particular distribution (e.g., normal, binomial)
  - Evaluating whether observed frequencies match expected frequencies
  - Assessing whether categorical variables are distributed as expected

### Types of Goodness of Fit Tests
- **One-Way Chi-Square Test**: Tests if observed frequencies in a single categorical variable match expected frequencies
- **Chi-Square Test for Independence**: Tests if two categorical variables are related (covered in later modules)
- **Kolmogorov-Smirnov Test**: Tests if a sample comes from a specific continuous distribution (not covered in this module)

## 2. The Chi-Square Distribution

### Definition and Properties
- **Definition**: The distribution of a sum of squares of independent standard normal random variables
- **Formula**: If Z₁, Z₂, ..., Zₖ are independent standard normal random variables, then:
  $$\chi^2_k = Z_1^2 + Z_2^2 + ... + Z_k^2$$
  follows a chi-square distribution with k degrees of freedom

- **Properties**:
  - Always non-negative (sum of squared values)
  - Right-skewed, especially with low degrees of freedom
  - Becomes more symmetric and approximately normal as degrees of freedom increase
  - Mean equals the degrees of freedom
  - Variance equals twice the degrees of freedom

### Degrees of Freedom
- **Definition**: The number of values that are free to vary in the calculation of a statistic
- **Interpretation**: In a chi-square test, degrees of freedom = (number of categories - 1)
- **Reason**: When we know the total sample size and all but one category count, the final count is determined

### Example: Reading Chi-Square Tables
For a chi-square distribution with 3 degrees of freedom, the probability that the chi-square value exceeds 6.25 is:
$$P(\chi^2_3 \geq 6.25) \approx 0.1001$$

This means that if we have a chi-square test statistic of 6.25 with 3 degrees of freedom, the p-value would be approximately 0.1001.

## 3. Chi-Square Goodness of Fit Test

### Test Statistic
- **Formula**:
  $$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$
  where:
  - Oᵢ = Observed count in category i
  - Eᵢ = Expected count in category i under the null hypothesis
  - k = Number of categories

- **Interpretation**: Measures the discrepancy between observed and expected frequencies
  - Larger values indicate greater discrepancy
  - Values close to zero suggest good fit

### Hypothesis Testing Framework
- **Null Hypothesis (H₀)**: The observed frequencies match the expected frequencies (or the data follow the specified distribution)
- **Alternative Hypothesis (H₁)**: The observed frequencies do not match the expected frequencies (or the data do not follow the specified distribution)
- **Decision Rule**: Reject H₀ if p-value < α (significance level)

### Conditions for Valid Chi-Square Test
1. **Independence**:
   - Observations must be independent of each other
   - Satisfied by random sampling or random assignment

2. **Sample Size**:
   - Each expected count must be at least 5
   - Ensures the chi-square approximation is valid

## 4. Testing for Specific Distributions

### Testing Categorical Distributions
- **Example**: Testing if jurors represent the racial demographics of registered voters
- **Procedure**:
  1. Calculate expected counts based on population proportions
  2. Compare observed counts to expected counts using chi-square statistic
  3. Determine p-value using chi-square distribution with (k-1) degrees of freedom

### Testing Probability Distributions
- **Example**: Testing if dice are fair
- **Procedure**:
  1. Determine the theoretical probabilities under the null hypothesis
  2. Calculate expected counts by multiplying probabilities by total sample size
  3. Compare observed counts to expected counts using chi-square statistic
  4. Determine p-value using chi-square distribution with appropriate degrees of freedom

### Binning Continuous Data
- For continuous distributions, data must be binned (grouped into categories)
- Bins should be chosen to ensure expected counts ≥ 5 in each bin
- Test is sensitive to choice of bins, but reasonable choices should yield similar results

## 5. Detailed Examples

### Example 1: Jury Representation Test

A random sample of 275 jurors from a small county had jurors identify their racial group. We want to test if the sample is representative of the population of registered voters.

| Race | White | Black | Hispanic | Other | Total |
|------|-------|-------|----------|-------|-------|
| On Juries (observed) | 205 | 26 | 25 | 19 | 275 |
| Registered Voters (proportion) | 0.72 | 0.07 | 0.12 | 0.09 | 1.00 |
| Expected Counts | 198 | 19.25 | 33 | 24.75 | 275 |

**Step 1**: State hypotheses
- H₀: The jurors are a random sample (no racial bias)
- H₁: The jurors are not a random sample (racial bias exists)

**Step 2**: Calculate expected counts
- Expected White jurors: 275 × 0.72 = 198
- Expected Black jurors: 275 × 0.07 = 19.25
- Expected Hispanic jurors: 275 × 0.12 = 33
- Expected Other jurors: 275 × 0.09 = 24.75

**Step 3**: Calculate Z-scores for each category
- Z₁ (White): (205 - 198)/√198 = 0.5
- Z₂ (Black): (26 - 19.25)/√19.25 = 1.54
- Z₃ (Hispanic): (25 - 33)/√33 = -1.39
- Z₄ (Other): (19 - 24.75)/√24.75 = -1.16

**Step 4**: Calculate chi-square statistic
$$\chi^2 = (0.5)^2 + (1.54)^2 + (-1.39)^2 + (-1.16)^2 = 5.8993$$

**Step 5**: Determine degrees of freedom and p-value
- Degrees of freedom = 4 - 1 = 3
- P-value = P(χ²₃ ≥ 5.8993) ≈ 0.1116

**Step 6**: Make decision
- Since p-value = 0.1116 > 0.05, we fail to reject H₀
- Conclusion: There is insufficient evidence of racial bias in juror selection

### Example 2: Testing if Dice are Fair

A player rolls two dice 200 times and records the number of sixes that appear on each roll:

| Number of Sixes | 0 | 1 | 2 | Total |
|-----------------|---|---|---|-------|
| Observed Count | 130 | 58 | 12 | 200 |

**Step 1**: State hypotheses
- H₀: The dice are fair
- H₁: The dice are not fair

**Step 2**: Calculate expected probabilities under H₀
- P(0 sixes) = (5/6)² = 25/36 ≈ 0.6944
- P(1 six) = 2 × (1/6) × (5/6) = 10/36 ≈ 0.2778
- P(2 sixes) = (1/6)² = 1/36 ≈ 0.0278

**Step 3**: Calculate expected counts
- Expected count for 0 sixes: 200 × 25/36 = 138.889
- Expected count for 1 six: 200 × 10/36 = 55.556
- Expected count for 2 sixes: 200 × 1/36 = 5.556

**Step 4**: Calculate chi-square statistic
$$\chi^2 = \frac{(130-138.889)^2}{138.889} + \frac{(58-55.556)^2}{55.556} + \frac{(12-5.556)^2}{5.556} \approx 8.15$$

**Step 5**: Determine degrees of freedom and p-value
- Degrees of freedom = 3 - 1 = 2
- P-value = P(χ²₂ ≥ 8.15) ≈ 0.017

**Step 6**: Make decision
- Since p-value = 0.017 < 0.05, we reject H₀
- Conclusion: There is evidence that the dice are not fair
- Note: Looking at the data, we can see more 2's (double sixes) than expected, suggesting the dice might be biased toward sixes

### Example 3: Hospital Check-ins by Weekday

A hospital administrator wants to find out if patient check-ins are evenly distributed across weekdays. They randomly sample 210 records:

| Day | Monday | Tuesday | Wednesday | Thursday | Friday | Total |
|-----|--------|---------|-----------|----------|--------|-------|
| Observed Count | 32 | 40 | 36 | 45 | 57 | 210 |

**Step 1**: State hypotheses
- H₀: Check-ins are evenly distributed across weekdays
- H₁: Check-ins are not evenly distributed across weekdays

**Step 2**: Calculate expected counts under H₀
- Expected count for each day: 210 ÷ 5 = 42

**Step 3**: Calculate chi-square statistic
$$\chi^2 = \frac{(32-42)^2}{42} + \frac{(40-42)^2}{42} + \frac{(36-42)^2}{42} + \frac{(45-42)^2}{42} + \frac{(57-42)^2}{42} \approx 9.29$$

**Step 4**: Determine degrees of freedom and p-value
- Degrees of freedom = 5 - 1 = 4
- P-value = P(χ²₄ ≥ 9.29) ≈ 0.054

**Step 5**: Make decision
- Since p-value = 0.054 > 0.05, we fail to reject H₀
- Conclusion: There is insufficient evidence that patient check-ins are unevenly distributed across weekdays

## 6. Common Misconceptions and Pitfalls

### Misconception 1: Chi-Square Tests Prove the Null Hypothesis
- Correct understanding: Failing to reject H₀ does not prove that the observed data follow the expected distribution; it only means we lack evidence to conclude otherwise

### Misconception 2: Chi-Square Tests Work with Small Samples
- Correct understanding: Chi-square tests require expected counts of at least 5 in each category for valid results

### Pitfall 1: Inappropriate Binning
- Problem: Results can vary based on how continuous data is binned
- Solution: Use consistent, reasonable binning strategies and ensure expected counts ≥ 5 in each bin

### Pitfall 2: Ignoring Independence Assumption
- Problem: Non-independent observations can lead to invalid results
- Solution: Ensure random sampling or appropriate experimental design

## 7. Key Takeaways

1. **Chi-Square Goodness of Fit Test**:
   - Tests whether observed frequencies match expected frequencies
   - Uses the chi-square statistic: χ² = Σ[(Oᵢ - Eᵢ)²/Eᵢ]
   - Larger values indicate greater discrepancy between observed and expected

2. **Chi-Square Distribution**:
   - Right-skewed distribution that approaches normal as degrees of freedom increase
   - Used to determine p-values for chi-square test statistics
   - Degrees of freedom = number of categories - 1

3. **Conditions for Valid Chi-Square Test**:
   - Independence of observations
   - Expected count ≥ 5 in each category

4. **Applications**:
   - Testing if a sample represents a population
   - Testing if data follow a specific distribution
   - Testing if categorical data are distributed as expected

5. **Interpretation**:
   - Small p-values (< α) suggest the observed data do not match the expected distribution
   - Large p-values (≥ α) suggest insufficient evidence to conclude the data don't match the expected distribution