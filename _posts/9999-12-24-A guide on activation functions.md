---
layout: post
title:  "A guide on activation functions"
date:   2018-07-01 00:00:00 -0500
description: "From the venerable tanh to the very popular ReLU and the mostly unknown PReLU, this guide is meant as a quick overview of some notable functions presented through the years" 
published: false
---

# A guide on activation functions

## What are activation functions

## Activation functions

An activation function is missing from the list? Send me an email at blog@belval.org with its introduction paper an I will update the post.

The idea of doing a TLDR on activations function came from this excellent paper by Bing Xu and al. on rectified activation. While my approach is, I hope, easier to understand for people without a PhD, it is a very good read which goes in depth into ReLU, LReLU, PReLU and RReLU and tests it in a CNN.

https://arxiv.org/pdf/1505.00853.pdf

### ReLU (Rectified Linear Unit) - 2010

$$f(x) = max(0, x)$$

$$f'(x) = \begin{cases}0, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/ReLU.png'](/assets/img/activation_functions/ReLU.png)
{:center}

By far the most known and the most used, ReLU is an activation function that for any given input X below 0 will return 0. Concisely, its formula is f(x) = max(0, x). While the concept itself of an asymmetric function as a better way to model the neuron draws its source from a paper published in *Nature* in 2000. The name *Rectified Linear Unit* was coined by Goeffrey Hinton and Vinod Nair in 2010 in their paper "Rectified Linear Unit Improve Restricted Boltzmann Machines".

It gained in popularity for being simple, fast and easy to optimize.

- http://www.ini.uzh.ch/admin/extras/doc_get.php?id=41838 (First mention)
- https://papers.nips.cc/paper/1793-permitted-and-forbidden-sets-in-symmetric-threshold-linear-networks.pdf (Second mention)
- http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.165.6419&rep=rep1&type=pdf (First ReLU)
- http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf (Strengths of ReLU)


### ReLU 6 (Rectified Linear Unit 6) - 2010

$$f(x) = min(max(0, x), 6)$$


$$f'(x) = \begin{cases}0, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/ReLU6.png'](/assets/img/activation_functions/ReLU6.png)
{:center}

Picture a ReLU, now set the maximum output at 6, now you have a ReLU6! In the original paper, the authors justify the use of a ceiling as a way to "encourage the model to learn sparse features earlier".

- http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf

### LReLU (Leaky Rectified Linear Unit) - 2014

$$f(x) = max(\alpha x, x)$$


$$f'(x) = \begin{cases}\alpha, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/LReLU.png'](/assets/img/activation_functions/LReLU.png)
{:center}

A leaky ReLU is an activation unit that while very similar to a typical ReLU, tries to address the dying ReLU problem by keeping a small yet significant value for $$x \lt 0$$ this will change the derivative's value from zero to the hyperparameter $$\alpha$$. It was first introduced in the paper *Rectifier Nonlinearities Improve Neural Network Acoustic Model* by Andrew Maas, Awni Hannun, and Andrew Ng.

*"ReL units are at a potential disadvantage during optimization because the gradient is 0 whenever the unit is not active. This could lead to cases where a unit never activates as a gradient-based optimization algorithm will not adjust the weights of a unit that never activates  initially. Further, like the vanishing gradients problem, we might expect learning to be slow when training ReL networks with constant 0 gradients."* - p.2

http://web.stanford.edu/~awni/papers/relu_hybrid_icml2013_final.pdf

### PReLU (Parametric Rectified Linear Unit) - 2015

$$f(\alpha, x) = max(\alpha x, x)$$

$$f'(\alpha, x) = \begin{cases}\alpha, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/PReLU.png'](/assets/img/activation_functions/PReLU.png)
{:center}

Since the field is called machine learning, Kaiming He and al. thought to themselves "let's learn the L in LReLU instead of guessing the right value!" (not an actual quote). Thus the PReLU was born. Its creators used it in a CNN on the well-known ImageNet dataset to surpass human-level performance.

- https://arxiv.org/pdf/1502.01852

### RLReLU (Randomized Leaky Rectified Linear Unit) - 2015

$$f(x) = \begin{cases} rand() x, x \lt 0 \\ x, x \geq 0\end{cases}$$

$$f'(x) = \begin{cases}0, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/RLReLU.png'](/assets/img/activation_functions/RLReLU.png)
{:center}

Randomized ReLUs work by multiplying any sub-zero input by a small random value, sampled from a given range. The paper referenced below notes the function's ability to reduce the risk of overfitting on smaller datasets due to its random nature. It was first proposed and used in a Kaggle competition.

https://arxiv.org/pdf/1505.00853.pdf

### NReLU (Noisy Rectified Linear Unit)

$$f(x) = \begin{cases} 0, x \lt 0 \\ x + rand(), x \geq 0\end{cases}$$


$$f'(x) = \begin{cases}0, x \leq 0 \\ 1, x \gt 0 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/NReLU.png'](/assets/img/activation_functions/NReLU.png)
{:center}



### DReLU (Displaced Rectified Linear Unit)

$$f(x) = \begin{cases} -1, x \lt -1 \\ x, x \geq -1\end{cases}$$


$$f'(x) = \begin{cases}0, x \leq -1 \\ 1, x \gt -1 \end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/DReLU.png'](/assets/img/activation_functions/DReLU.png)
{:center}

### ELU (Exponential Linear Unit)

$$f(x) = \begin{cases} e^x - 1, x \lt 0 \\ x, x \geq 0\end{cases}$$

$$f'(x) = \begin{cases} f(e^x - 1) + 1, x \lt 0 \\ 1, x \geq 0\end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/ELU.png'](/assets/img/activation_functions/ELU.png)
{:center}

### SELU (Scaled Exponential Linear Unit)

$$f(\alpha, x) = \alpha \begin{cases} e^x - 1, x \lt 0 \\ x, x \geq 0\end{cases}$$

$$f'(\alpha, x) = \alpha \begin{cases} f(e^x - 1) + 1, x \lt 0 \\ 1, x \geq 0\end{cases}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/SELU.png'](/assets/img/activation_functions/SELU.png)
{:center}

### Softplus

$$f(x) = ln(1 + e^x)$$

$$f'(x) = \frac{1}{1 + e^{-x}}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/Softplus.png'](/assets/img/activation_functions/Softplus.png)
{:center}

### Softsign

$$f(x) = \frac{x}{1 + abs(x)}$$

$$f'(x) = \frac{1}{(1 + abs(x))^2}$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/Softsign.png'](/assets/img/activation_functions/Softsign.png)
{:center}

### Sigmoid - ????

$$f(x) = \frac{1}{1 + e^{-x}}$$

$$f'(x) = (1 - f(x)) f(x)$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/Sigmoid.png'](/assets/img/activation_functions/Sigmoid.png)
{:center}

### Tanh (Hyperbolic tangent) - ????

$$f(x) = tanh(x)$$

$$f'(x) = 1 - tanh^2(x)$$

{:center: style="text-align: center"}
!['/assets/img/activation_functions/Tanh.png'](/assets/img/activation_functions/Tanh.png)
{:center}
