---
layout: post
title:  "Comparing Clustering Algorithms on Various Tasks"
date:   9999-10-15 00:00:00 -0500
published: false
categories: Unsupervised Learning
---

# Comparing Clustering Algorithms on Various Tasks

This is meant as a quick reference on clustering algorithms, with their respective strengths and weaknesses when applied to three tasks. Most of them can be found in the scikit-learn package.

This article will cover:

- Centroid-Based Clustering
  - K-means
  - K-medoids
  - Affinity propagation
- Hierarchical Clustering
  - Agglomerative clustering
  - Birch
- Density-Based Clustering
  - DBSCAN
  - OPTICS
  - HDBSCAN
  - Mean-shift

I placed HDBSCAN into the last category as it is density based, but it is worth noting that the H stands for "Hierarchical".

## Methodology

For the sake of completeness, all the algorithms will be tested on three different datasets with various parameter count, category count and example count.

- Normalization will be applied to all datasets.
- Visualization of datasets with high parameter count will use PCA.

### Result template

- Distribution representation in 3D
- Percentage of clustered points
- Percentage of outliers
- Number of produced clusters
- Average cluster coherence ($AvgClusterCoherence =  \frac{HighestCategoryCount}{PointInClusterCount}$)

### Datasets

- Iris: A well-known arguably easy dataset with few samples
- KDDCup: A huge and unbalanced dataset (+70% of data points are DoS) with a limited category count.
- Reddit post: A custom dataset, difficult to fit and produce good clusters on as we are classifying text.

See the following comparison
| Name | Parameter count | Category count | Example count |
|--|--|--|--|
| Iris | 3 | 3 | 150 |
| KDDCup | 121 | 5 | 2 600 000 |
| 20 Newsgroup | 3000 | 20 | 18 800 |

## Centroid-Based Clustering

Clusters are based on centroid defined through a (usually) iterative method. The most common technique is k-means also known as "Lloyd's algorithm".

### K-means

### K-medoids

### Affinity Propagation

## Hierarchical Clustering

Clusters aren't absolute and will instead be defined by a tree-like structure which can be used to get various sized clusters. It is based on a distance metric computed through a function.

### Agglomerative Clustering

### Birch

## Density-Based Clustering



### DBSCAN

### OPTICS

### HDBSCAN

### Mean-Shift

## References
