# DSC 215: Probability and Statistics for Data Science
## Module 3 Summary: Introduction to Probability

## 1. Foundations of Probability

### Why Study Probability?
- Probability is the foundation upon which statistics is built
- Essential for machine learning, artificial intelligence, game theory, and information theory
- Provides a formal framework for understanding uncertainty and randomness
- Enables deeper understanding of statistical tools and techniques

### Sample Space
- **Definition**: The set of all possible outcomes of an experiment, denoted by Ω
- **Examples**:
  - Rolling a die: Ω = {1, 2, 3, 4, 5, 6}
  - Flipping a coin: Ω = {Heads, Tails}
  - Tossing a coin three times: Ω = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}

### Event Space
- **Definition**: A set whose elements are themselves sets (subsets of Ω)
- Every event A in the event space ℱ is a subset of Ω (A ⊂ Ω)
- The event space must satisfy certain properties:
  - The empty set ∅ must be in ℱ
  - If A is in ℱ, then its complement A<sup>c</sup> must also be in ℱ
  - If A₁, A₂, ... are all in ℱ, then their union must also be in ℱ

### Probability Measure
- **Definition**: A function ℙ: ℱ → [0,1] that assigns probabilities to events
- Must satisfy the axioms of probability:
  - ℙ(A) ≥ 0 for all A ∈ ℱ (non-negativity)
  - ℙ(Ω) = 1 (normalization)
  - If A₁, A₂, ... are disjoint events (A<sub>i</sub> ∩ A<sub>j</sub> = ∅ for i ≠ j), then ℙ(A₁ ∪ A₂ ∪ ...) = Σᵢ ℙ(A<sub>i</sub>)

### Properties of Probability Measures
- If A ⊂ B, then ℙ(A) ≤ ℙ(B)
- ℙ(A ∩ B) ≤ min(ℙ(A), ℙ(B))
- ℙ(A ∪ B) ≤ ℙ(A) + ℙ(B) (union bound)
- ℙ(A<sup>c</sup>) = 1 - ℙ(A)

### Example: Die Rolling
For a fair six-sided die:
- Sample space: Ω = {1, 2, 3, 4, 5, 6}
- Event space: ℱ = P(Ω) (the power set of Ω)
- Probability measure: If a set A ∈ ℱ has i elements, then ℙ(A) = i/6
- Example: ℙ({1, 4, 6}) = 3/6 = 0.5

## 2. Conditional Probability and Independence

### Conditional Probability
- **Definition**: The probability of event A occurring given that event B has occurred
- Formula: 
  $$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$
  where ℙ(B) ≠ 0

### Independence
- **Definition**: Two events A and B are independent if and only if:
  $$\mathbb{P}(A \cap B) = \mathbb{P}(A) \times \mathbb{P}(B)$$
- Equivalently, A and B are independent if:
  $$\mathbb{P}(A|B) = \mathbb{P}(A)$$

### Example: Left-Handed People
If 9% of people are left-handed and 2 people are selected at random from a large population:
- Probability both are left-handed (assuming independence):
  $$\mathbb{P}(\text{both left-handed}) = \mathbb{P}(\text{first left-handed}) \times \mathbb{P}(\text{second left-handed}) = 0.09^2 = 0.0081$$

### Example: Smallpox in Boston, 1721
A dataset of 6,224 individuals exposed to smallpox in Boston:

| | Inoculated | Not Inoculated | Total |
|---|---|---|---|
| Lived | 238 | 5,136 | 5,374 |
| Died | 6 | 844 | 850 |
| Total | 244 | 5,980 | 6,224 |

- Probability a non-inoculated person died from smallpox:
  $$\mathbb{P}(\text{died}|\text{not inoculated}) = \frac{\mathbb{P}(\text{died} \cap \text{not inoculated})}{\mathbb{P}(\text{not inoculated})} = \frac{0.1356}{0.9608} \approx 0.1411$$

- Probability an inoculated person died from smallpox:
  $$\mathbb{P}(\text{died}|\text{inoculated}) = \frac{\mathbb{P}(\text{died} \cap \text{inoculated})}{\mathbb{P}(\text{inoculated})} = \frac{0.0010}{0.0392} \approx 0.0246$$

### Bayes' Theorem
- **Formula**:
  $$\mathbb{P}(A|B) = \frac{\mathbb{P}(B|A)\mathbb{P}(A)}{\mathbb{P}(B)}$$

- When ℙ(B) is not directly accessible:
  $$\mathbb{P}(B) = \sum_i \mathbb{P}(B|A_i)\mathbb{P}(A_i)$$
  where A<sub>i</sub> ∩ A<sub>j</sub> = ∅ for i ≠ j and ∪<sub>i</sub> A<sub>i</sub> = Ω

### Example: Bayes' Theorem with Smallpox Data
Using the smallpox data to find the probability that a person who died was not inoculated:
$$\mathbb{P}(\text{not inoculated}|\text{died}) = \frac{\mathbb{P}(\text{died}|\text{not inoculated})\mathbb{P}(\text{not inoculated})}{\mathbb{P}(\text{died})} = \frac{0.1411 \times 0.9608}{0.1366} \approx 0.993$$

