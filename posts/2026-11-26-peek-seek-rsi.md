---
title: I asked an agent to find my printer. It rewrote its camera driver.
date: 2026-11-26
slug: peek-seek-rsi
excerpt: A $25 camera took 2.4 seconds to answer every time the agent looked. Keeping the stream open brought that down to 1.63 milliseconds.
hero: /assets/peek-and-seek.png
---

I asked a coding agent to find the 3D printer in my office. Each time it wanted another look, its camera tool spent **2.4 seconds** getting a picture. A search takes several looks. The agent had access to the source for its own tools, so I asked it to make looking cheap.

These are Peek and Seek, two roughly $25 Tapo cameras. I put googly eyes on them. It’s surprisingly hard to feel watched by something that looks this unsure where you are.

## Why a second look cost as much as the first

The agent called a snapshot tool over MCP. Underneath, Python used ONVIF to control the camera and opened an RTSP video connection to get a picture. On the next call it opened the stream all over again. We were paying startup latency every time the agent asked what had changed.

The agent rewrote the MCP server in Rust. While the preview is active, a background reader keeps the stream open and replaces the latest frame as new ones arrive. A snapshot request picks up the current frame and returns it. We rebuilt both versions and timed 100 warm requests per version on the same C210. **Median request time fell from 2,385 ms to 1.63 ms.** Starting the Rust process and getting its first image still took 160 ms. The camera produces 15 frames per second. What became fast was reading the latest one. [Per-commit timings and protocol](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/commit-history)

![The Rust preview path keeps RTSP ingestion running while MCP requests read the latest frame.](/assets/rust-pipeline.png)

## Give the agent another round

We played *I spy*. Peek picked an object and withheld its coordinates. Seek had to find it. That gave the agent a reason to care about the next bottleneck, and a way to check whether a faster tool still worked. Across seven independently judged games and 216 motion trials, we kept the timings alongside the outcomes. [Game records and motion trials](https://github.com/Belval/onvif-mcp/tree/main/benchmarks/i-spy)

Two changes from the next optimization pass held up under replay:

| What the agent found | What changed | Before → after |
| --- | --- | --- |
| Tracking nine points on one pair of images repeated feature extraction. | Each frame now caches its features. We replayed identical images and checked the tracked coordinates. | **350 → 74 ms** for nine tracks |
| Even a warm preview spent time scanning trace messages and encoding the image for transport. | The server now uses vectorized newline scanning and SIMD base64 encoding. We ran 600 live requests per release with tracing enabled. | **1.70 → 1.54 ms** median, **2.07 → 1.86 ms** p95 |

The tracking result measures CPU work on fixed inputs. The preview result measures a complete live MCP call from the client. Both exclude agent thinking time. [Optimization benchmarks and raw traces](https://github.com/Belval/onvif-mcp/tree/ddc847f/benchmarks/mcp-optimization)

That was the recursive part of *I spy*. The same agent that had to find the printer could change what happened the next time it called its camera. Its biggest win was figuring out that the second look should cost less than the first.
