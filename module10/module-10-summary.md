# DSC 215: Probability and Statistics for Data Science
## Module 10 Summary: Comparing Many Means with ANOVA

## 1. Introduction to ANOVA

### What is ANOVA?
- **Definition**: Analysis of Variance (ANOVA) is a statistical method used to compare means across multiple groups
- **Purpose**: Tests whether there are significant differences between the means of three or more independent groups
- **Advantage over Multiple t-tests**: 
  - Reduces the risk of Type I errors that would accumulate when conducting multiple pairwise comparisons
  - If you have k groups, you would need k(k-1)/2 pairwise comparisons, increasing the chance of finding differences by random chance

### Hypothesis Framework
- **Null Hypothesis (H₀)**: All population means are equal
  $$H_0: \mu_1 = \mu_2 = \ldots = \mu_k$$
- **Alternative Hypothesis (H₁)**: At least one population mean is different from the others
  $$H_1: \mu_i \neq \mu_j \text{ for some } i \neq j$$

## 2. Conditions for Valid ANOVA

### Three Key Conditions
1. **Independence**: 
   - Observations are independent within each group
   - Observations are independent across groups
   - Typically satisfied by random sampling or random assignment

2. **Normality**: 
   - The data within each group is approximately normally distributed
   - Less critical for larger sample sizes due to the Central Limit Theorem
   - Can be assessed using histograms, Q-Q plots, or formal tests

3. **Variability** (Homogeneity of Variance): 
   - The variability across groups is approximately equal
   - Can be assessed by comparing standard deviations or using formal tests like Levene's test
   - ANOVA is somewhat robust to violations of this assumption when sample sizes are equal

## 3. The F-Statistic and F-Distribution

### The Basic Idea
- ANOVA compares two sources of variation:
  - **Between-group variation**: Variation of group means around the overall mean
  - **Within-group variation**: Variation of individual observations around their group means
- If the between-group variation is large relative to the within-group variation, we have evidence that the group means differ

### The F-Statistic
- **Formula**:
  $$F = \frac{\text{Mean Square Between Groups (MSG)}}{\text{Mean Square Error (MSE)}}$$

- **Mean Square Between Groups (MSG)**:
  $$\text{MSG} = \frac{1}{k-1} \sum_{i=1}^{k} n_i(\bar{x}_i - \bar{x})^2$$
  where:
  - k = number of groups
  - n_i = sample size of group i
  - $\bar{x}_i$ = sample mean of group i
  - $\bar{x}$ = overall sample mean

- **Mean Square Error (MSE)**:
  $$\text{MSE} = \frac{1}{n-k} \left( \sum_{i=1}^{n} (x_i - \bar{x})^2 - \sum_{i=1}^{k} n_i(\bar{x}_i - \bar{x})^2 \right)$$
  where n = total sample size

### The F-Distribution
- The F-distribution is parametrized by two degrees of freedom:
  - **df₁** = k - 1 (degrees of freedom for MSG)
  - **df₂** = n - k (degrees of freedom for MSE)
- Properties:
  - Always non-negative (ratio of variances)
  - Right-skewed, especially with low degrees of freedom
  - Becomes less skewed as degrees of freedom increase
  - Under H₀, the F-statistic follows an F-distribution with df₁ and df₂ degrees of freedom

## 4. Conducting an ANOVA Test

### Step-by-Step Procedure
1. **Prepare**: Identify the groups and collect data
2. **Check**: Verify the conditions for ANOVA
3. **Calculate**: Compute the F-statistic
4. **Conclude**: Determine the p-value and make a decision

### Example: Course Delivery Methods
A professor taught the same class in three different formats (remote, hybrid, and in-person) and wants to know if the mean final scores differ. Here are the scores:

| Remote | Hybrid | In-person |
|--------|--------|-----------|
| 80     | 94     | 78        |
| 84     | 85     | 83        |
| 90     | 87     | 93        |
| 84     | 90     | 81        |
| 89     | 76     | -         |
| -      | 89     | -         |
| **Mean** | **85.4** | **89.0** | **83.3** |