## 3. Random Variables

### Definition and Types
- **Random Variable**: A function from the sample space Ω to another set (typically ℝ or ℕ)
- **Discrete Random Variable**: Takes values from a countable set
- **Continuous Random Variable**: Takes values from an uncountable set (typically an interval of real numbers)

### Example: Coin Tossing
For a sequence of 3 coin tosses:
- Sample space: Ω = {(H,H,H), (H,H,T), (H,T,H), (H,T,T), (T,H,H), (T,H,T), (T,T,H), (T,T,T)}
- Random variable X = number of heads in the sequence
- For ω = (H,H,T), X(ω) = 2

## 4. Probability Distributions for Discrete Random Variables

### Probability Mass Function (PMF)
- **Definition**: A function p<sub>X</sub>: ℝ → [0,1] that gives the probability that a discrete random variable equals a specific value
- **Formula**: p<sub>X</sub>(a) = ℙ(X = a)
- **Properties**:
  - p<sub>X</sub>(x) ≥ 0 for all x
  - Σ<sub>x</sub> p<sub>X</sub>(x) = 1

### Example: Fair Coin Toss
For a random variable X associated with a fair coin toss (X = 1 for heads, X = 0 for tails):
$$p_X(x) = \begin{cases}
1/2 & \text{if } x = 0 \\
1/2 & \text{if } x = 1 \\
0 & \text{otherwise}
\end{cases}$$

## 5. Probability Distributions for Continuous Random Variables

### Cumulative Distribution Function (CDF)
- **Definition**: A function F<sub>X</sub>: ℝ → [0,1] that gives the probability that a random variable is less than or equal to a specific value
- **Formula**: F<sub>X</sub>(x) = ℙ(X ≤ x)
- **Properties**:
  - 0 ≤ F<sub>X</sub>(x) ≤ 1
  - lim<sub>x→-∞</sub> F<sub>X</sub>(x) = 0
  - lim<sub>x→+∞</sub> F<sub>X</sub>(x) = 1
  - x ≤ y ⟹ F<sub>X</sub>(x) ≤ F<sub>X</sub>(y) (non-decreasing)
  - ℙ(a ≤ X ≤ b) = F<sub>X</sub>(b) - F<sub>X</sub>(a)

### Probability Density Function (PDF)
- **Definition**: For a continuous random variable with a differentiable CDF, the PDF is the derivative of the CDF
- **Formula**: f<sub>X</sub>(x) = d/dx F<sub>X</sub>(x)
- **Properties**:
  - f<sub>X</sub>(x) ≥ 0
  - ∫<sub>-∞</sub><sup>∞</sup> f<sub>X</sub>(x)dx = 1
  - For a set A, ∫<sub>A</sub> f<sub>X</sub>(x)dx = ℙ(X ∈ A)
  - ℙ(a ≤ X ≤ b) = ∫<sub>a</sub><sup>b</sup> f<sub>X</sub>(x)dx
  - F<sub>X</sub>(x) = ∫<sub>-∞</sub><sup>x</sup> f<sub>X</sub>(z)dz
  - Important: In general, f<sub>X</sub>(x) ≠ ℙ(X = x)

### Example: Uniform Random Variable
For a uniform random variable on [0,1]:
$$f_X(x) = \begin{cases}
1 & \text{if } x \in [0,1] \\
0 & \text{otherwise}
\end{cases}$$

The CDF is:
$$F_X(x) = \begin{cases}
0 & \text{if } x < 0 \\
x & \text{if } 0 \leq x \leq 1 \\
1 & \text{if } x > 1
\end{cases}$$

## 6. Expectation, Variance, and Standard Deviation

### Expectation (Expected Value)
- **For Discrete Random Variables**:
  $$\mathbb{E}(X) = \sum_{x \in S} x \cdot p_X(x)$$

- **For Continuous Random Variables**:
  $$\mathbb{E}(X) = \int_{-\infty}^{\infty} x \cdot f_X(x) dx$$

- **For Functions of Random Variables**:
  - Discrete: 𝔼(g(X)) = Σ<sub>x∈S</sub> g(x) · p<sub>X</sub>(x)
  - Continuous: 𝔼(g(X)) = ∫<sub>-∞</sub><sup>∞</sup> g(x) · f<sub>X</sub>(x) dx

### Example: Expected Value of a Die Roll
For a fair six-sided die:
$$\mathbb{E}(X) = \sum_{i=1}^{6} i \times \frac{1}{6} = \frac{1}{6} + \frac{2}{6} + \frac{3}{6} + \frac{4}{6} + \frac{5}{6} + \frac{6}{6} = \frac{21}{6} = 3.5$$

### Example: Expected Value of a Uniform Random Variable
For a uniform random variable on [0,1]:
$$\mathbb{E}(X) = \int_{-\infty}^{\infty} x \cdot f_X(x) dx = \int_{0}^{1} x \cdot 1 \, dx = \left[ \frac{x^2}{2} \right]_{0}^{1} = \frac{1}{2}$$

