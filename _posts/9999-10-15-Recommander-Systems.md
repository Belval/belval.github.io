---
layout: post
title:  "5 minutes read: Recommander Systems"
date:   9999-10-15 00:00:00 -0500
categories: Recommandation system
---

Recommander systems are used extensively on every "big" website. Internet's current business model being centered around targeted advertisement, using an intelligent model that uses its knowledge of the client (and of its others clients) to offer the right product at the right time is the smart thing to do.

But how does it work? What are the state-of-the-art algorithms? There are countless papers covering the subject (and listed below). I took the time to read as many as I could to provide a quick reference and ultimately, orient further investigation into this arguably complex yet incredibly interesting branch of machine learning.

Without further due, lets dive in.

###  Collaborative Filtering

Arguably older yet simple and powerful, collaborative filtering works by predicting a user's rating based on the rating of other users with similar rating profiles.

| Name | R1 | R2 | R3 | R4 | R5 |
|--|--|--|--|--|--|
| U1 | 10 | 9 | 8 |
| U2 |  | 2 | 9 | 8 |
| U3 | 4 | 6 |  | 9 |
| U4 | 9 | 9 | 8 | 10 |

Here, U* are users and R* are ratings on ten. Keep in mind that in real-life scenario, whoever is designing the system will try to have more than five users and five items.

We are a company and we want to predict what U1's R4 will be. We can predict that there are very good chances that he will give it a rating of 8 and above based on the other three users that praised it. The actual value will be computed using the following equation:

\[U1\_R4 = \]
