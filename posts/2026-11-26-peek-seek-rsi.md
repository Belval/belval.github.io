---
title: I asked an agent to find my printer. It rewrote its camera tool.
date: 2026-11-26
slug: peek-seek-rsi
excerpt: A $25 camera took 2.4 seconds to answer every time the agent looked. Keeping the stream open brought that down to 1.63 milliseconds.
hero: /assets/peek-and-seek.png
---

I wanted to see how good a coding agent would be at finding things in my office, mostly because I already had a Tapo C210 and figured that if I gave it a way to turn the camera and get a picture back, it should have everything it needed to find something reasonably obvious like my 3D printer. What I hadn’t accounted for was that every time it wanted to check whether it had turned far enough, it had to wait another 2.4 seconds for a picture. At that point I was more interested in why a camera that does 15 fps needed two seconds to give me one frame.

The useful number here is 15 fps, because it means the camera has another frame roughly every 67 ms whether the agent asks for one or not. Our Python implementation would open the stream, get one of those frames and close it, so the next call got to do all of that again. The agent rewrote the server in Rust and left a reader running between calls, which brought the median down to 1.63 ms (for the latest frame already in memory, in case anyone is wondering what firmware I put on this thing).

![A persistent RTSP reader feeds a shared latest-frame buffer. Each MCP request reads the preview already there.](/assets/rust-pipeline.png)

We rebuilt the Python and Rust versions and timed 100 warm snapshot calls on each, using the same camera. ONVIF still handles the pan and tilt commands. The connection we kept opening and closing was RTSP, the one carrying the video. [Per-commit measurements](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/commit-history)

## A second camera makes a decent test harness

Once the agent had found the printer, asking it to find the printer again seemed like a fairly generous test, so we had two agents play I Spy. Peek picked something in the room and kept the coordinates to itself, which meant Seek had to move its own camera and bring back a picture that somebody else could judge. Both cameras have googly eyes, a small hardware modification that makes having two of them looking around my office feel considerably less creepy.

![Peek withholds the object's coordinates. Seek searches, checks the image and timings, patches its tools, and tries a fresh target. Seven games and 216 motion trials supplied feedback.](/assets/improvement-loop.png)

We ended up with seven independently judged games and 216 timed motion trials. The part I like about this setup is that Seek could edit the very tool it had just used, and on the next round we could check the picture as well as the timing. Cutting a wait is easy enough if nobody checks where the camera landed. [Trial records](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/i-spy)

## What was left to speed up in Rust?

Take two images and ask the tracker where nine points went between them. All nine answers depend on features extracted from the same two images, and we were paying to extract those features again for each point. The agent attached the features to the frames that owned them, so after the first point the other eight could reuse the work.

![Nine-point tracking on the same frame pair fell from 350 to 74 milliseconds when all nine points shared the two frames’ cached features.](/assets/tracking-reuse.png)

On the same pair of test images, those nine answers took **74 ms instead of 350 ms**, and we checked that the coordinates agreed. The gain on a live preview call was smaller. Faster trace scanning and SIMD base64 encoding brought the median from **1.70 to 1.54 ms** over 600 requests per release, with tracing enabled and the agent’s thinking time excluded. I doubt I could spot those last 0.16 ms while looking for the printer, but I could certainly spot the two seconds we used to spend reconnecting every time I wanted to know where it was. [Benchmarks and raw traces](https://github.com/Belval/onvif-mcp/tree/ddc847f/benchmarks/mcp-optimization)
