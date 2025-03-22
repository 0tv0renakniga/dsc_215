# DSC 215: Probability and Statistics for Data Science
## Module 9 Summary: Inference for Numerical Data

## 1. Introduction to Inference for Numerical Data

### From Categorical to Numerical Data
- **Previous Modules**: Focused on inference for categorical data
  - Single proportion
  - Difference of two proportions
  - Multiple groups (goodness of fit)
- **This Module**: Focuses on inference for numerical data
  - Single mean
  - Paired data
  - Difference of two means
  - Many means

### Key Differences in Approach

| Categorical Data | Numerical Data |
|------------------|----------------|
| Sample proportion: p̂ | Sample mean: x̄ |
| Population proportion: p | Population mean: μ |
| Normal distribution with SE = √[p(1-p)/n] | t-distribution with SE = s/√n |
| z-statistic | t-statistic |

## 2. The t-Distribution

### Why Use the t-Distribution?
- When working with numerical data, we typically don't know the population standard deviation (σ)
- We must estimate σ using the sample standard deviation (s)
- This additional uncertainty is accounted for by using the t-distribution instead of the normal distribution

### Properties of the t-Distribution
- Always centered at 0 (like the standard normal)
- Parametrized by a single parameter: degrees of freedom (df)
- More spread out than the normal distribution (heavier tails)
- As df increases, the t-distribution approaches the standard normal distribution
- For df > 30, the t-distribution is very similar to the normal distribution

### Degrees of Freedom
- For a single sample: df = n - 1
- For two independent samples: df = min(n₁ - 1, n₂ - 1) (conservative approach)
- Represents the number of independent pieces of information available

## 3. One-Sample t-Confidence Intervals

### Conditions for Valid Inference
1. **Independence**: The sample observations must be independent
   - Satisfied by random sampling from a large population
2. **Normality**: 
   - If n < 30: Data should come from a normally distributed population (or have no outliers)
   - If n ≥ 30: The Central Limit Theorem applies (no extreme outliers)

### Formula for t-Confidence Interval
$$\bar{x} \pm t^*_{df} \times \frac{s}{\sqrt{n}}$$

Where:
- x̄ is the sample mean
- s is the sample standard deviation
- n is the sample size
- t*ᵈᶠ is the critical value from the t-distribution with df degrees of freedom
- df = n - 1

### Steps for Constructing a t-Confidence Interval
1. **Prepare**: Identify or calculate x̄, s, n, and determine the confidence level
2. **Check**: Verify the conditions for using the t-distribution
3. **Calculate**: Compute SE = s/√n and find the critical value t*ᵈᶠ
4. **Conclude**: Construct and interpret the confidence interval

### Example: Height of 18-Year-Olds
A random sample of 25 eighteen-year-olds has a mean height of 67.73 inches with a standard deviation of 2.00 inches.

**Step 1**: We have x̄ = 67.73, s = 2.00, n = 25, and we want a 95% confidence interval.

**Step 2**: The sample is random, and there are no clear outliers, so conditions are satisfied.

**Step 3**: 
- SE = s/√n = 2.00/√25 = 0.4
- df = n - 1 = 25 - 1 = 24
- t*₂₄ = 2.10 (for 95% confidence)

**Step 4**: 
- 95% CI = 67.73 ± 2.10 × 0.4 = 67.73 ± 0.84 = (66.89, 68.57)
- Interpretation: We are 95% confident that the average height of 18-year-olds in the population is between 66.89 and 68.57 inches.

## 4. One-Sample t-Tests

### Hypothesis Testing Framework
- **Null Hypothesis (H₀)**: μ = μ₀ (population mean equals a specific value)
- **Alternative Hypothesis (H₁)**:
  - Two-sided: μ ≠ μ₀
  - Right-tailed: μ > μ₀
  - Left-tailed: μ < μ₀

### Test Statistic
$$T = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}}$$

### Steps for Conducting a One-Sample t-Test
1. **Prepare**: Identify or calculate x̄, s, n, and determine the significance level α
2. **Check**: Verify the conditions for using the t-distribution
3. **Calculate**: Compute the test statistic T and find the p-value
4. **Conclude**: Compare the p-value to α and make a decision

### Example: Sleep Duration of UCSD Students
We want to determine if UCSD students sleep less than 7 hours per night on average. A random sample of 50 students has a mean sleep duration of 6.74 hours with a standard deviation of 0.71 hours.