**Step 1**: Check conditions
- Independence: Assume students were randomly assigned to different formats
- Normality: Sample sizes are small, but assume scores within each group are approximately normal
- Variability: The standard deviations appear comparable across groups

**Step 2**: Calculate the overall mean
- $\bar{x} = \frac{5(85.4) + 6(89.0) + 4(83.3)}{5+6+4} = \frac{1278.8}{15} = 85.25$

**Step 3**: Calculate MSG
- MSG = $\frac{1}{3-1} [5(85.4-85.25)^2 + 6(89.0-85.25)^2 + 4(83.3-85.25)^2]$
- MSG = $\frac{1}{2} [5(0.15)^2 + 6(3.75)^2 + 4(-1.95)^2]$
- MSG = $\frac{1}{2} [0.1125 + 84.375 + 15.21]$
- MSG = $\frac{99.6975}{2} = 49.85$

**Step 4**: Calculate MSE
- First, calculate the sum of squares within each group:
  - Remote: $(80-85.4)^2 + (84-85.4)^2 + (90-85.4)^2 + (84-85.4)^2 + (89-85.4)^2 = 102.8$
  - Hybrid: $(94-89.0)^2 + (85-89.0)^2 + (87-89.0)^2 + (90-89.0)^2 + (76-89.0)^2 + (89-89.0)^2 = 234.0$
  - In-person: $(78-83.3)^2 + (83-83.3)^2 + (93-83.3)^2 + (81-83.3)^2 = 146.75$
- Total within-group sum of squares = 102.8 + 234.0 + 146.75 = 483.55
- MSE = $\frac{483.55}{15-3} = \frac{483.55}{12} = 40.30$

**Step 5**: Calculate the F-statistic
- F = $\frac{MSG}{MSE} = \frac{49.85}{40.30} = 1.24$

**Step 6**: Determine the p-value
- df₁ = 3 - 1 = 2
- df₂ = 15 - 3 = 12
- Using an F-distribution table or software: p-value = P(F ≥ 1.24) ≈ 0.32

**Step 7**: Make a decision
- Since p-value = 0.32 > 0.05, we fail to reject H₀
- Conclusion: There is insufficient evidence to conclude that the mean final scores differ across the three teaching formats

## 5. Multiple Comparisons

### The Multiple Comparisons Problem
- If ANOVA rejects H₀, we know that at least one mean differs, but we don't know which ones
- To identify specific differences, we need to conduct pairwise comparisons
- However, conducting multiple tests increases the risk of Type I errors (false positives)

### Bonferroni Correction
- **Purpose**: Controls the overall Type I error rate when conducting multiple comparisons
- **Adjusted Significance Level**:
  $$\alpha^* = \frac{\alpha}{K}$$
  where K = k(k-1)/2 is the number of pairwise comparisons

- **Justification**: By the union bound in probability theory:
  $$\mathbb{P}\left( \bigcup_{i=1}^{K} (p_i \leq \alpha/K) \right) \leq \sum_{i=1}^{K} \mathbb{P}(p_i \leq \alpha/K) \leq \alpha$$

### Example: Pairwise Comparisons with Bonferroni Correction
Suppose ANOVA indicates significant differences among four groups (A, B, C, D) with α = 0.05.

**Step 1**: Calculate the number of pairwise comparisons
- K = 4(4-1)/2 = 6 comparisons (A-B, A-C, A-D, B-C, B-D, C-D)

**Step 2**: Calculate the adjusted significance level
- α* = 0.05/6 = 0.0083

**Step 3**: Conduct pairwise t-tests
- For each pair, calculate the t-statistic and p-value
- Compare each p-value to α* = 0.0083
- Only pairs with p-values < 0.0083 are considered significantly different

### Important Note
- It is possible to reject the null hypothesis in ANOVA but not find significant differences in any pairwise comparisons
- This does not invalidate the ANOVA result
- It simply means we cannot identify which specific groups differ with the given sample sizes

