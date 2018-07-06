---
layout: post
title:  "Sniffing IoT: Alexa"
date:   2018-12-01 00:00:00 -0500
published: false
---

# Sniffing IoT: Alexa

There is an healthy skepticism in the computer science community whenever a business makes any claims about privacy. Since the Internet of Things is mostly aiming to add all kinds of sensors to the home of tomorrow, it sparks countless debates on how where the boundaries should be set to avoid violating the most basic privacy. While I was not very interested in the whole home assistant thing, I happened to win an Alexa Echo at work and wondered what data it was sending to Amazon.

## TLDR

From the data collected, it seems that Amazon stayed true to its word; Alexa only sends data after being summoned.

## The setup

I created an access point using the create_ap script to which I connected Alexa. I then ran tshark for about a month to get a big enough dataset to mine. 

## The results

Lets start by plotting packet count on a day-to-day basis.

[Packet-per-day here]

Unsuprisingly, the packet count is about 15% higher on weekends when I use it with a steady baseline of 40 000 packets that can probably be associated with Alexa "phoning home". Lets see instead the total byte count per day as I would expect those pings to be significantly smaller in size.

[Bytes-per-day here]

That seems coherent with my hypothesis. Now lets see what happens if we only take outbound traffic, both by packet and raw bytes count.

[Outgoing-packet-per-day here]
[Outgoing-bytes-per-day here]