**Step 1**: We have x̄ = 6.74, s = 0.71, n = 50, and we'll use α = 0.05.

**Step 2**: The sample is random and n ≥ 30, so conditions are satisfied.

**Step 3**: 
- SE = s/√n = 0.71/√50 = 0.1004
- df = n - 1 = 50 - 1 = 49
- T = (6.74 - 7)/0.1004 = -2.59
- p-value = P(T < -2.59) = 0.0063

**Step 4**: 
- Since p-value = 0.0063 < 0.05, we reject H₀
- Conclusion: There is strong evidence that UCSD students sleep less than 7 hours per night on average.

## 5. Paired Data Analysis

### What is Paired Data?
- Two sets of observations are paired if each observation in one set has a special correspondence with exactly one observation in the other set
- Examples:
  - Before and after measurements on the same subjects
  - Measurements on matched pairs (e.g., twins)
  - Prices of the same items at two different stores

### Analyzing Paired Data
- Calculate the differences between paired observations
- Analyze these differences using one-sample t-methods
- The parameter of interest is μd (the mean difference)

### Example: Grocery Store Prices
Comparing prices of the same items at two different grocery stores:

| Item | Whole Foods | Vons | Difference (WF - V) |
|------|-------------|------|---------------------|
| Fuji Apples | $1.89 | $1.49 | $0.40 |
| Whole Milk | $2.49 | $3.99 | -$1.50 |
| Yogurt | $5.89 | $5.99 | -$0.10 |

We would analyze the differences using a one-sample t-test or confidence interval.

## 6. Confidence Intervals for Difference of Means

### Conditions for Valid Inference
1. **Independence (extended)**: 
   - Data are independent within each group
   - Data are independent between groups
   - Satisfied by random sampling or random assignment
2. **Normality**: 
   - If n < 30: Data should come from normally distributed populations
   - If n ≥ 30: The Central Limit Theorem applies

### Formula for Standard Error
$$SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$

### Formula for Confidence Interval
$$({\bar{x}_1 - \bar{x}_2}) \pm t^*_{df} \times SE$$

Where:
- x̄₁ and x̄₂ are the sample means
- s₁ and s₂ are the sample standard deviations
- n₁ and n₂ are the sample sizes
- df = min(n₁ - 1, n₂ - 1) (conservative approach)

### Example: Treatment Effect Study
A small randomized control trial gives the following results for treating a particular condition:

| Group | n | Sample Mean | Sample SD |
|-------|---|-------------|-----------|
| Treatment | 9 | 3.5 | 5.17 |
| Control | 9 | -4.33 | 2.76 |

**Step 1**: We want a 95% confidence interval for the treatment effect.

**Step 2**: The data are from a randomized trial, so independence is satisfied.

**Step 3**: 
- SE = √[(5.17²/9) + (2.76²/9)] = 1.95
- df = min(9-1, 9-1) = 8
- t*₈ = 2.31 (for 95% confidence)
- Point estimate = x̄₁ - x̄₂ = 3.5 - (-4.33) = 7.83

**Step 4**: 
- 95% CI = 7.83 ± 2.31 × 1.95 = 7.83 ± 4.51 = (3.32, 12.34)
- Interpretation: We are 95% confident that the true difference in mean outcomes between the treatment and control groups is between 3.32 and 12.34 units.

## 7. Hypothesis Testing for Difference of Means

### Hypothesis Testing Framework
- **Null Hypothesis (H₀)**: μ₁ - μ₂ = 0 (no difference between population means)
- **Alternative Hypothesis (H₁)**:
  - Two-sided: μ₁ - μ₂ ≠ 0
  - Right-tailed: μ₁ - μ₂ > 0
  - Left-tailed: μ₁ - μ₂ < 0

### Test Statistic
$$T = \frac{(\bar{x}_1 - \bar{x}_2) - 0}{SE}$$

### Example: Birth Weight and Smoking
A study investigates whether newborns from mothers who smoke have different average birth weights than newborns from mothers who don't smoke.

| Group | n | Sample Mean | Sample SD |
|-------|---|-------------|-----------|
| Non-smoker | 100 | 7.18 | 1.6 |
| Smoker | 50 | 6.78 | 1.43 |

**Step 1**: We have α = 0.05.

**Step 2**: The data come from a random sample, and n ≥ 30 for both groups, so conditions are satisfied.

