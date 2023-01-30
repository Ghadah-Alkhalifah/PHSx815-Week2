# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt


# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    #plot histogram for array (times)    
    n, bins, patches = plt.hist(times, 50, density=True, facecolor='red', alpha=0.75, histtype='bar', log=True)
    # plot formating options
    plt.xlabel('Time between missing cookies[days]')
    plt.ylabel('Probability')
    plt.title('rate of 1.5 cookies/day')
    plt.grid(True)
    plt.savefig('plot1.png')
    # show figure (program only ends once closed
    plt.show()

    # calculating the quantiles of the sorted array (times_avg)
    Q1= np.quantile(times_avg, .135)
    Q2= np.quantile(times_avg, .34)
    Q3= np.quantile(times_avg, .50)
    Q4= np.quantile(times_avg, .68)
    Q5= np.quantile(times_avg, .975)
    
    

    #plot histogram for array (times_avg)
    n, bins, patches= plt.hist(times_avg, 50, density=True, facecolor='skyblue', alpha=0.75, log=True)
    
    # adding lines to show quantiles and texts to the histogram
    plt.axvline(Q1, color='r', linestyle='dashed', linewidth=2, label="-2 $\sigma$")
    plt.text(Q1, plt.ylim()[1]*0.5, "-2 $\sigma$", rotation=90, color='black', fontsize=10)
    plt.axvline(Q2, color='r', linestyle='dashed', linewidth=2, label="-1 $\sigma$")
    plt.text(Q2, plt.ylim()[1]*0.5, "-1 $\sigma$", rotation=90, color='black', fontsize=10)
    plt.axvline(Q3, color='g', linestyle='dashed', linewidth=2, label='median')
    plt.text(Q3, plt.ylim()[1]*0.3, 'median', rotation=90, color='black', fontsize=10)
    plt.axvline(Q4, color='r', linestyle='dashed', linewidth=2, label="+1 $\sigma$")
    plt.text(Q4, plt.ylim()[1]*0.5, "+1 $\sigma$", rotation=90, color='black', fontsize=10)
    plt.axvline(Q5, color='r', linestyle='dashed', linewidth=2, label="+2 $\sigma$")
    plt.text(Q5, plt.ylim()[1]*0.5, "+2 $\sigma$", rotation=90, color='black', fontsize=10)

    # plot formating options
    plt.xlabel('Average time between missing cookies [days]')
    plt.ylabel('Probability')
    plt.title('averge time', fontweight ="bold")
    plt.grid(True)
    plt.legend()
    plt.savefig('plot2.png')
    # show figure (program only ends once closed
    plt.show()


