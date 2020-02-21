---
layout: post
title:  "A treasure trove of untapped performance: Optimizing DL models"
date:   2020-03-01 11:28:50 -0400
categories: deeplearning
published: false
---

## What treasure trove?

For most people working on deploying deep learning models in production, there is often a need to optimize training and inference workloads. The reason is simple: P100 or V100 have a finite amount of computing power. When your load cannot scale to multiple GPUs, you cannot make your training or inference faster anymore and you have to make the whole thing more efficient. Below is my personal checklist, which cover most low-hanging fruits that I encountered in my albeit limited experience. The whole thing will be very framework agnostic, as most issues are also very framework agnostic.

## 1 CPU bottlenecks

This is unsurprisingly common in a lot of projects that I encountered, which is why it earned the first spot on my list. Always benchmark your training or inference process **FIRST**. More often than not, your GPU is sitting idle most of the time because your CPU is not feeding it any data.

Introducing [`py-spy`](https://github.com/benfred/py-spy) which is an open-source project that will happily tell you what part of your code is taking most of the CPU time. When moving "research-grade" code to production, it is very common to find a preprocessing or postprocessing function that consumes 55% of your CPU time, badly crippling your stats.

## 2 CPU-GPU data transfers

This is common and is very easy to notice. Run `watch -n 1 nvidia-smi` and look at your GPU usage. Does it oscillate between 5 and 99% every few seconds? If so look no further and 
