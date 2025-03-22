# DSC 215: Probability and Statistics for Data Science
## Module 6 Summary: Hypothesis Testing for a Proportion

## 1. Introduction to Hypothesis Testing

### The Hypothesis Testing Framework
- **Definition**: A formal procedure for evaluating claims about a population parameter
- **Purpose**: To determine whether sample data provides sufficient evidence against a specified claim
- **Key Components**:
  - Null Hypothesis (H₀): The "status quo" or "skeptical" perspective
  - Alternative Hypothesis (H₁ or H<sub>A</sub>): The claim being investigated

### Types of Hypotheses
- **Null Hypothesis (H₀)**:
  - Makes a specific claim about the parameter (often that there is "no effect" or "no difference")
  - Always contains an equality (=, ≤, or ≥)
  - Example: H₀: p = 0.5 (the proportion equals 0.5)

- **Alternative Hypothesis (H<sub>A</sub>)**:
  - The claim we are looking for evidence to support
  - Contains only inequalities (<, >, or ≠)
  - Example: H<sub>A</sub>: p > 0.5 (the proportion is greater than 0.5)

### Types of Hypothesis Tests
- **Two-sided test**: H<sub>A</sub> claims the parameter is different from the null value (≠)
  - Example: H₀: p = 0.5 vs. H<sub>A</sub>: p ≠ 0.5
- **One-sided test**: H<sub>A</sub> claims the parameter is either greater than (>) or less than (<) the null value
  - Example: H₀: p ≤ 0.5 vs. H<sub>A</sub>: p > 0.5
  - Example: H₀: p ≥ 0.5 vs. H<sub>A</sub>: p < 0.5

## 2. The Logic of Hypothesis Testing

### Decision Process
- We start by assuming the null hypothesis is true
- We collect sample data and calculate a test statistic
- We determine how likely our observed result (or more extreme) would be if H₀ were true
- Based on this probability (p-value), we either:
  - Reject H₀ if the evidence against it is strong enough
  - Fail to reject H₀ if the evidence is not strong enough

### Important Note
- Failing to reject H₀ does not mean we accept or prove H₀
- It simply means we don't have enough evidence to reject it
- This is similar to "innocent until proven guilty" in a legal system

## 3. Errors in Hypothesis Testing

### Type I Error
- **Definition**: Rejecting a true null hypothesis
- **Probability**: α (significance level)
- **Example**: Concluding a medical treatment is effective when it actually isn't

### Type II Error
- **Definition**: Failing to reject a false null hypothesis
- **Probability**: β
- **Example**: Failing to detect that a medical treatment is effective when it actually is

### Relationship Between Errors
- There is a trade-off between Type I and Type II errors
- Decreasing α (making it harder to reject H₀) increases β
- Increasing α (making it easier to reject H₀) decreases β

### Power of a Test
- **Definition**: The probability of correctly rejecting a false null hypothesis (1 - β)
- **Factors affecting power**:
  - Sample size (larger samples increase power)
  - Effect size (larger differences from H₀ are easier to detect)
  - Significance level (higher α increases power but also increases Type I error risk)

## 4. Testing Hypotheses Using Confidence Intervals

### Procedure
1. Calculate a confidence interval for the parameter
2. Check if the null value (from H₀) falls within the interval
3. If the null value is outside the interval, reject H₀
4. If the null value is inside the interval, fail to reject H₀

### Example: Multiple Choice Question
A multiple choice question has 4 options. We want to test if adults perform better than random guessing.
- H₀: p = 0.25 (adults are as accurate as random guessing)
- H<sub>A</sub>: p ≠ 0.25 (adults perform differently than random guessing)

**Scenario 1**: 21 out of 100 adults answer correctly
- Sample proportion: p̂ = 0.21
- Standard error: SE = √[0.21(1-0.21)/100] = 0.0407
- 95% confidence interval: p̂ ± 1.96 × SE = 0.21 ± 1.96 × 0.0407 = (0.1302, 0.2898)
- Since p₀ = 0.25 falls within the interval, we fail to reject H₀

