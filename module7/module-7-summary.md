# DSC 215: Probability and Statistics for Data Science
## Module 7 Summary: Inference for Comparing Two Proportions

## 1. Introduction to Comparing Two Proportions

### Why Compare Two Proportions?
- **Purpose**: To determine if there is a significant difference between two population proportions
- **Applications**:
  - Medical studies (treatment vs. control groups)
  - Marketing (comparing effectiveness of two campaigns)
  - Social research (comparing behaviors across different demographics)
  - Quality control (comparing defect rates between manufacturing processes)

### Key Parameters and Statistics
- **Population Parameters**: p₁ and p₂ (true proportions in each population)
- **Sample Statistics**: p̂₁ and p̂₂ (observed proportions in each sample)
- **Parameter of Interest**: p₁ - p₂ (difference between population proportions)
- **Point Estimate**: p̂₁ - p̂₂ (difference between sample proportions)

## 2. Confidence Intervals for the Difference of Two Proportions

### Conditions for Valid Inference
1. **Independence**:
   - Data are independent within each group
   - Data are independent between groups
   - Satisfied by random sampling or random assignment

2. **Success/Failure Condition**:
   - For each group i (i = 1, 2):
     - nᵢp̂ᵢ ≥ 10 (at least 10 successes)
     - nᵢ(1-p̂ᵢ) ≥ 10 (at least 10 failures)

### Formula for the Standard Error
- **Standard Error for Difference in Proportions**:
  $$SE = \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}}$$

- **Estimated Standard Error** (using sample proportions):
  $$SE = \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$

### Confidence Interval Formula
- **General Formula**:
  $$(\hat{p}_1 - \hat{p}_2) \pm z^* \times SE$$

- **Expanded Form**:
  $$(\hat{p}_1 - \hat{p}_2) \pm z^* \times \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$

### Example: Blood Thinner Study
A study examined the effect of blood thinners on survival after heart attacks:

| Group | Survived | Died | Total |
|-------|----------|------|-------|
| Control | 11 | 39 | 50 |
| Treatment | 14 | 26 | 40 |

**Step 1**: Calculate sample proportions
- p̂ₜ (treatment) = 14/40 = 0.35
- p̂ₖ (control) = 11/50 = 0.22
- Difference: p̂ₜ - p̂ₖ = 0.35 - 0.22 = 0.13

**Step 2**: Check conditions
- Independence: Satisfied (randomized experiment)
- Success/Failure: All groups have at least 10 successes and failures

**Step 3**: Calculate standard error
$$SE = \sqrt{\frac{0.35(1-0.35)}{40} + \frac{0.22(1-0.22)}{50}} = 0.095$$

**Step 4**: Construct 90% confidence interval (z* = 1.65)
$$0.13 \pm 1.65 \times 0.095 = 0.13 \pm 0.157 = (-0.027, 0.287)$$

**Interpretation**: We are 90% confident that blood thinners have an impact on survival rate ranging from -2.7% (slightly harmful) to +28.7% (beneficial). Since the interval contains 0, we cannot conclude at this confidence level whether blood thinners help or harm in this context.

## 3. Hypothesis Testing for the Difference of Two Proportions

### Hypothesis Formulation
- **Null Hypothesis (H₀)**: p₁ - p₂ = 0 (no difference between proportions)
- **Alternative Hypothesis (H<sub>A</sub>)**:
  - Two-sided: p₁ - p₂ ≠ 0 (proportions are different)
  - One-sided: p₁ - p₂ > 0 or p₁ - p₂ < 0 (one proportion is larger)

### Pooled Proportion
- **When to Use**: When testing H₀: p₁ = p₂ (null hypothesis assumes equal proportions)
- **Formula**:
  $$\hat{p}_{pooled} = \frac{n_1\hat{p}_1 + n_2\hat{p}_2}{n_1 + n_2} = \frac{\text{total successes}}{\text{total sample size}}$$

