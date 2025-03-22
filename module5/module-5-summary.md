# DSC 215: Probability and Statistics for Data Science
## Module 5 Summary: Introduction to Statistical Inference

## 1. Introduction to Statistical Inference

### What is Statistical Inference?
- **Definition**: The process by which we estimate parameters of interest from data and quantify the uncertainty in our estimates
- **Key Components**:
  - Point estimates: Single values that estimate population parameters
  - Confidence intervals: Ranges of plausible values for population parameters
  - Hypothesis tests: Methods to evaluate claims about the population

### Population Parameters vs. Sample Statistics
- **Population Parameter**: A numerical characteristic of the entire population (usually unknown)
  - Example: The true proportion of all voters who support a candidate (p)
- **Sample Statistic**: A numerical characteristic calculated from a sample (known)
  - Example: The proportion of sampled voters who support a candidate (p̂)

### Sources of Error in Estimation
- **Sampling Error**: Variability that occurs due to random sampling
  - Related to sample size (n)
  - Unavoidable but can be quantified
- **Bias**: Systematic error that causes estimates to consistently deviate from the true parameter
  - Examples: Non-response bias, selection bias, poorly worded questions
  - Can be minimized through proper study design

## 2. Sampling Distribution of a Proportion

### Sampling Distribution
- **Definition**: The distribution of a sample statistic over all possible samples of the same size from the same population
- **Properties of the Sampling Distribution of p̂**:
  - Center: The mean of p̂ is p (the population parameter)
  - Spread: The standard error of p̂ is $\sqrt{\frac{p(1-p)}{n}}$
  - Shape: Approximately normal for large enough samples

### Standard Error
- **Definition**: The standard deviation of the sampling distribution
- **Formula for Proportion**: 
  $$SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}$$
- **Interpretation**: Measures the typical deviation between the sample proportion and the population proportion
- **Example**: For a sample of 1000 people with p = 0.75:
  $$SE_{\hat{p}} = \sqrt{\frac{0.75 \times 0.25}{1000}} \approx 0.0137$$

### Central Limit Theorem (CLT) for Proportions
- **Statement**: For large enough samples, the sampling distribution of p̂ is approximately normal with:
  - Mean: μ = p
  - Standard error: $SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}$

- **Success/Failure Condition**: For the CLT to apply, we need:
  - np ≥ 10 (at least 10 successes)
  - n(1-p) ≥ 10 (at least 10 failures)

### Using the CLT in Practice
- Since p is unknown in real applications, we use p̂ to:
  1. Check the success/failure condition: np̂ ≥ 10 and n(1-p̂) ≥ 10
  2. Estimate the standard error: $SE_{\hat{p}} \approx \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Example: Applying the CLT
If 761 out of 1000 randomly sampled people support candidate A:
- Sample proportion: p̂ = 761/1000 = 0.761
- Estimated standard error: $SE_{\hat{p}} \approx \sqrt{\frac{0.761 \times 0.239}{1000}} \approx 0.0135$
- Success/failure check: 
  - np̂ = 1000 × 0.761 = 761 ≥ 10 ✓
  - n(1-p̂) = 1000 × 0.239 = 239 ≥ 10 ✓

## 3. Confidence Intervals for a Proportion

### Definition and Interpretation
- **Confidence Interval**: A range of plausible values for the population parameter
- **General Form**: Point estimate ± Margin of error
- **Interpretation**: If we repeatedly collect samples and construct confidence intervals using the same method, approximately (confidence level)% of these intervals would contain the true population parameter

### Formula for Confidence Interval
- **Formula**: 
  $$\hat{p} \pm z^* \times SE_{\hat{p}}$$
  where z* is the critical value corresponding to the desired confidence level

- **Margin of Error**: 
  $$MOE = z^* \times SE_{\hat{p}}$$

### Common Critical Values (z*)
- 90% confidence: z* = 1.64
- 95% confidence: z* = 1.96
- 99% confidence: z* = 2.58

### Example: Constructing a 95% Confidence Interval
For a sample where 761 out of 1000 people support candidate A:
- p̂ = 0.761
- SE = 0.0135
- 95% confidence interval:
  $$0.761 \pm 1.96 \times 0.0135 = 0.761 \pm 0.0265 = (0.7345, 0.7875)$$

- Interpretation: We are 95% confident that the true proportion of people who support candidate A is between 73.45% and 78.75%.

### Effect of Confidence Level on Interval Width
- Higher confidence level → Wider interval
- Lower confidence level → Narrower interval
- Trade-off between precision (narrow interval) and confidence (high percentage)

