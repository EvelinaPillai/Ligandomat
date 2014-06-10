from sklearn.decomposition import PCA
import numpy as np
import csv
import pylab as pl
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def csvRead(file):
    with open(file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile,delimiter='\t')
        list_individuals = []
        for row in reader:
            list_individuals.append(row)
    return list_individuals
            
if __name__ == '__main__':
    
    #Load data 
    rcc = csvRead("/home/eva/Dropbox/DB_QValFilter_hlas.csv")
    
    names = ['benign', 'tumor']
    classes=[]
    rccArray = []
    vals=[]
    for row in rcc:
     
      #delete names from data table 
      classes.append(int(row['class']))
      row.pop('class')
      row.pop('name')

      np_row = row.values() 
      np_row = [float(v) for v in np_row]
      rccArray.append(np_row)
      
    
    #PCA
  
    rccArray = np.asarray(rccArray)
    classes = np.asarray(classes)
    names = np.asarray(names)
   
    pca = PCA(n_components=3)
    pca.fit(rccArray)
    X = pca.transform(rccArray)
    
    #3D Plot   
    
    centers = [[1, 1], [-1, -1], [1, -1]]
    
    fig = pl.figure(1, figsize=(4, 3))
    pl.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    pl.cla()
    for name, label in [('benign', 0), ('tumor', 1)]:
        ax.text3D(X[classes == label, 0].mean(),
              X[classes == label, 1].mean() +5,
               X[classes == label, 2].mean()+5,name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
    
    # Reorder the labels to have colors matching the cluster results
    classes = np.choose(classes, [1, 0]).astype(np.float)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=classes, cmap=pl.cm.spectral)

    x_surf = [X[:, 0].min(), X[:, 0].max(),
          X[:, 0].min(), X[:, 0].max()]
    y_surf = [X[:, 0].max(), X[:, 0].max(),
          X[:, 0].min(), X[:, 0].min()]
    x_surf = np.array(x_surf)
    y_suRf = np.array(y_surf)
    v0 = pca.transform(pca.components_[0])
    v0 /= v0[-1]
    v1 = pca.transform(pca.components_[1])
    v1 /= v1[-1]

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])

    #Percentage of variance explained for each components
    print('explained variance ratio (first three components): %s'
      % str(pca.explained_variance_ratio_))
 
    #components plot
    pl.figure()
    for c, i, target_name in zip("rb", [0, 1], names):
        pl.scatter(X[classes == i,0], X[classes == i,1], c=c, label=target_name)
    pl.legend()
    pl.title('PCA of RCC dataset comp1 vs comp2')
     
    pl.figure()
    for c, i, target_name in zip("rb", [0, 1], names):
        pl.scatter(X[classes == i,0], X[classes == i,2], c=c, label=target_name)
    pl.legend()
    pl.title('PCA of RCC dataset comp1 vs comp3')
     
     
    pl.figure()
    for c, i, target_name in zip("rb", [0, 1], names):
        pl.scatter(X[classes == i,1], X[classes == i,2], c=c, label=target_name)
    pl.legend()
    pl.title('PCA of RCC dataset comp2 vs comp3')
    pl.show()
