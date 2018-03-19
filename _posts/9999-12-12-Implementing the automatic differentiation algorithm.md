---
layout: post
title:  "Implementing the automatic differentiation algorithm"
date:   2018-12-01 00:00:00 -0500
published: false
---

# Implementing the automatic differentiation algorithm

Ever wondered how TensorFlow successfully compute the derivative of all the functions in the graph to successfully apply backpropagation to the most complex neural networks without complaining? It does so by using an algorithm known as automatic differentiation which is itself using the chain rule of calculus. For the sake of limiting the length of the article, I will assume prior knowledge of calculus.

The chain rule is a formula that allows one to compute the derivative of a composition of function. Succinctly, $$(f \circ g)'(x) = f'(g(x))g'(x)$$ or $$F'(x) =  f'(g(x))g'(x)$$ for $$F(x) = f(g(x))$$. You can see this as a way to break down a rather hard-to-derive function into two smaller chunks.

Back to automatic differentiation, since everything is usually easier with an exemple, let's consider the much used an easy to comprehend example of backpropagation in a small ANN.

Picture a 4 layers neural net with this configuration:

For the sake of the example, let's say the second layer's nodes uses ReLU for an activation function, the third's are sigmoid and the last is softmax. The backpropagation algorithm allows us to calculate the gradient based on the error.

## Sources

Atilim Günes Baydin and Barak A. Pearlmutter. **Automatic differentiation of Algorithms for Machine Learning**. National University of Ireland https://arxiv.org/pdf/1404.7456.pdf (2014)
