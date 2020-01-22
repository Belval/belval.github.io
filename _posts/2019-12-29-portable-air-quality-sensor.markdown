---
layout: post
title:  "Portable air quality sensor"
date:   2020-03-22 11:28:50 -0400
categories: hardware
---

# Portable air quality sensor

Recently while wondering about how to test my [portable hvac unit]() I wondered how I could design a simple system to measure and save PM2.5 and PM10 measurements in my room. I then designed an OrangePi-based solution that uses an [SNS011](https://www.aliexpress.com/item/32724933436.html) sensor. The result was not very pretty, but was able to get reasonably precise values at a dirt cheap price of 15$. I might go over the conception of the system itself in another post as I believe it would be interesting, but in the meantime, there is a nice overview of the project + source code available on the [GitHub project page](https://github.com/Belval/air-quality-station).

Speaking with friends about the project, I was hit by requests to measure **their** air quality. I found the idea interesting, but my current setup could not be moved easily as it used a wall charger as its power supply and an ethernet cable as its internet connection, both thing that are not always available.

## Measuring the power draw

Since the whole system is already up and running (while plugged in the wall), I started by measuring the power draw of the OrangePi Zero + SNS011 sensor using a [USB test voltmeter](https://www.aliexpress.com/item/32571512709.html). Which came out at around 300mA@5.20V or 1.56Wh. Since I also plan to add a [CO2 sensor](https://www.aliexpress.com/item/32706795833.html) in the very near future, I have to account for its power draw too, which according to the manufacturer, is around 18mA@3.3V or 0.06Wh. Any measurements from AliExpress is not to be taken litteraly so I will assume for the worst and double the power consumption to 0.12Wh.

Our final power consumption is therefore of 1.68Wh.

## DIY or buy?

First idea that comes to mind is to buy an off-the-shelf powerbank, but custom lithium battery packs are a fun introduction to the reasonably complex world energy storage. I had ten 18650 cells lying around that I had bought for another project, that never came to fruition. With an advertised capacity rating of 3400mAh, I could expect way more than the minimal 24 hours sampling period I set as my target. I also had multiple 3 cells platic holders that can facilitate the assembly of the pack.

As my baseline, I picked an [Anker PowerCore Slim 10000](https://www.amazon.ca/Anker-Ultra-Compact-High-Speed-VoltageBoost-Technology/dp/B07QXV6N1B) which has a capacity of 10000mAh. If we trust my calculations above this gives 37Wh (little known fact, powerbanks are not rated at their output voltage but at the usual 3.7V lithium cell voltage).

My cell holders being in groups of three, I decided to use a six cells configuration (2 x 3 cells), for a total of 20400mAh or 75.48Wh. To charge the pack, I had three [TP4056 charging modules](https://www.aliexpress.com/item/32797834680.html), each module charging two cells in parallel. This would probably be considered a bad practice, but I was not willing to wait and order more. Besides, with matching cells, there is little risk of catastrophic failure over time, simply greater chances of premature wear.

<center>
<img src="{{ site.baseurl }}/imgs/2_result.jpg" alt="an-unusable-cover" width="350" />
<img src="{{ site.baseurl }}/imgs/2_opened.jpg" alt="opened" width="350" />
</center>

Time to pull out the soldering iron and connect all the cells, charging modules and step-up converter:

<center>
</center>

I would have to agree that it looks like a rat nest but that is due to the 6 wires needed for each charging module 2 x (charge, battery, output). To prevent short circuit risk, I 3D printed a rectangular enclosure in two pieces (my maximal print surface is too small).




DIY:

Charge: 12900mAh@5.20V
Discharge: 






