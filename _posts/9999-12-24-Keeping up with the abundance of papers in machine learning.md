---
layout: post
title:  "Keeping up with the abundance of papers in machine learning"
date:   2018-07-01 00:00:00 -0500
description: "As a popular field that sparks a lot of interest and therefore is given a lot of funding, machine learning and especially deep learning is the topic of a prodigious amount of research papers. In this article I will introduce my personal techniques and tools I employ daily to keep up." 
published: false
---

# Keeping up with the abundance of papers in machine learning

As a popular field that sparks a lot of interest and therefore is given a lot of funding, machine learning and especially deep learning is the topic of a prodigious amount of research papers. In this article I will introduce my personal techniques and tools I employ daily to keep up.


## Use [Arxiv-sanity-preserver](https://github.com/karpathy/arxiv-sanity-preserver)

I made this my first point because frankly, if you do not know this excellent project already you have to use it as a starting point in your quest. Created by Andrej Karpathy as "a web interface that attempts to tame the overwhelming flood of papers on Arxiv". It is packed with features like sorting by popularity ("hype") which is based on retweet counts, and a very useful **Recommended** tab that keeps track of your saved papers and try to pinpoint your interest. I can hardly write enough on how fundamental this is to a good organization when reading new publications and skimming through abstracts. It is not very mobile friendly but is still better than Arxiv and most of the actual reading is done in your PDF viewer anyway.

## Check the references

Akin to link surfing on Wikipedia (although a bit less user friendly I will grant you that), take advantages of the usually rigourous use of references in papers. Most of the time a researcher will be building on other great research. A recurrent personal mistake of mine is to gloss over something unknown and keep reading. While that works from time to time. It usually ends up being a poor decision if your goal is learning. Recently while reading a rather new paper [NRTR: A No-Recurrence Sequence-to-Sequence Model For Scene Text Recognition](https://arxiv.org/pdf/1806.00926.pdf) they mentionned that their architecture was based on **Transformer**, that was introduced in [Attention is all you need](https://arxiv.org/abs/1706.03762). Reading the latter helped greatly with some key concepts in the former and most importantly helped when I tried to implement it afterwards.

## Make it part of your daily routine

Final and rather personal subpoint as I know some people do not have a routine, making the whole process part of your daily routine is the best way to ensure that you will actually start reading papers and not keep telling yourself "I should read more papers". Find a bit of recurring free time in your day (mine is when commuting), a paper with an interesting topic, and read away!

## In conclusion...

These were my three pillars to keep up with the abundance of paper in machine learning, while I believe them to be very good suggestion, you should keep in mind that above all, trying will eventually lead you to your personal tricks that might be miles away from mine.  