# DSC 215: Probability and Statistics for Data Science
## Module 4 Summary: Distributions of Random Variables

## 1. Introduction to Probability Distributions

### Common Distributions
- **Discrete Random Variables**:
  - Bernoulli distribution
  - Binomial distribution
  - Geometric distribution
  - Negative binomial distribution
  - Poisson distribution

- **Continuous Random Variables**:
  - Normal distribution
  - Chi-squared distribution
  - t-distribution
  - F-distribution
  - Logistic distribution

## 2. Bernoulli Distribution

### Definition
- Models processes with only two outcomes: "success" (1) and "failure" (0)
- A random variable X with a Bernoulli distribution takes:
  - Value 1 with probability p
  - Value 0 with probability 1-p

### Probability Mass Function (PMF)
$$p_X(x) = \begin{cases}
p & \text{if } x = 1 \\
1-p & \text{if } x = 0 \\
0 & \text{otherwise}
\end{cases}$$

### Expected Value and Variance
- Expected value: $\mu = \mathbb{E}(X) = p$
- Variance: $\sigma^2 = p(1-p)$

### Applications
- Coin flips
- Voting preference in a two-party system
- Whether a product is defective

## 3. Binomial Distribution

### Definition
- Describes the probability of having exactly k successes in n independent Bernoulli trials
- Each trial has the same probability p of success
- Notation: $X \sim B(n,p)$ means X follows a binomial distribution with parameters n and p

### Probability Mass Function (PMF)
$$\mathbb{P}(X = k) = \binom{n}{k}p^k(1-p)^{n-k} \text{ for } k = 0,1,...,n$$

Where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.

### Expected Value and Variance
- Expected value: $\mu = np$
- Variance: $\sigma^2 = np(1-p)$

### Example: Peanut Allergies
If the probability of a child having a peanut allergy is 2%, and a classroom has 30 children:
- Probability that none of them has a peanut allergy:
  $\mathbb{P}(X = 0) = \binom{30}{0}0.02^0 \times 0.98^{30} \approx 0.5455$
- Probability that 3 of them have a peanut allergy:
  $\mathbb{P}(X = 3) = \binom{30}{3}0.02^3 \times 0.98^{27} \approx 0.0188$

### Example: International Students
If 23.2% of UCSD students are international students, and there are 50 students on a dorm floor:
- Expected number of international students: $E[X] = np = 50 \times 0.232 = 11.6$
- Standard deviation: $SD(X) = \sqrt{np(1-p)} = \sqrt{50 \times 0.232 \times 0.768} \approx 2.99$

## 4. Normal Distribution

### Definition
- Symmetric, unimodal, bell-shaped curve
- Parametrized by mean μ and standard deviation σ
- Notation: $X \sim \mathcal{N}(\mu, \sigma)$

