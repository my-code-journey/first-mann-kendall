import csv
import pymannkendall as mk
import matplotlib.pyplot as plt

# 1: get compound names and other data related to compounds
with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
filename = open('file.csv', 'r')
file = csv.DictReader(filename)
compound_name = data[0]

def destring(arr):
    results = list(filter(None, arr))
    results = [float(i) for i in results]
    return results
            


def arrify(x):
    temp = []
    for col in file:
        temp.append(col[compound_name[x]])
    return destring(temp)

# print(arrify(3))

#2 plot compound in mann kendall

def plot(x):
    gfg_data = arrify(x)
 

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

    # Creating figure
    fig = plt.figure()
 
    # Adding axes on the figure
    ax = fig.add_subplot(111)
    heading = compound_name[x]
    #plot(x,y)
    ax.set_title(heading, fontsize=15)
    # ax.set_xlabel('Day', fontsize=12)
    # ax.set_ylabel('No of Questions', fontsize=12)

    ax.plot(gfg_data)
    # https://matplotlib.org/stable/tutorials/text/text_intro.html
    plt.show()


plot(3)