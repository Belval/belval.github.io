---
layout: post
title:  "Portable air quality sensor"
date:   2020-02-01 11:28:50 -0400
categories: hardware
---

# Making my air quality sensor portable

Recently while wondering about how to test my portable HVAC unit I asked myself how I could design a simple system to log PM2.5 and PM10 measurements in my room. I then designed an OrangePi-based solution that uses an [SNS011](https://www.aliexpress.com/item/32724933436.html) sensor. The result was not very pretty but was able to get reasonably precise values at a price point of 15$. I might go over the conception of the system itself in a later post as I believe it would be interesting, but in the meantime, there is a nice overview of the project + source code available on the [GitHub project page](https://github.com/Belval/air-quality-station).

Unfortunately, my initial design had two critical limitations: it needed a power outlet and an ethernet port to work properly. This was obviously not a problem when I only wanted to measure air quality in my room, but what about the living room or the garage? It was obvious that I would need an external power bank to provide energy to the project.

## Measuring the power draw

Since the whole system is already up and running (while plugged in the wall), I started by measuring the power draw of the OrangePi Zero + SNS011 sensor using a [USB test voltmeter](https://www.aliexpress.com/item/32571512709.html). Which came out at around 300mA@5.20V or 1.56Wh. Since I also plan to add a [CO2 sensor](https://www.aliexpress.com/item/32706795833.html) in the very near future, I have to account for its power draw too, which according to the manufacturer, is around 18mA@3.3V or 0.06Wh. Any measurement from AliExpress is not to be taken literally so I will assume for the worst and double the power consumption to 0.12Wh.

Our final power consumption is therefore of 1.68Wh.

## Part list

- 3x [TP4056 lithium battery charger module](https://www.aliexpress.com/item/32797834680.html) (1.52$ for 5)
- 1x [USB A female connector](https://www.aliexpress.com/item/Micro-Mini-USB-USB-A-Male-USB-2-0-3-0-A-Female-USB-B-Connector/33045236019.html) (0.12$)
- 6x ["Panasonic" 18650 3400mAh lithium cell](https://www.aliexpress.com/item/33016517000.html) (19.38$ for 6)
    - The linked one are NOT the one I used my seller is not offering these cells anymore. Be careful when buying lithium cells off of AliExpress.
- 2x [3 section plastic battery holder](https://www.aliexpress.com/item/33038284120.html) (0.47$)
- 1x [DC-DC Step Up Converter MT3608 Booster](https://www.aliexpress.com/item/32970333618.html) (0.58$)
- 1x [Micro USB female connector](https://www.aliexpress.com/item/4000484202812.html) (1.04$ for 10)

## DIY or buy?

The first idea that comes to mind is to buy an off-the-shelf power bank, but I had 18650 cells lying around that I had bought for another project, that never came to fruition. With an advertised capacity rating of 3400mAh, I could expect way more than the minimal 24 hours sampling period I set as my target. I also had multiple 3 cell plastic holders that can facilitate the assembly of the pack.

As my baseline, I picked an [Anker PowerCore Slim 10000](https://www.amazon.ca/Anker-Ultra-Compact-High-Speed-VoltageBoost-Technology/dp/B07QXV6N1B) which has a capacity of 10000mAh. If we trust my calculations above this gives 37Wh (little known fact, power banks are not rated at their output voltage but at the usual 3.7V lithium cell voltage).

My cell holders being in groups of three, I decided to use a six cells configuration (2 x 3 cells), for a total of 20400mAh or 75.48Wh. To charge the pack, I used three [TP4056 charging modules](https://www.aliexpress.com/item/32797834680.html), each module being responsible for two cells in parallel. This would probably be considered bad practice since it is bound to lead to an imbalance between the cells in the future, but I was not willing to wait and order more. Besides, with matching cells, there is little risk of catastrophic failure over time, simply greater chances of premature wear.

Time to pull out the soldering iron and connect all the cells, charging modules and step-up converter!

I would have to agree that it looks like a rat nest but that is due to the 6 wires needed for each charging module 2 x (charge, battery, output). To prevent short circuit risk, I 3D printed a rectangular enclosure in two pieces (my maximum print surface is only of 12x12x12cm).

## Results

| | DIY | Anker PowerCore |
|:-----:|:-----:|:-----:|
| Capacity (mAh) | 20400 | 10000 |
| Charge (mAh) | X | 12900 |
| Discharge (mAh) | X | X |

Now it is worth noting that the step-up converter used was a [TZT 0.9-5V To 5V DC-DC Step-Up](https://www.aliexpress.com/item/32807311456.html) which is undeniably garbage even at its very low price point. The efficiency of 85% is but one of its drawbacks. It actually burned during one of my tests at 300mA which below the spec'ed maximum intensity of 480mA. To replace it, I bought a bulkier [DC-DC Step Up Converter MT3608 Booster](https://www.aliexpress.com/item/32970333618.html) which goes all the way up to 2A.

## Conclusion

Coming at a price point of 21.74$ (including shipping and taxes) the DIY version beats the 30$ Anker Power Core with a comfortable margin. Now obviously this is excluding the time it took to solder the whole thing but it was a very enjoyable activity nonetheless. Furthermore, while my use case draws very little amps and therefore does not need fancy features like fast-charging, the Anker power bank supports fast charge at 3+ amps, which is not something that could be done with the current build. While the 3 TP4056 modules in parallel add up to 3 amps, they are probably not designed to run at their peak intensity for long periods.

For further reading, I would recommend [DIY Lithium Batteries by Micah Toll](https://www.amazon.ca/DIY-Lithium-Batteries-Build-Battery/dp/0989906701). He goes over most of the off-the-shelf chemistry and explains good practices.



