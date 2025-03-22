# DSC 215: Probability and Statistics for Data Science
## Midterm Exam Analysis and Solution Guide

## Part A: Exam Summary and Solution Guide

### Overview
This midterm exam covers material from Modules 1-4, testing students' understanding of:
- Research design and variable identification
- Descriptive statistics and data distribution
- Probability and random variables
- Normal distribution and standardization

The exam consists of 5 questions with multiple parts, totaling approximately 50 points.

### Question 1: Research Design Analysis

**Topic: Research Design and Variables (Module 1)**

This question presents a study on children's honesty and cheating behavior, asking students to:
- Identify the main research question
- Identify the subjects and sample size
- Identify variables and their types

#### Solution Guide:

**Part (a): Identify the main research question**
- The main research question is: "Does explicitly telling children not to cheat affect their likelihood to cheat?"
- This question identifies the explanatory variable (explicit instruction vs. no instruction) and the response variable (cheating behavior).

**Part (b): Identify subjects and sample size**
- Subjects: Children between the ages of 5 and 15 (or 10 and 15 in version 2)
- Sample size: 160 children (or 100 children in version 2)

**Part (c): Identify variables and their types**
Four variables were recorded:
1. Age (numerical, continuous)
2. Sex (categorical)
3. Whether they were an only child or not (categorical)
4. Whether they cheated or not (categorical)

**Key Concepts Applied:**
- Distinguishing between numerical and categorical variables
- Identifying explanatory and response variables
- Understanding research design elements

### Question 2: Descriptive Statistics and Distribution Shape

**Topic: Summarizing Data (Module 2)**

This question provides summary statistics for exam grades and asks students to:
- Determine if the distribution is left-skewed, right-skewed, or symmetric
- Identify if there are any outliers

#### Solution Guide:

**Part (a): Determine the shape of the distribution**

For Version 1:
- Mean = 78, Median = 76
- Since Mean > Median, this suggests a right-skewed distribution
- However, Q1 (60.25) is farther from the median than Q3 (86.5), which suggests left skew
- The distribution is slightly left-skewed

For Version 2:
- Mean = 80, Median = 84
- Since Mean < Median, this suggests a left-skewed distribution
- However, Q3 (95) is farther from the median than Q1 (76), which suggests right skew
- The distribution is slightly right-skewed

**Part (b): Identify outliers**

For Version 1:
- Calculate the IQR = Q3 - Q1 = 86.5 - 60.25 = 26.25
- Lower fence = Q1 - 1.5 × IQR = 60.25 - 1.5 × 26.25 = 20.875
- Upper fence = Q3 + 1.5 × IQR = 86.5 + 1.5 × 26.25 = 125.875
- Min = 30, Max = 95
- Since Min > Lower fence and Max < Upper fence, there are no outliers

For Version 2:
- Calculate the IQR = Q3 - Q1 = 95 - 76 = 19
- Lower fence = Q1 - 1.5 × IQR = 76 - 1.5 × 19 = 47.5
- Upper fence = Q3 + 1.5 × IQR = 95 + 1.5 × 19 = 123.5
- Min = 45, Max = 99
- Since Min < Lower fence, there is at least one outlier (on the lower end)

**Key Concepts Applied:**
- Relationship between mean, median, and skewness
- Interquartile range (IQR) calculation
- Outlier identification using the 1.5 × IQR rule

### Question 3: Expected Value and Variance of Random Variables

**Topic: Random Variables (Module 3)**

This question tests understanding of expected value and variance properties for independent random variables, asking students to find the mean and standard deviation of linear combinations.

#### Solution Guide:

**Properties Used:**
For independent random variables X and Y:
- E[aX + bY + c] = aE[X] + bE[Y] + c
- Var(aX + bY + c) = a²Var(X) + b²Var(Y)
- SD(aX + bY + c) = √Var(aX + bY + c)

**Version 1 Solutions:**

Given:
- E[X] = 10, SD(X) = 2, E[Y] = 20, SD(Y) = 3

