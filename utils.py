import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def get_data1():

    mean2 = [0,0]
    cov2 = [[1,-0.8],[-0.8,1]]
    mean1 = [1,1]
    cov1 = [[1,0.0],[0.0,1]]

    x1,x2 = np.random.multivariate_normal(mean1, cov1, 100).T
    y = [0]*100


    x12,x22 = np.random.multivariate_normal(mean2, cov2, 150).T
    x1 = list(x1)
    x2 = list(x2)
    x1.extend(list(x12))
    x2.extend(list(x22))
    y.extend([1]*150)
    y = list(y)

    data = np.array([x1,x2,y]).T

    df = pd.DataFrame(data, columns=['x1', 'x2', 'y'])

    df = df.sample(frac=1).reset_index(drop=True)

    return df



def plot_2d(X,Y):
    return 1