## 4. Sample Size Determination

### Determining Sample Size for a Desired Margin of Error
- **Formula**: 
  $$n = \frac{z^{*2} \times p(1-p)}{MOE^2}$$

- Since p is unknown before sampling, we can:
  1. Use a previous estimate of p
  2. Use p = 0.5 (which maximizes p(1-p) and gives the largest, most conservative sample size)

### Example: Sample Size Calculation
To achieve a margin of error of 5% with 95% confidence:
- z* = 1.96
- Using p = 0.5 (conservative approach):
  $$n = \frac{1.96^2 \times 0.5 \times 0.5}{0.05^2} = \frac{0.9604}{0.0025} = 384.16$$
- We would need at least 385 participants.

## 5. Common Misconceptions about Confidence Intervals

### What a Confidence Interval IS:
- A range of plausible values for the population parameter
- A procedure that, when repeated, captures the true parameter at the specified rate
- A measure of the reliability of our estimation method

### What a Confidence Interval IS NOT:
- A probability statement about the parameter (once calculated, the interval either contains the parameter or it doesn't)
- A statement that X% of the population falls within the interval
- A guarantee that the true parameter is in any specific interval

## 6. Practical Examples

### Example 1: Teenage Phone Usage
A random sample of 1000 teenagers were interviewed about their average daily phone use. About 60% said they spent around 5-7 hours on their phones per day.

- Sample proportion: p̂ = 0.6
- Standard error: $SE_{\hat{p}} = \sqrt{\frac{0.6 \times 0.4}{1000}} = 0.015$
- 95% confidence interval: 
  $$0.6 \pm 1.96 \times 0.015 = 0.6 \pm 0.029 = (0.571, 0.629)$$

- Interpretation: We are 95% confident that the true proportion of teenagers who spend 5-7 hours on their phones daily is between 57.1% and 62.9%.

### Example 2: Roller Coaster Survey
According to a survey, around 38% of American teenagers are scared to ride roller coasters. This survey was conducted based on a random sample of 800 teenagers.

- Checking CLT conditions:
  - np̂ = 800 × 0.38 = 304 ≥ 10 ✓
  - n(1-p̂) = 800 × 0.62 = 496 ≥ 10 ✓
- Standard error: $SE_{\hat{p}} = \sqrt{\frac{0.38 \times 0.62}{800}} \approx 0.017$
- 95% confidence interval:
  $$0.38 \pm 1.96 \times 0.017 = 0.38 \pm 0.033 = (0.347, 0.413)$$

### Example 3: E-book Preferences
A research firm wants to find the proportion of adults who prefer traditional books to E-books. They took a random sample of 200 adults and found that 65% like E-books better.

- Standard error: $SE_{\hat{p}} = \sqrt{\frac{0.65 \times 0.35}{200}} \approx 0.034$
- For an 80% confidence interval, z* = 1.28
- 80% confidence interval:
  $$0.65 \pm 1.28 \times 0.034 = 0.65 \pm 0.044 = (0.606, 0.694)$$

- Interpretation: We are 80% confident that the true proportion of adults who prefer E-books is between 60.6% and 69.4%.

### Example 4: Sample Size for Delivery Company
A delivery company wants to estimate the proportion of on-time deliveries with a margin of error of 3% at 95% confidence. How many customers should they survey?

- Using p̂ = 0.5 (conservative approach):
  $$n = \frac{1.96^2 \times 0.5 \times 0.5}{0.03^2} = \frac{0.9604}{0.0009} = 1067.11$$
- They should survey at least 1068 customers.

## 7. Key Takeaways

1. Statistical inference allows us to make educated guesses about population parameters based on sample data.

2. The Central Limit Theorem tells us that for large enough samples, the sampling distribution of p̂ is approximately normal, regardless of the shape of the population distribution.

3. Confidence intervals provide a range of plausible values for the population parameter, along with a measure of confidence in that range.

4. The width of a confidence interval is affected by:
   - Sample size (n): Larger samples lead to narrower intervals
   - Confidence level: Higher confidence requires wider intervals
   - Population variability: More variable populations require wider intervals

5. When interpreting confidence intervals, be careful to avoid common misconceptions:
   - A 95% confidence interval does not mean there is a 95% probability that the parameter is in that specific interval
   - Instead, it means that if we repeated the sampling process many times, about 95% of the resulting intervals would contain the true parameter

6. Sample size calculations help us determine how many observations we need to achieve a desired level of precision in our estimates.