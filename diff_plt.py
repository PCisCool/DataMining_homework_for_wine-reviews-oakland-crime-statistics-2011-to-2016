import matplotlib.pyplot as plt
import pandas as pd

def diff_hist(data1,data2):

    fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(12, 8))
    # 调整子图位置
    plt.subplots_adjust(hspace=0)


    data1.value_counts().head(10).plot.bar(ax=ax0)

    ax0.grid()

    data2.value_counts().head(10).plot.bar(ax=ax1)
    ax1.grid()
    plt.show()

