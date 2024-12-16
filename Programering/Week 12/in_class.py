import numpy as np

po2_list=np.array([2]).astype(int)

def po2(n):
    for i in range(1,n+1):
        liste_med_2=np.array(i*po2_list)
        print(po2_list)

po2(3)