### Linearity of Expectation
- If X and Y are random variables, and a and b are constants:
  $$\mathbb{E}(a \cdot g(X) + b \cdot h(Y)) = a \cdot \mathbb{E}(g(X)) + b \cdot \mathbb{E}(h(Y))$$

### Example: Linearity of Expectation
If the expected sales price of an apple is $1 and an orange is $2, then the expected sales price of 2 apples and 3 oranges is:
$$\mathbb{E}(2 \cdot \text{apple price} + 3 \cdot \text{orange price}) = 2 \cdot \mathbb{E}(\text{apple price}) + 3 \cdot \mathbb{E}(\text{orange price}) = 2 \times \$1 + 3 \times \$2 = \$8$$

### Variance and Standard Deviation
- **Variance**: Measures the spread or dispersion of a random variable around its mean
  $$\text{Var}(X) = \mathbb{E}((X - \mu)^2) = \mathbb{E}(X^2) - \mu^2$$
  where μ = 𝔼(X)

- **Standard Deviation**: Square root of the variance
  $$\sigma = \sqrt{\text{Var}(X)}$$

### Example: Variance of a Die Roll
For a fair six-sided die with μ = 3.5:
$$\text{Var}(X) = \mathbb{E}((X - \mu)^2) = \sum_{i=1}^{6} (i - 3.5)^2 \times \frac{1}{6} = \frac{105}{36} \approx 2.92$$
$$\sigma = \sqrt{\frac{105}{36}} \approx 1.71$$

### Example: Variance of a Uniform Random Variable
For a uniform random variable on [0,1] with μ = 1/2:
$$\text{Var}(X) = \mathbb{E}((X - \mu)^2) = \int_{0}^{1} (x - \frac{1}{2})^2 dx = \frac{1}{12}$$
$$\sigma = \sqrt{\frac{1}{12}} \approx 0.289$$

### Properties of Variance
- For independent random variables X and Y, and constants a and b:
  $$\text{Var}(a \cdot g(X) + b \cdot h(Y)) = a^2 \cdot \text{Var}(g(X)) + b^2 \cdot \text{Var}(h(Y))$$

## 7. Practical Examples

### Example 1: Card Drawing
For a standard deck of 52 cards:
- The sample space for drawing two cards and recording their sum (Ace = 1, Jack/Queen/King = 10) is:
  {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
- The sample space for the number of spades when drawing five cards is:
  {0, 1, 2, 3, 4, 5}

### Example 2: Die Rolling and Event Independence
For a fair 6-sided die with events:
- A: The number rolled is odd = {1, 3, 5}
- B: The number rolled is greater than or equal to 4 = {4, 5, 6}
- C: The number rolled doesn't start with the letters "f" or "t" = {1, 6}

To determine if A and C are independent:
- ℙ(A) = 3/6 = 1/2
- ℙ(C) = 2/6 = 1/3
- ℙ(A ∩ C) = |{1}|/6 = 1/6
- Since ℙ(A) × ℙ(C) = (1/2) × (1/3) = 1/6 = ℙ(A ∩ C), events A and C are independent

### Example 3: Blood Type Probabilities
Given that 44% of Americans have type O blood, 42% have type A, 10% have type B, and the rest have type AB:
- Probability of not having type A blood: 1 - 0.42 = 0.58
- Probability of having type A or AB blood: 0.42 + (1 - 0.44 - 0.42 - 0.10) = 0.42 + 0.04 = 0.46

### Example 4: Betting Game Expected Value
In a betting game where you roll a die and:
- Win $200 if you get a 5 on the first roll
- Win $100 if you don't get a 5 on the first roll but get a 5 on the second roll
- Win $0 otherwise

The expected winnings are:
- ℙ(X = 200) = 1/6
- ℙ(X = 100) = (5/6) × (1/6) = 5/36
- ℙ(X = 0) = 1 - 1/6 - 5/36 = 25/36
- 𝔼(X) = 200 × (1/6) + 100 × (5/36) + 0 × (25/36) = 33.33 + 13.89 = $47.22

## 8. Key Takeaways

1. Probability provides a formal framework for quantifying uncertainty and randomness
2. The three components of a probability space are:
   - Sample space (Ω): All possible outcomes
   - Event space (ℱ): Collection of subsets of Ω
   - Probability measure (ℙ): Function assigning probabilities to events

3. Conditional probability allows us to update probabilities based on new information
4. Independence of events means the occurrence of one event doesn't affect the probability of another
5. Random variables map outcomes to numbers, allowing mathematical analysis
6. Probability distributions describe the likelihood of different values of a random variable:
   - PMF for discrete random variables
   - PDF and CDF for continuous random variables

7. Expected value represents the long-run average of a random variable
8. Variance and standard deviation measure the spread or dispersion around the expected value
9. Linearity of expectation and properties of variance simplify calculations for combinations of random variables