**Scenario 2**: 37 out of 100 adults answer correctly
- Sample proportion: p̂ = 0.37
- Standard error: SE = √[0.37(1-0.37)/100] = 0.0483
- 95% confidence interval: p̂ ± 1.96 × SE = 0.37 ± 1.96 × 0.0483 = (0.2754, 0.4646)
- Since p₀ = 0.25 falls outside the interval, we reject H₀

## 5. Testing Hypotheses Using P-values

### P-value
- **Definition**: The probability of observing a test statistic as extreme as, or more extreme than, the one observed, assuming H₀ is true
- **Interpretation**: A measure of the strength of evidence against H₀
- **Decision rule**: Reject H₀ if p-value < α

### Calculating P-values for a Proportion Test
1. Calculate the test statistic:
   $$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$
   where p₀ is the null value, p̂ is the sample proportion, and n is the sample size

2. Find the p-value:
   - For H<sub>A</sub>: p ≠ p₀ (two-sided): P(Z ≤ -|z|) + P(Z ≥ |z|) = 2 × P(Z ≥ |z|)
   - For H<sub>A</sub>: p > p₀ (right-tailed): P(Z ≥ z)
   - For H<sub>A</sub>: p < p₀ (left-tailed): P(Z ≤ z)

### Example: Policy Support
We want to test if a majority of adults support Policy A.
- H₀: p = 0.5 (50% support)
- H<sub>A</sub>: p ≠ 0.5 (support differs from 50%)

A random sample of 1000 adults shows 42% support the policy.
- Test statistic: z = (0.42 - 0.5)/√[0.5(1-0.5)/1000] = -0.08/0.016 = -5
- P-value (two-sided): 2 × P(Z ≥ 5) ≈ 5.73 × 10⁻⁷
- Since p-value < 0.05, we reject H₀
- Conclusion: There is strong evidence that the proportion of adults who support Policy A differs from 50% (specifically, it appears to be less than 50%)

## 6. Steps for Conducting a Hypothesis Test for a Proportion

### Step 1: Prepare
- Identify the parameter of interest
- State the null and alternative hypotheses
- Choose the significance level α
- Identify the sample proportion p̂ and sample size n

### Step 2: Check
- Verify that the sample is random or representative
- Check the success/failure condition using the null value p₀:
  - np₀ ≥ 10
  - n(1-p₀) ≥ 10

### Step 3: Calculate
- Compute the standard error using the null value: SE = √[p₀(1-p₀)/n]
- Calculate the test statistic: z = (p̂ - p₀)/SE
- Find the p-value based on the form of H<sub>A</sub>

### Step 4: Conclude
- Compare the p-value to α
- Make a decision: reject H₀ or fail to reject H₀
- State the conclusion in the context of the problem

## 7. Choosing the Significance Level (α)

### Common Choices
- α = 0.05 (5%): Standard in many fields
- α = 0.01 (1%): More stringent, used when Type I errors are costly
- α = 0.10 (10%): More lenient, used when Type II errors are costly

### Considerations
- **Type I Error Concerns**: Use smaller α when falsely rejecting H₀ is serious
  - Example: Approving an ineffective drug (α = 0.01 or lower)
- **Type II Error Concerns**: Use larger α when failing to detect an effect is serious
  - Example: Missing a potential environmental hazard (α = 0.10)

## 8. Practical Examples

### Example 1: College Dropout Rate
A study aims to determine if the dropout rate for undergraduate college students has changed from the 2018 rate of 40%.

- Parameter of interest: p = proportion of undergraduate students who drop out
- H₀: p = 0.4
- H<sub>A</sub>: p ≠ 0.4
- Significance level: α = 0.05

Suppose a random sample of 500 students shows 175 dropped out (p̂ = 0.35).
- Check conditions: np₀ = 500 × 0.4 = 200 ≥ 10; n(1-p₀) = 500 × 0.6 = 300 ≥ 10 ✓
- SE = √[0.4(1-0.4)/500] = 0.022
- Test statistic: z = (0.35 - 0.4)/0.022 = -2.27
- P-value (two-sided): 2 × P(Z ≥ 2.27) ≈ 0.023
- Decision: Since p-value < 0.05, reject H₀
- Conclusion: There is sufficient evidence to conclude that the dropout rate has changed from 40% (appears to have decreased).