## 6. Practical Example: Travel Routes

A student is interested in the times it takes (in minutes) to get to campus using three different routes. She wants to test whether the mean times are equal.

| Route 1 | Route 2 | Route 3 |
|---------|---------|---------|
| 30      | 27      | 16      |
| 32      | 29      | 41      |
| 27      | 28      | 22      |
| 35      | 36      | 31      |
| **Mean** | **31.0** | **30.0** | **27.5** |

**Step 1**: State hypotheses
- H₀: μ₁ = μ₂ = μ₃ (mean travel times are equal across routes)
- H₁: At least one mean is different

**Step 2**: Check conditions (assume all conditions are met)

**Step 3**: Calculate the overall mean
- $\bar{x} = \frac{4(31.0) + 4(30.0) + 4(27.5)}{12} = 29.5$

**Step 4**: Calculate MSG
- MSG = $\frac{1}{3-1} [4(31.0-29.5)^2 + 4(30.0-29.5)^2 + 4(27.5-29.5)^2]$
- MSG = $\frac{1}{2} [4(1.5)^2 + 4(0.5)^2 + 4(-2.0)^2]$
- MSG = $\frac{1}{2} [9 + 1 + 16]$
- MSG = $\frac{26}{2} = 13$

**Step 5**: Calculate MSE
- Total sum of squares = $(30-29.5)^2 + (32-29.5)^2 + ... + (31-29.5)^2 = 467$
- Between-group sum of squares = 26
- Within-group sum of squares = 467 - 26 = 441
- MSE = $\frac{441}{12-3} = \frac{441}{9} = 49$

**Step 6**: Calculate the F-statistic
- F = $\frac{MSG}{MSE} = \frac{13}{49} = 0.265$

**Step 7**: Determine the p-value
- df₁ = 3 - 1 = 2
- df₂ = 12 - 3 = 9
- Using software: p-value = P(F ≥ 0.265) ≈ 0.773

**Step 8**: Make a decision
- Since p-value = 0.773 > 0.05, we fail to reject H₀
- Conclusion: There is insufficient evidence to conclude that the mean travel times differ across the three routes

## 7. Common Misconceptions and Pitfalls

### Misconception 1: ANOVA Tests for Any Difference
- **Misconception**: ANOVA tests for any type of difference between groups
- **Reality**: ANOVA specifically tests for differences in means, not medians, variances, or other parameters

### Misconception 2: Significant ANOVA Means All Groups Differ
- **Misconception**: A significant ANOVA result means all group means are different
- **Reality**: A significant result only indicates that at least one mean differs from the others

### Pitfall 1: Ignoring Conditions
- **Problem**: Using ANOVA when conditions are not satisfied
- **Solution**: Always check independence, normality, and equal variance assumptions

### Pitfall 2: Conducting Multiple t-tests Without Correction
- **Problem**: Performing multiple pairwise comparisons without adjusting the significance level
- **Solution**: Use the Bonferroni correction or other multiple comparison procedures

## 8. Key Takeaways

1. **ANOVA Purpose**:
   - Compares means across multiple groups with a single hypothesis test
   - Controls the overall Type I error rate better than multiple pairwise comparisons

2. **F-Statistic**:
   - Ratio of between-group variance to within-group variance
   - Large values suggest significant differences between group means
   - Under H₀, follows an F-distribution with df₁ = k-1 and df₂ = n-k degrees of freedom

3. **Conditions**:
   - Independence: Observations are independent within and across groups
   - Normality: Data within each group is approximately normally distributed
   - Equal Variance: Variability across groups is comparable

4. **Multiple Comparisons**:
   - After a significant ANOVA, use pairwise comparisons to identify specific differences
   - Apply the Bonferroni correction to control the overall Type I error rate
   - Adjusted significance level: α* = α/K, where K = k(k-1)/2

5. **Interpretation**:
   - Failing to reject H₀: Insufficient evidence of differences between means
   - Rejecting H₀: At least one group mean differs from the others
   - Follow-up with multiple comparisons to identify specific differences