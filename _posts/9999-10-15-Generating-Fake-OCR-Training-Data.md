---
layout: post
title:  "Generating Fake OCR Training Data"
date:   9999-10-15 00:00:00 -0500
categories: Synthetic Data Generation
---

# Generating Fake OCR Training Data

```
  OCR stands for Optical Character Recognition, reading text in images.
```

While I was developping my CRNN for text recognition, I found myself in a situation where I needed prodigious amounts of visual text for training.

Most of the datasets I could find were unsuitable and did not offer the flexibility I was looking for. The end goal being to craft an homemade OCR to turn scanned pages into strings, I needed various lengths, fonts, backgrounds, skews and characters. Using Pillow and OpenCV I decided to solve the challenge myself.

## How would it work?

As described above, I wanted (and frankly needed)

- More than 100 000 samples
- Various word count
- Skewing
- Random backgrounds
- Random fonts

But also to be able to change those settings every generation without meddling with a config file. A CLI seemed in order and the excellent argparse module of Python definitely was a perfect candidate.

## Introducing FakeTextDataGenerator

FakeTextDataGenerator is able to produce as many images as needed in a short time with a plethora of parameters to tailor it to your need. Let's dive in

### Parameters

For an up-to-date list, simply do `python run.py -h` (Python 3)

| Flag | Description | Default value |
|---|---|--|
| output_dir | The directory where the images will be saved if it is not specified. | `'out/'` |
| -\-input-file | Specify a text file containing the strings to use to create the images. It is expected that each line will be an image. If you specify a `--count` that is higher than the number of line in the file, it will loop through it. | |
| -\-language (-l) | Specify a language to use (to pick the word randomly from). Obviously this does not apply if you use `--input-file`. | `'eng'` |
| -\-count (-c) | Specify how many images should be generated. | `1000` |
| -\-include_numbers (-n) | Specify if the text in the images should include numbers. This is not implemented yet. | `False` |
| -\-include_symbols (-s) | Specify if the text in the images should include symbols. This is not implemented yet. | `False` |
| -\-length (-w) | Specify how many words should be included in each strings used to generate an image. If you add `--use-wikipedia` this becomes a MINIMUM. | |
| -\-random (-r) | Specify if the produced string will have variable word count (with `--length` being the maximum). It can go as low as 1. | `False` |
| -\-format (-f) | Specify the output height. 32 means 32 pixels. | `32` |
| -\-thread_count (-t) | Specify how many threads should be used for generating the images. | |
| -\-extension | Specify the image extension (jpg, png, bmp, etc...). This is used by Pillow so any supported extension [here](http://pillow.readthedocs.io/en/3.4.x/handbook/image-file-formats.html) should work. | `'jpg'` |
| -\-skew_angle (-k) | Specify the maximum skew angle, will be applied as k or -k so it goes both way. | `0` |
| -\-random_skew (-rk) | Specify if the skewing will be random in the interval [-k, k] | `False` |
| -\-use-wikipedia (-wk) | Specify if random sentences from Wikipedia should be used to generate the strings. | `False` |

### Cheatsheet