### Standard Error Under the Null Hypothesis
- **Formula**:
  $$SE = \sqrt{\hat{p}_{pooled}(1-\hat{p}_{pooled})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$

### Test Statistic
- **Z-statistic**:
  $$Z = \frac{(\hat{p}_1 - \hat{p}_2) - 0}{SE} = \frac{\hat{p}_1 - \hat{p}_2}{SE}$$

### P-value Calculation
- **Two-sided test**: P(|Z| ≥ |observed z|)
- **Right-tailed test**: P(Z ≥ observed z)
- **Left-tailed test**: P(Z ≤ observed z)

### Example: Survival Rate Study
A large-scale study examined survival rates in treatment and control groups:

| Group | Survived | Died | Total |
|-------|----------|------|-------|
| Control | 505 | 44,405 | 44,910 |
| Treatment | 500 | 44,425 | 44,925 |

**Step 1**: State hypotheses
- H₀: pₜ - pₖ = 0 (no difference in death rates)
- H<sub>A</sub>: pₜ - pₖ ≠ 0 (death rates are different)

**Step 2**: Calculate sample proportions
- p̂ₜ = 500/44,925 = 0.01113
- p̂ₖ = 505/44,910 = 0.01125
- Difference: p̂ₜ - p̂ₖ = -0.00012

**Step 3**: Calculate pooled proportion
$$\hat{p}_{pooled} = \frac{500 + 505}{44,925 + 44,910} = \frac{1,005}{89,835} = 0.0112$$

**Step 4**: Check conditions
- Independence: Satisfied (randomized experiment)
- Success/Failure: All values (nₜ × p̂ₚₒₒₗₑₐ, nₜ × (1-p̂ₚₒₒₗₑₐ), etc.) are greater than 10

**Step 5**: Calculate standard error
$$SE = \sqrt{0.0112 \times 0.9888 \times \left(\frac{1}{44,925} + \frac{1}{44,910}\right)} = 0.00070$$

**Step 6**: Calculate test statistic
$$Z = \frac{-0.00012 - 0}{0.00070} = -0.17$$

**Step 7**: Find p-value
For a two-sided test with Z = -0.17, p-value = 0.865

**Step 8**: Make decision
Since p-value = 0.865 > 0.05, we fail to reject H₀.

**Interpretation**: The difference in deaths between the control and treatment groups can be reasonably explained by chance. There is insufficient evidence to conclude that the treatment affects survival rates.

## 4. Sample Size Determination for Confidence Intervals

### Determining Sample Size for a Desired Margin of Error
- **Formula for a Single Proportion**:
  $$n = \frac{z^{*2} \times p(1-p)}{MOE^2}$$

- **Conservative Approach** (when p is unknown):
  - Use p = 0.5 (maximizes p(1-p))
  - Results in the largest, most conservative sample size
  - Formula simplifies to:
    $$n = \frac{z^{*2} \times 0.25}{MOE^2}$$

### Example: Sample Size Calculation
To achieve a margin of error of 5% with 95% confidence:
- z* = 1.96
- Using p = 0.5 (conservative approach):
  $$n = \frac{1.96^2 \times 0.5 \times 0.5}{0.05^2} = \frac{0.9604}{0.0025} = 384.16$$
- We would need at least 385 participants.

### Reducing the Margin of Error
To cut the margin of error in half while maintaining the same confidence level:
- Original MOE = z* × √[p(1-p)/n]
- To halve the MOE: n<sub>new</sub> = 4 × n<sub>original</sub>

**Example**: If a 95% CI based on 100 students has a certain margin of error, to cut that margin of error in half (while maintaining 95% confidence), we would need 4 × 100 = 400 students.

## 5. Practical Examples

### Example 1: Non-profit vs. For-profit Employee Happiness
A study compared happiness levels between employees in non-profit and for-profit organizations:
- Non-profit: 423 out of 467 employees reported being happy (p̂₁ = 0.906)
- For-profit: 446 out of 531 employees reported being happy (p̂₂ = 0.840)

**Confidence Interval Calculation**:
- Difference in proportions: p̂₁ - p̂₂ = 0.906 - 0.840 = 0.066
- Standard error:
  $$SE = \sqrt{\frac{0.906 \times 0.094}{467} + \frac{0.840 \times 0.160}{531}} = 0.0214$$
- 99% confidence interval (z* = 2.576):
  $$0.066 \pm 2.576 \times 0.0214 = 0.066 \pm 0.055 = (0.0167, 0.1233)$$

**Interpretation**: We are 99% confident that the proportion of employees who are happy working in non-profit organizations is between 1.67% and 12.33% higher than the proportion of employees who are happy working in for-profit organizations.

### Example 2: Foreign-born Residents Comparison
A study compared the proportion of foreign-born residents in the U.S. and China:
- U.S.: 196 out of 980 residents were foreign-born (p̂₁ = 0.2)
- China: 212 out of 1560 residents were foreign-born (p̂₂ = 0.136)

**Hypothesis Test**:
- H₀: p₁ - p₂ = 0 (same proportion of foreign-born residents)
- H<sub>A</sub>: p₁ - p₂ ≠ 0 (different proportions)

- Pooled proportion:
  $$\hat{p}_{pooled} = \frac{196 + 212}{980 + 1560} = \frac{408}{2540} = 0.1606$$

- Standard error:
  $$SE = \sqrt{0.1606 \times 0.8394 \times \left(\frac{1}{980} + \frac{1}{1560}\right)} = 0.0150$$

- Test statistic:
  $$Z = \frac{0.2 - 0.136}{0.0150} = 4.267$$

- P-value (two-sided): 2 × P(Z > 4.267) < 0.0001

**Conclusion**: Since p-value < 0.05, we reject H₀. There is strong evidence that the proportion of foreign-born residents differs between the U.S. and China.

## 6. Key Takeaways

1. **Comparing Two Proportions**:
   - Allows us to determine if there's a significant difference between two groups
   - Uses the difference in sample proportions (p̂₁ - p̂₂) as the point estimate

2. **Confidence Intervals**:
   - Provide a range of plausible values for the true difference in proportions
   - Use individual sample proportions to calculate the standard error
   - Interpretation should address both magnitude and direction of the difference

3. **Hypothesis Testing**:
   - Typically tests whether the difference in proportions equals zero
   - Uses the pooled proportion to calculate standard error under the null hypothesis
   - Follows the same general framework as single-proportion hypothesis tests

4. **Sample Size Considerations**:
   - Larger samples provide more precise estimates (narrower confidence intervals)
   - To halve the margin of error, quadruple the sample size
   - When planning studies, use conservative estimates (p = 0.5) if no prior information is available

5. **Practical Significance**:
   - Statistical significance doesn't always imply practical importance
   - Consider the context and magnitude of the difference when interpreting results
   - Confidence intervals provide more information about effect size than p-values alone