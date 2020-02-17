---
layout: post
title:  "Wireguard is awesome"
date:   2020-02-10 11:28:50 -0400
categories: networking
---

## Wireguard is awesome

With Wireguard being added to Linus' tree, it seems everything is coming together for its release as a viable VPN solution. As an avid self-hoster, I need such a solution to direct my local server traffic to an outside VPS that acts as a proxy. This ensures that my ever-changing public IP address does not cause unexpected outages. Moreover, it allows me to serve content on my HTTP (80) and HTTPS (443) ports, both of which are blocked by my ISP.

For the last two years, my solution was to pay for a digital ocean VPS at 5$/month. The monthly data cap of 1 TB is more than enough for my usage and in the rare events that I needed more, I would simply pay for a temporary increase.

I used autossh to create ssh tunnels between my home server and my proxy. The process included a bit of elbow grease but was still relatively straight forward, with two major drawbacks. First, OpenSSH for data transfer is CPU intensive and it limited the throughput of my home server. Second, it requires a DNS client on the server to check for periodic public IP address changes and update the DNS record. As I wrote, it did work for two years without a hitch, but it was far from perfect.

## Why Wireguard?

Some more knowledgeable readers will question my decision to use ssh tunnels at all. After all, there are plenty of VPN solutions that have been battle-tested and work in production at a much greater scale.

That's true, without a doubt. The thing is, I did try to get IPSec working through with Strongswan, but I always ended up giving up because the configuration is tedious (in my arguably limited exposure). As for OpenVPN, it is a whole other beast, probably as complex if not more than IPSec with a bigger overhead.

Wireguard is **new**, which means that it hasn't been audited as much as the other two solutions, if at all. Regardless, its killer feature is quite a simple one: it is incredibly easy to setup. I'm not talking "follow a tutorial to get it working in an hour" easy, it's more of 15 minutes during a class easy. 

The configuration files are a breeze to put together, and adding clients is only one `wg-quick` command away. See for yourself, here are my two `wg0.conf` files, totaling less than 27 lines together.

```
[Interface]
Address = 10.10.0.1/24
Address = fd86:ea04:1111::1/64
SaveConfig = true
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; ip6tables -A FORWARD -i wg0 -j ACCEPT; ip6tables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE; ip6tables -D FORWARD -i wg0 -j ACCEPT; ip6tables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = 51820
PrivateKey = [Server-Private-Key]

[Peer]
PublicKey = [Peer2-Public-Key]
PersistentKeepalive = 25
AllowedIPs = 10.10.0.2/32, fd86:ea04:1111::2/128

[Peer]
PublicKey = [Peer3-Public-Key]
AllowedIPs = 10.10.0.3/32, fd86:ea04:1111::3/128

[Peer]
PublicKey = [Peer4-Public-Key]
AllowedIPs = 10.10.0.4/32, fd86:ea04:1111::4/128
```

```
[Interface]
Address = 10.10.0.2/32
Address = fd86:ea04:1111::2/128
SaveConfig = true
PrivateKey = [Peer2-Private-Key]

[Peer]
PublicKey = [Peer2-Public-Key]
PersistentKeepalive = 25
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = [ServerIP]:51820
```

As a bonus, once that is set up, you can add Android/iOS clients with little effort and again, it. just. works.

## Conclusion

If it wasn't obvious from the heavy-handed praise above, I think Wireguard is the solution to a whole lot of VPN headaches. Any serious production usage should wait after more auditing has been done, but on paper, it is an excellent piece of software.

## Edit

I noticed that the VPN would stay connected, yet no packets could go through. I fixed the problem by adding `PersistentKeepalive = 25` to both configurations.