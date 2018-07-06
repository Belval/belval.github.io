---
layout: post
title: "Implementing papers for fun and profit"
date: 2018-07-01 00:00:00 -0500
description: "Often in ML, reading a lot of paper can give you the impression that you have a good grasp of the concept and that you \"understand\" the topic. In my experience however, implementing paper can be a better way to gain precious insights."
published: false
---

# Implementing papers for fun and profit

Full disclaimer, the "profit" part is not a real thing, unless you see it as "intellectual profit" but that's a little bit too cheesy for me. While it is relatively widely known that you learn a lot more by doing than by simply reading, it is not given that you will have the self-awareness to stop and reflect on whether you truly grasped the concepts and ideas conveyed or if you *mindlessly* skimmed through without a second thought.

In my case, I was in the second group for a long time and I still am from time to time. To avoid this, I started implementing (or reimplementing) the architectures I read about. Most of the time I end up gaining precious insights and that is without considering the added value of perfectionning my skills with the framework I happen to be using.

## Finding the right paper

Obviously not all papers are easy to implement or even implementable at all. You should always ask yourself the following questions:

1. Is there data available to reproduce the results shown?
2. Is the model trainable or did it take 3 months to converge on 200 TPUs in Google Cloud?
3. Is there enough information given on the architecture to reimplement it or did the author(s) forget crucial information?
4. Do you have enough interest to carry the whole development through?

The two first points are a must, you cannot train without data and you cannot train if it takes Google-level infrastructure. The third one is a bit more flexible as you can conduct your own experiments to fill the gap or even contact the author(s) directly. I found that most of the time they will be very open to help if the questions are precise enough. 

The fourth and last point depends entirely on you and how much free time you have. A few hours can go a long way but if you get stuck and need to work even harder to figure out a solution you will need every ounces of determination to carry on.

## Writing and reusing the boilerplate code

For the unadept, "boilerplate" is the term used by developers when talking about what you need to bootstrap a project. This 