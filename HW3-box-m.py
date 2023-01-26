from Random_HW3 import Random
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    seed=5555
    random_number = Random(seed)
    y1 =[]
    for i in range(0,10000):
        y1.append(random_number.BoxM())
    #plot histogram    
    n, bins, patches = plt.hist(y1, 50, density=True, facecolor='red', alpha=0.75, ec='black')
    # plot formating options
    plt.xlabel('y1')
    plt.ylabel('Probability')
    plt.title('Box-Muller transform-1')
    plt.grid(True)
    plt.savefig('plot1.pdf')
    # show figure (program only ends once closed
    plt.show()

    #plot histogram 
    
    y2 =[]
    for i in range(0,10000):
        y2.append(random_number.BoxM())
    n, bins, patches = plt.hist(y2, 50, density=True, facecolor='blue', alpha=0.75, ec='black')
    plt.xlabel('y2')
    plt.ylabel('Probability')
    plt.title('Box-Muller transform-2')
    plt.grid(True)
    plt.savefig('plot2.pdf')
    plt.show()