**Step 3**: 
- Point estimate = x̄ₙ - x̄ₛ = 7.18 - 6.78 = 0.4
- SE = √[(1.6²/100) + (1.43²/50)] = 0.26
- T = 0.4/0.26 = 1.54
- df = min(100-1, 50-1) = 49
- p-value = P(|T| ≥ 1.54) = 0.1304

**Step 4**: 
- Since p-value = 0.1304 > 0.05, we fail to reject H₀
- Conclusion: There is not enough evidence to conclude that there is a difference in average birth weight between newborns from mothers who smoke and those who don't.

## 8. Statistical Power for Difference of Means

### Definition of Statistical Power
- The probability of correctly rejecting the null hypothesis when a specific alternative hypothesis is true
- Mathematically: power = P(reject H₀ | H₁ is true)
- Equivalently: power = 1 - P(Type II error)

### Factors Affecting Power
1. **Sample size**: Larger samples increase power
2. **Effect size**: Larger differences are easier to detect
3. **Variability**: Less variability increases power
4. **Significance level**: Higher α increases power (but also increases Type I error risk)

### Calculating Power
1. Determine the rejection region under H₀
2. Calculate the probability of falling in the rejection region under H₁

### Example: Blood Pressure Medication
A study is designed to test if a new blood pressure medication reduces blood pressure compared to a standard medication. We want to detect a difference of 3 mmHg.

- Sample size: n₁ = n₂ = 100
- Estimated standard deviation: s₁ = s₂ = 12
- Significance level: α = 0.05

**Step 1**: Calculate the standard error
- SE = √[(12²/100) + (12²/100)] = 1.7

**Step 2**: Determine the rejection region
- For α = 0.05 (two-sided), reject H₀ if |T| > 1.96
- This corresponds to x̄₁ - x̄₂ < -3.332 or x̄₁ - x̄₂ > 3.332

**Step 3**: Calculate power for detecting a 3 mmHg reduction
- Under H₁, x̄₁ - x̄₂ follows approximately N(-3, 1.7²)
- Power = P(x̄₁ - x̄₂ < -3.332 | μ₁ - μ₂ = -3)
- Z = (-3.332 - (-3))/1.7 = -0.2
- Power = P(Z < -0.2) = 0.42 or 42%

**Step 4**: Determine sample size for 80% power
- For 80% power, we need Z = 0.84
- Distance between means = 2.8 × SE = 3
- 2.8 × √[(12²/n) + (12²/n)] = 3
- Solving for n: n = 251 per group

## 9. Common Misconceptions and Pitfalls

### Misconception 1: t-Distribution vs. Normal Distribution
- **Misconception**: The t-distribution is always very different from the normal distribution
- **Reality**: For large degrees of freedom (df > 30), the t-distribution is very similar to the normal distribution

### Misconception 2: Paired vs. Independent Samples
- **Misconception**: Any comparison of two groups should use the two-sample t-test
- **Reality**: Paired data should be analyzed using paired methods (one-sample t-test on differences)

### Pitfall 1: Ignoring Conditions
- **Problem**: Using t-methods when conditions are not satisfied
- **Solution**: Always check independence and normality conditions

### Pitfall 2: Misinterpreting p-values
- **Problem**: Interpreting a non-significant result as "proving" the null hypothesis
- **Solution**: A non-significant result only means there is insufficient evidence to reject H₀

## 10. Key Takeaways

1. **t-Distribution**:
   - Used when the population standard deviation is unknown
   - Accounts for the additional uncertainty from estimating σ with s
   - Approaches the normal distribution as sample size increases

2. **One-Sample Inference**:
   - Confidence interval: x̄ ± t*ᵈᶠ × (s/√n)
   - Hypothesis test: T = (x̄ - μ₀)/(s/√n)
   - Degrees of freedom: df = n - 1

3. **Paired Data**:
   - Analyze the differences between paired observations
   - Use one-sample methods on these differences

4. **Two-Sample Inference**:
   - Confidence interval: (x̄₁ - x̄₂) ± t*ᵈᶠ × SE
   - Hypothesis test: T = (x̄₁ - x̄₂)/SE
   - Standard error: SE = √[(s₁²/n₁) + (s₂²/n₂)]
   - Degrees of freedom: df = min(n₁ - 1, n₂ - 1) (conservative approach)

5. **Statistical Power**:
   - The probability of correctly rejecting H₀ when H₁ is true
   - Increases with larger sample sizes, larger effect sizes, and higher significance levels
   - Important for study design and sample size determination