Part (a): Find mean and SD of X + 3Y
- E[X + 3Y] = E[X] + 3E[Y] = 10 + 3(20) = 10 + 60 = 70
- Var(X + 3Y) = Var(X) + 9Var(Y) = 2² + 9(3²) = 4 + 9(9) = 4 + 81 = 85
- SD(X + 3Y) = √85 ≈ 9.22

Part (b): Find mean and SD of 2X - Y - 6
- E[2X - Y - 6] = 2E[X] - E[Y] - 6 = 2(10) - 20 - 6 = 20 - 20 - 6 = -6
- Var(2X - Y - 6) = 4Var(X) + Var(Y) = 4(4) + 9 = 16 + 9 = 25
- SD(2X - Y - 6) = √25 = 5

**Version 2 Solutions:**

Given:
- E[X] = 40, Var(X) = 16, E[Y] = 20, Var(Y) = 9

Part (a): Find mean and SD of 4X - 40
- E[4X - 40] = 4E[X] - 40 = 4(40) - 40 = 160 - 40 = 120
- Var(4X - 40) = 16Var(X) = 16(16) = 256
- SD(4X - 40) = √256 = 16

Part (b): Find mean and SD of X - Y
- E[X - Y] = E[X] - E[Y] = 40 - 20 = 20
- Var(X - Y) = Var(X) + Var(Y) = 16 + 9 = 25
- SD(X - Y) = √25 = 5

**Key Concepts Applied:**
- Properties of expected value for linear combinations
- Properties of variance for independent random variables
- Relationship between variance and standard deviation

### Question 4: Normal Distribution Probabilities

**Topic: Normal Distribution (Module 4)**

This question tests understanding of the normal distribution and standardization, asking students to find probabilities for normally distributed test scores.

#### Solution Guide:

**Key Formula:**
For a normal random variable X with mean μ and standard deviation σ:
- Z = (X - μ)/σ follows the standard normal distribution
- Use Z-scores to find probabilities using standard normal tables or calculators

**Version 1 Solutions:**

Given:
- Test scores are normally distributed with mean μ = 100 and standard deviation σ = 15

Part (a): Find P(X > 90)
- Z = (90 - 100)/15 = -0.67
- P(X > 90) = P(Z > -0.67) = 1 - P(Z < -0.67) = 1 - 0.251 = 0.749

Part (b): Find P(112 < X < 132)
- Z₁ = (112 - 100)/15 = 0.8
- Z₂ = (132 - 100)/15 = 2.13
- P(112 < X < 132) = P(0.8 < Z < 2.13) = P(Z < 2.13) - P(Z < 0.8) = 0.983 - 0.788 = 0.195 ≈ 0.19

**Version 2 Solutions:**

Given:
- Test scores are normally distributed with mean μ = 1500 and standard deviation σ = 300

Part (a): Find P(X < 1600)
- Z = (1600 - 1500)/300 = 0.33
- P(X < 1600) = P(Z < 0.33) = 0.629

Part (b): Find P(1200 < X < 1700)
- Z₁ = (1200 - 1500)/300 = -1
- Z₂ = (1700 - 1500)/300 = 0.67
- P(1200 < X < 1700) = P(-1 < Z < 0.67) = P(Z < 0.67) - P(Z < -1) = 0.749 - 0.159 = 0.59

**Key Concepts Applied:**
- Standardizing normal random variables
- Using Z-scores to find probabilities
- Finding probabilities for intervals

### Question 5: Probability and Independence

**Topic: Probability Concepts (Module 3)**

This question tests understanding of probability, independence, and conditional probability in the context of a classroom scenario.

#### Solution Guide:

Given:
- 20 students total
- 10 students have brown eyes (event E)
- 8 students are left-handed (event F)
- 3 students have brown eyes and are left-handed (event E ∩ F)

**Part (a): Determine if events E and F are independent**

Two events are independent if P(E ∩ F) = P(E) × P(F)

Calculate:
- P(E) = 10/20 = 0.5
- P(F) = 8/20 = 0.4
- P(E ∩ F) = 3/20 = 0.15
- P(E) × P(F) = 0.5 × 0.4 = 0.2

