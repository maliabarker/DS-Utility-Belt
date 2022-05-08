* Descriptive Statistics: Summarizes or describes the characteristics of a dataset, consists of measures of central tendency and measures of variability (or spread). Tells us about the proportion of data we’re currently working with, can be representative of entire population or a sample of the population.
* Inferential Statistics: Can guide us to evaluate patterns and behaviors across data we don’t have access to. Allows you to make predictions from sample of data that apply to the generalized population.
* Z-Scores: A measure of how many standard deviations below or above the population mean a raw score is. Associated with normal distributions.
![normal distribution with z scores](https://github.com/maliabarker/DS-Utility-Belt/blob/main/imgs/z_scores.png?raw=true)
* Hypothesis Tests: Allows you to verify whether a deviance is statistically significant enough to say that it’s most likely not a result of chance/randomness (reject the null hypothesis). Allows you to draw conclusions about a sample of data that can allow you to infer about similar patterns across a larger population.
* P-Value: The probability of our test statistic arising by chance.
* α-Value: A proportional value indicating the level/degree of significance upon which we can accept/reject the null hypothesis.
![examples of alpha values and p values](https://github.com/maliabarker/DS-Utility-Belt/blob/main/imgs/p_value.png?raw=true)
* One-Tailed Test: Hypothesis test that tests one sampling group against some set of population statistics.
* Two-Tailed Test: Hypothesis test that test statistics of two sampling groups against each other.
![examples of alpha values and p values](https://github.com/maliabarker/DS-Utility-Belt/blob/main/imgs/tail_tests.png?raw=true)
* Z-Distributions: Otherwise known as normal distributions or bell curves. Represent data that is classically normalized, aka symmetric across the mean and incrementable via the 68-95-99.7 Rule by z-score.
* T-Distributions: Occurs when given data would be normally distributed, but there exist too few samples to create an effective bell-curve-like distribution (under 30 samples).
* Normality Tests: Hypothesis test that quantitatively evaluates how “normal” a specific dataset is by verifying the spread, central tendency, and symmetric curvature of a Gaussian distribution. (Shapiro-Wilk Test, D’Agostino’s K^2 Test, and the Anderson-Darling Test.)
* Correlation Tests: Hypothesis test used to assess the value and strength of the correlation between two independent variables (Pearson’s Correlation Coefficient Test, the Spearman’s Rank Correlational Test, the Kendall’s Rank Correlational Test, and the Chi-Squared Test).
* Stationarity Tests: Works with time-series data. Determines a score that indicates how strongly the data changes over time (Dickey-Fuller Unit Root Test and the Kwiatowski-Phillips-Schmidt-Shin (KPSS) Test).
* Parametric Test: Hypothesis test used to generalize our samples into a population distribution and infer off of general patterns (Z-test, the Student’s t-test, the Paired Student’s t-test, and the Analysis of Variance (ANOVA) test).
* Non-Parametric Test: Hypothesis test used when you either know so little about your data that you cannot effectively parametrize a relevant population, or you’re simply working with data whereupon population phenomena are irrelevant (Mann-Whitney U Test, the Wilcoxon Signed-Rank Test, the Kruskal-Wallis H Test, and the Friedman Test.)

*For more information on statistical tests (including python code to run these tests) go to https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/*