### Example 2: New Drink Flavor
A company will introduce a new drink to the market if more than 65% of people like the flavor.

- Parameter of interest: p = proportion of people who like the flavor
- H₀: p = 0.65
- H<sub>A</sub>: p > 0.65
- Significance level: α = 0.05

Suppose a random sample of 200 people shows 140 like the flavor (p̂ = 0.7).
- Check conditions: np₀ = 200 × 0.65 = 130 ≥ 10; n(1-p₀) = 200 × 0.35 = 70 ≥ 10 ✓
- SE = √[0.65(1-0.65)/200] = 0.034
- Test statistic: z = (0.7 - 0.65)/0.034 = 1.47
- P-value (right-tailed): P(Z ≥ 1.47) ≈ 0.071
- Decision: Since p-value > 0.05, fail to reject H₀
- Conclusion: There is insufficient evidence to conclude that more than 65% of people like the flavor.

### Example 3: Law Support in a Small Town
A study investigates whether the proportion of residents in a small town who support a certain law is 68%.

- Parameter of interest: p = proportion of residents who support the law
- H₀: p = 0.68
- H<sub>A</sub>: p ≠ 0.68
- Significance level: α = 0.05

A random sample of 200 residents shows 140 support the law (p̂ = 0.7).
- Check conditions: np₀ = 200 × 0.68 = 136 ≥ 10; n(1-p₀) = 200 × 0.32 = 64 ≥ 10 ✓
- 95% confidence interval: p̂ ± 1.96 × √[p̂(1-p̂)/n] = 0.7 ± 1.96 × √[0.7(1-0.7)/200] = 0.7 ± 0.064 = (0.636, 0.764)
- Since p₀ = 0.68 falls within the interval, fail to reject H₀
- Conclusion: There is insufficient evidence to conclude that the proportion of residents who support the law differs from 68%.

## 9. Common Misconceptions and Pitfalls

### Misconception 1: Failing to reject H₀ means H₀ is true
- Correct interpretation: We don't have enough evidence to reject H₀, not that H₀ is proven true

### Misconception 2: P-value is the probability that H₀ is true
- Correct interpretation: P-value is the probability of observing data as extreme as ours if H₀ were true

### Misconception 3: Statistical significance implies practical significance
- A result can be statistically significant but too small to matter in practice
- Always consider the context and magnitude of the effect

### Pitfall 1: Using p̂ instead of p₀ to calculate SE in hypothesis testing
- For confidence intervals: Use p̂ to calculate SE
- For hypothesis tests: Use p₀ to calculate SE

### Pitfall 2: Incorrect formulation of hypotheses
- H₀ must contain an equality (=, ≤, or ≥)
- H<sub>A</sub> must contain only inequalities (<, >, or ≠)
- Parameters (p, μ) should be used, not statistics (p̂, x̄)

## 10. Key Takeaways

1. Hypothesis testing provides a formal framework for making decisions based on data

2. The null hypothesis (H₀) represents the status quo or skeptical perspective, while the alternative hypothesis (H<sub>A</sub>) represents the claim we're looking for evidence to support

3. Two approaches to hypothesis testing:
   - Using confidence intervals: Reject H₀ if the null value falls outside the interval
   - Using p-values: Reject H₀ if the p-value is less than the significance level α

4. Type I error occurs when we reject a true H₀; Type II error occurs when we fail to reject a false H₀

5. The significance level α represents the probability of making a Type I error

6. When conducting a hypothesis test for a proportion:
   - Use p₀ (not p̂) to calculate the standard error
   - Check the success/failure condition using p₀
   - State conclusions in the context of the problem

7. The choice of significance level should balance the risks of Type I and Type II errors based on the specific context of the problem