Since P(E ∩ F) = 0.15 ≠ 0.2 = P(E) × P(F), the events E and F are not independent.

**Part (b): Find the probability that a left-handed student does not have brown eyes**

This is asking for P(E^c | F), where E^c is the complement of E (not having brown eyes).

Method 1:
- P(E^c | F) = P(E^c ∩ F)/P(F)
- Number of left-handed students without brown eyes = 8 - 3 = 5
- P(E^c ∩ F) = 5/20 = 0.25
- P(E^c | F) = 0.25/0.4 = 5/8 = 0.625

Method 2:
- P(E^c | F) = 1 - P(E | F)
- P(E | F) = P(E ∩ F)/P(F) = 3/8 = 0.375
- P(E^c | F) = 1 - 0.375 = 0.625

The probability that a left-handed student does not have brown eyes is 5/8 or 0.625.

**Key Concepts Applied:**
- Definition of independence
- Conditional probability
- Complement of events

## Part B: Trend Analysis

### Relationship Between Exam Questions and Module Content

#### Module 1 Coverage
**Question 1** directly tests concepts from Module 1:
- Research design and methodology
- Identifying variables and their types (categorical vs. numerical)
- Understanding subjects and sampling

This question aligns with Module 1's focus on the foundations of statistics, data collection methods, and variable classification. The question tests students' ability to analyze a research study and identify its key components.

#### Module 2 Coverage
**Question 2** tests concepts from Module 2:
- Descriptive statistics (mean, median, quartiles)
- Distribution shape (skewness)
- Outlier identification using IQR

This question directly applies the concepts of summarizing numerical data, understanding distribution shapes, and identifying outliers using the 1.5 × IQR rule, which are core topics in Module 2.

#### Module 3 Coverage
**Questions 3 and 5** test concepts from Module 3:
- Expected value and variance of random variables (Question 3)
- Properties of linear combinations of random variables (Question 3)
- Probability concepts, independence, and conditional probability (Question 5)

These questions assess students' understanding of probability theory, random variables, and their properties, which are the main focus of Module 3.

#### Module 4 Coverage
**Question 4** tests concepts from Module 4:
- Normal distribution
- Standardization (Z-scores)
- Finding probabilities using the standard normal distribution

This question directly applies the concepts of the normal distribution and using Z-scores to find probabilities, which are central topics in Module 4.

### Trends and Patterns in Exam Emphasis

1. **Equal Coverage Across Modules**
   - The exam provides balanced coverage of all four modules, with approximately one question per module (with Module 3 having slightly more emphasis with two questions).

2. **Focus on Computational Skills**
   - Most questions require calculations and application of formulas rather than theoretical explanations.
   - Students need to demonstrate their ability to apply statistical concepts to solve problems.

3. **Real-World Applications**
   - Questions are framed in real-world contexts (research studies, test scores, classroom scenarios).
   - This emphasizes the practical application of statistical concepts.

4. **Multiple Versions of Questions**
   - The exam includes multiple versions of the same question with different numerical values.
   - This suggests an emphasis on understanding the underlying concepts rather than memorizing specific solutions.

5. **Progressive Difficulty**
   - The exam progresses from more straightforward conceptual questions (Question 1) to more complex computational problems (Questions 3-5).
   - This allows students to demonstrate both basic understanding and advanced application.

6. **Integration of Concepts**
   - Some questions require integrating concepts from multiple modules.
   - For example, Question 5 combines probability concepts with conditional probability.

7. **Emphasis on Core Statistical Skills**
   - The exam focuses on fundamental statistical skills that form the foundation for more advanced topics:
     - Understanding research design
     - Summarizing and interpreting data
     - Working with probability and random variables
     - Using the normal distribution

### Conclusion

The midterm exam provides a comprehensive assessment of students' understanding of the first four modules of the course. It emphasizes computational skills, application of statistical concepts to real-world scenarios, and integration of concepts across modules. The balanced coverage ensures that students have a solid foundation in the fundamental principles of probability and statistics before moving on to more advanced topics in later modules.