#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:38:53 2018

@author: nishithapaidimukkala
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams['figure.figsize'] =(16,9)

# creating a sample data set with 4 clusters

X , y = make_blobs(n_samples=800, n_features=3, centers=4)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:,1], X[:, 2])


#Intiating KMeas
kmeans = KMeans(n_clusters=4)
#Fitting with imputs
kmeans = kmeans.fit(X)
#Predicting  the clusters
labels = kmeans.predict(X)
#Getting the cluster centers
C = kmeans.cluster_centers_

fig = plt.figure()
ax= Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)