### Probability Density Function (PDF)
$$f_X(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

### Standard Normal Distribution
- When $\mu = 0$ and $\sigma = 1$, we have the standard normal distribution: $\mathcal{N}(0,1)$
- Often denoted as Z

### Z-scores
- The Z-score of an observation x is the number of standard deviations it falls above or below the mean:
  $$Z = \frac{x - \mu}{\sigma}$$
- Z-scores allow us to standardize data for comparison
- Z-scores follow the standard normal distribution

### Finding Tail Areas
- Methods to calculate probabilities:
  - Statistical software (R, Python, MATLAB)
  - Probability tables
  - Graphing calculators

### Example: SAT Scores
If SAT scores follow $\mathcal{N}(1100, 200)$ and Ann scores 1300:
- Z-score: $Z = \frac{1300-1100}{200} = 1$
- Probability of scoring below 1300: $\mathbb{P}(X \leq 1300) \approx 0.8413$

### Example: Test Scores
For a test with scores normally distributed with mean 100 and standard deviation 15:
- The interquartile range (IQR) can be calculated using Z-scores:
  - Q1 corresponds to Z = -0.6745
  - Q3 corresponds to Z = 0.6745
  - Q1 = 100 + (-0.6745 × 15) = 89.88
  - Q3 = 100 + (0.6745 × 15) = 110.12
  - IQR = Q3 - Q1 = 20.24

## 5. Approximating Binomial with Normal Distribution

### Conditions for Approximation
- The binomial distribution $B(n,p)$ is approximately normal when:
  - $np \geq 10$
  - $n(1-p) \geq 10$

### Parameters for Approximation
- Use $\mathcal{N}(\mu, \sigma)$ where:
  - $\mu = np$
  - $\sigma = \sqrt{np(1-p)}$

### Example: Defective Light Bulbs
If 2% of light bulbs are defective, what is the probability of getting 30 or fewer defective bulbs in a batch of 1000?
- Check conditions: $np = 1000 \times 0.02 = 20 \geq 10$ and $n(1-p) = 980 \geq 10$
- Use normal approximation with $\mu = 20$ and $\sigma = \sqrt{1000 \times 0.02 \times 0.98} \approx 4.43$
- Calculate Z-score: $Z = \frac{30-20}{4.43} \approx 2.26$
- Probability: $\mathbb{P}(X \leq 30) = \mathbb{P}(Z \leq 2.26) \approx 0.988$

## 6. Theoretical Foundations

### Law of Large Numbers (LLN)
- If $X_1, X_2, ...$ is a sequence of independent and identically distributed random variables with expected value $\mu$, then the sample average $\bar{X}_n = \frac{X_1 + ... + X_n}{n}$ satisfies:
  $$\mathbb{P}(\lim_{n\to\infty} \bar{X}_n = \mu) = 1$$
- Intuitively: As we increase the number of trials, the sample mean converges to the expected value

### Central Limit Theorem (CLT)
- If $X_1, X_2, ...$ is a sequence of independent and identically distributed random variables with expected value $\mu$ and variance $\sigma^2 < \infty$, then:
  $$\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$
- Intuitively: The distribution of the sample mean approaches a normal distribution as sample size increases
- This is why the normal distribution is so prevalent in statistics

## 7. Other Important Distributions

### Chi-Squared Distribution
- If $Z_1, Z_2, ..., Z_k$ are independent standard normal random variables, then $Q = \sum_{i=1}^{k} Z_i^2$ follows a chi-squared distribution with k degrees of freedom
- Notation: $Q \sim \chi^2_k$
- Used in goodness-of-fit tests and confidence intervals for variance
- PDF becomes less skewed as degrees of freedom increase

### t-Distribution
- Used when the population variance is unknown and estimated from the data
- If the sample variance $s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$ is used instead of $\sigma^2$, then $\frac{\bar{X} - \mu}{s/\sqrt{n}}$ follows a t-distribution with n-1 degrees of freedom
- Has heavier tails than the normal distribution
- Approaches the standard normal distribution as degrees of freedom increase

### F-Distribution
- Ratio of two chi-squared distributions, each divided by their degrees of freedom:
  $$F = \frac{U/d_1}{V/d_2}$$
- Where $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$
- Used in ANOVA and testing equality of variances
- Parametrized by two degrees of freedom parameters: $d_1$ and $d_2$

### Example: F-Distribution
If $W = \frac{\chi^2_3/3}{\chi^2_2/2}$, then W follows an F-distribution with degrees of freedom 3 and 2, denoted as $F_{3,2}$.

## 8. Practical Applications in Statistical Inference

### Hypothesis Testing
- Test statistics often follow specific distributions under the null hypothesis
- The distribution of the test statistic is used to calculate p-values
- Example: For testing if a coin is fair after 100 flips with 60 heads:
  - Test statistic: $Z = \frac{60-50}{5} = 2$
  - Under the null hypothesis (p = 0.5), Z follows approximately $\mathcal{N}(0,1)$
  - P-value: $\mathbb{P}(Z \geq 2) \approx 0.0228$

### Confidence Intervals
- Different distributions are used depending on what parameter is being estimated
- Normal distribution: Used when population variance is known
- t-distribution: Used when population variance is unknown
- Chi-squared distribution: Used for variance estimation

## 9. Key Properties of Random Variables

### Discrete vs. Continuous Random Variables
- **Discrete Random Variables**:
  - Take values from a countable set
  - Have a probability mass function (PMF)
  - Example: Number of points scored in a basketball game
  - For discrete RVs, $\mathbb{P}(X = x)$ can be positive

- **Continuous Random Variables**:
  - Take values from an uncountable set (typically an interval)
  - Have a probability density function (PDF)
  - Example: Distance walked in a day
  - For continuous RVs, $\mathbb{P}(X = x) = 0$ for any specific value x

### Properties of Symmetric Distributions
- If Z has a symmetric distribution around 0 and $\mathbb{P}(Z < a) = 0.25$, then:
  - $\mathbb{P}(Z > -a) = 1 - \mathbb{P}(Z \leq -a) = 1 - \mathbb{P}(Z < -a) = 1 - 0.25 = 0.75$
  - This is because for symmetric distributions, $\mathbb{P}(Z < -a) = \mathbb{P}(Z > a)$

## 10. Key Takeaways

1. Different distributions model different types of random phenomena
2. The normal distribution is central to statistical inference due to the Central Limit Theorem
3. Z-scores standardize observations for comparison across different distributions
4. The binomial distribution can be approximated by the normal distribution under certain conditions
5. The t-distribution, chi-squared distribution, and F-distribution are crucial for statistical inference when population parameters are unknown
6. Understanding the properties of these distributions is essential for hypothesis testing and confidence interval construction