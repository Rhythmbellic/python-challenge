#here we will plot graph of brownian movement and how it is plotted
import numpy as np
import matplotlib.pyplot as plt
def main(data):
    n=1000
    T=1.
    times=np.linspace(0.,T,n)
    dt=times[1]-times[0]
    dB=np.random.normal(size=(n-1,))
    B0=np.zeros(shape=(1,))
    B=np.concatenate((B0,np.cumsum(dB)))
    plt.plot(times,B)
    plt.show()
    data=B
    return data

if __name__=='__main__':
    pass
print(main("a"))
