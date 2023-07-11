import numpy as np
import matplotlib.pyplot as plt


def aliens(F, n):
    
   
     
    F[n] = F[n-1] + F[n-2]
    return F[n]

def aliens2(F, n):
    
  
    
    if len(F) < 2:
        print(' F is not long enough')
        return(0)
    
    F.append(F[n-1]+F[n-2])
    return F[n]

if __name__ == "__main__":
    

    
    F = np.zeros(100)
    F[0] = 0
    F[1] = 1
    
    for n in range(2, 20):
        F[n] = aliens(F, n)
    
    intF = [int(x) for x in F[:20]]
    print(intF)
    

    
    F = []
    F.append(0)
    F.append(1)
    print(F)
    
    for n in range(2,19):
        F[n] = aliens2(F, n)
        print(F[n])
        

    d = F
    plt.plot(d,'.')
    
    




















