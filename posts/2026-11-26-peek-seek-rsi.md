---
title: I asked an agent to find my printer. It rewrote its camera driver.
date: 2026-11-26
slug: peek-seek-rsi
excerpt: A $25 camera took 2.4 seconds to answer every time the agent looked. Keeping the stream open brought that down to 1.63 milliseconds.
hero: /assets/peek-and-seek.png
---

I asked an agent to find my 3D printer. Every look cost **2.4 seconds**. It could edit its own camera tools, so I asked it to fix that. The googly eyes on our $25 Tapos, Peek and Seek, made watching them search my office feel a little less creepy.

## Make the second look cheap

Python reopened RTSP for each snapshot. The Rust rewrite kept the stream open. On the same camera, median snapshot latency fell from **2,385 ms to 1.63 ms** across 100 warm calls per version. The camera still delivered 15 fps. [Per-commit measurements](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/commit-history)

![A persistent RTSP reader feeds a shared latest-frame buffer. Each MCP request reads the preview already there.](/assets/rust-pipeline.png)

## Let the game drive the next edit

![Peek withholds the object's coordinates. Seek searches, checks the image and timings, patches its tools, and tries a fresh target. Seven games and 216 motion trials supplied feedback.](/assets/improvement-loop.png)

## Reuse work inside the tracker

![Nine-point tracking on the same frame pair fell from 350 to 74 milliseconds when all nine points shared the two frames’ cached features.](/assets/tracking-reuse.png)

One last change showed up in the live tool call. Faster trace scanning and SIMD base64 encoding moved warm preview from **1.70 to 1.54 ms** median over 600 calls per release. Agent time is excluded. [Optimization measurements](https://github.com/Belval/onvif-mcp/tree/ddc847f/benchmarks/mcp-optimization) · [I Spy trial records](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/i-spy)
