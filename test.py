import pymannkendall as mk
import matplotlib.pyplot as plt
 
gfg_data = [54, 52, 53, 59, 56, 57, 51, 52, 50, 53]
 

"""
    trend: This tells the trend-increasing, decreasing, or no trend.
    h: True if the trend is present. False if no trend is present.
    p: The p-value of the test.
    z: The normalized test statistic.
    Tau: Kendall Tau.
    s: Mann-Kendal’s score
    var_s: Variance S
    slope: Theil-Sen estimator/slope
    intercept: Intercept of Kendall-Theil Robust Line
"""

# perform Mann-Kendall Trend Test
t = mk.original_test(gfg_data)
print(t)
#plot(x,y)
plt.text(0, 8, t, fontsize = 17)
plt.plot(gfg_data)
# https://matplotlib.org/stable/tutorials/text/text_intro.html
plt.show()