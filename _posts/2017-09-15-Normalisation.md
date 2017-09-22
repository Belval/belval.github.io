---
layout: post
title:  "Did you normalize your data?"
date:   9999-10-15 00:00:00 -0500
published: false
categories: Machine Learning
---

"You should use a cosine function instead of the euclidean distance between your vectors it gives better results" - My colleague, September 2017

Scikit did provide a cosine function, but the HDBSCAN module I was using wasn't having any of it. Raising exception and whatnot. After looking around the web, I found an old issue on the module's repo in which the owner replied "It does not work, but you can achieve the same result by applying normalization to the data".

I stared at my code, I had not applied any normalization. Worse yet, most parameters were at 0 and those that weren't tended to be between 1 and 10. I added the required code and voilà! Better clustering!

Now I believed it would be worth a couple hours of my time to come up with a definitive explanation of why it is **very** important to normalize the data before doing most kind of analysis **when the dataset has high dimensionality**. All code snippets and samples are available on my GitHub page.

Before diving straight into the why, let's take some very well spent time to investigate the what. What is normalization and why should we/you care? A simplified explanation would be that normalization is a process through which the data is scaled to fit on a predefined range. If we picture a common "bag-of-word" dataset that we wish to cluster using k-means (or any other clustering algorithm really).

We have a simple dataset that we wish to cluster
