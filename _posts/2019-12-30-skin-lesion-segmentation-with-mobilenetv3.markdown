---
layout: post
title:  "Skin lesion analysis with MobileNetv3"
date:   2019-12-30 11:28:50 -0400
categories: computer-vision
---

# Skin lesion analysis with MobileNetv3

This post is based on a paper with the same name that may or may not be published in a near future, which explored how suitable a lightweight architecture like MobileNetv3 might be when applied to the skin lesion segmentation and classification problem.

## What is a skin lesion?

While there are probably a lot of much better resources to explain what are skin lesions, I will attempt to frame them in the context of the ISIC Challenge 2018, which aims to bolster research in machine learning applied to melanoma (skin cancer) detection.

The proper official definition is: "A skin lesion is an abnormal lump, bump, ulcer, sore or colored area on the skin. Common skin lesions include moles and actinic keratosis, among others.". For ISIC, the lesions to detect were classified among seven categories:

- Nevus
- Dermatofibroma
- Melanoma
- Pigmented Bowen's
- Pigmented Benign Keratoses
- Basal Cell Carcinoma
- Vascular

As for segmentation, is was expected to work indiscriminately for every categories.

## MobileNet v3

[MobileNetv3](https://arxiv.org/pdf/1905.02244.pdf) was introduced by Howard et al. in November this year. It is an efficient network to be deployed on highend smartphones (Pixel 3).

