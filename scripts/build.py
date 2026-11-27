"""Build Markdown posts into a small static blog. Output: _site (never source)."""
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path
import json
import re
import shutil
import xml.etree.ElementTree as ET
import markdown
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
SITE=json.loads((ROOT/'site.json').read_text())

def page(title,content,path='/',description=None,image=None):
    title=title+' · '+SITE['title'] if title else SITE['title']
    description=description or SITE['description']
    canonical=SITE['url']+path
    image_tag=f'<meta property="og:image" content="{escape(SITE["url"]+image)}">' if image else ''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description)}">
<link rel="canonical" href="{escape(canonical)}"><meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}"><meta property="og:type" content="article"><meta property="og:url" content="{escape(canonical)}">{image_tag}
<meta name="theme-color" content="#F5F3EC"><link rel="icon" href="/assets/mark.svg" type="image/svg+xml">
<link rel="alternate" type="application/atom+xml" title="{escape(SITE['title'])}" href="/feed.xml">
<link rel="stylesheet" href="/assets/brand-theme.css"><link rel="stylesheet" href="/assets/style.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="navigation wrap"><a class="wordmark" href="/" aria-label="Edouard Belval, home">edouard belval<span>.</span></a>
<nav aria-label="Main navigation"><a href="/#writing">Writing</a><a href="/about/">About</a><a href="{SITE['github']}">GitHub <span aria-hidden="true">↗</span></a></nav></header>
<main id="main">{content}</main>
<footer class="wrap"><a href="/" class="footer-name">Tales from the Latent Space</a><p>Built, measured, written down.</p><a href="/feed.xml">RSS ↗</a></footer>
</body></html>'''

def write(path,text):
    target=OUT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text)

def read_posts():
    posts=[]
    for file in sorted((ROOT/'posts').glob('*.md')):
        chunks=file.read_text().split('---',2)
        if len(chunks)!=3 or chunks[0].strip():raise ValueError('Post needs YAML front matter: '+str(file))
        meta=yaml.safe_load(chunks[1]);body=chunks[2].strip()
        for key in ('title','date','slug','excerpt','hero'):
            if not meta.get(key):raise ValueError(f'Missing {key} in {file}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',meta['slug']):raise ValueError('Invalid slug')
        meta['date']=date.fromisoformat(str(meta['date']))
        meta['body']=markdown.markdown(body,extensions=['tables','fenced_code','attr_list','md_in_html'])
        meta['body']=meta['body'].replace('<p><em>', '<p class="figure-note"><em>')
        meta['url']='/writing/'+meta['slug']+'/'
        meta['read_minutes']=max(1,round(len(body.split())/220))
        posts.append(meta)
    if len({p['slug'] for p in posts})!=len(posts):raise ValueError('Duplicate slug')
    return sorted(posts,key=lambda p:p['date'],reverse=True)

def build():
    posts=read_posts()
    if not posts:raise ValueError('At least one post is required')
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/'assets',OUT/'assets')
    (OUT/'.nojekyll').write_text('')
    latest=posts[0]
    hero=f'''<section class="intro wrap"><p class="eyebrow">FIELD NOTES / BY EDOUARD BELVAL</p>
<h1>Tales from the<br><em>latent space.</em></h1><div class="intro-bottom"><p>{escape(SITE['description'])}</p><a class="text-link" href="#writing">Read the latest <span aria-hidden="true">↓</span></a></div></section>
<section class="writing wrap" id="writing"><div class="chapter"><span>01 / THE NOTEBOOK</span><span>Experiments, not predictions.</span></div>
<a class="feature-art" href="{latest['url']}"><img src="{latest['hero']}" alt="Peek and Seek, two Tapo cameras wearing googly eyes" width="1672" height="941" fetchpriority="high"></a>
<div class="feature-copy"><div><p class="eyebrow">AGENTS × HARDWARE / {latest['date'].strftime('%d %B %Y').upper()}</p><h2><a href="{latest['url']}">{escape(latest['title'])}</a></h2></div>
<div><p>{escape(latest['excerpt'])}</p><a class="text-link" href="{latest['url']}">Read the experiment <span aria-hidden="true">↗</span></a></div></div></section>'''
    if len(posts)>1:
        hero+='<section class="archive wrap"><h2>More field notes</h2>'+''.join(f'<p><a href="{p["url"]}">{escape(p["title"])}</a></p>' for p in posts[1:])+'</section>'
    write('index.html',page('',hero,image=latest['hero']))
    for post in posts:
        caption = post.get('hero_caption')
        caption_html = f'<figcaption>{escape(caption)}</figcaption>' if caption else ''
        header=f'''<article><header class="post-header wrap"><a class="back" href="/">← All field notes</a><p class="eyebrow">AGENTS × HARDWARE / {post['date'].strftime('%d %B %Y').upper()} / {post['read_minutes']} MIN READ</p>
<h1>{escape(post['title'])}</h1><p class="standfirst">{escape(post['excerpt'])}</p></header>
<figure class="post-hero wrap"><img src="{post['hero']}" alt="Peek and Seek, two real Tapo cameras with googly eyes, on an oak desk" width="1672" height="941" fetchpriority="high">{caption_html}</figure>
<div class="prose">{post['body']}</div><div class="post-end wrap"><span class="eyebrow">END OF FIELD NOTE</span><a class="text-link" href="https://github.com/Belval/onvif-mcp">Explore the source ↗</a></div></article>'''
        write(post['url'].strip('/')+'/index.html',page(post['title'],header,post['url'],post['excerpt'],post['hero']))
    about='''<section class="about wrap"><p class="eyebrow">ABOUT / EDOUARD BELVAL</p><h1>Make it work.<br><em>Then measure it.</em></h1><div class="about-copy"><p>I build software, machine learning systems, and the occasional piece of hardware.</p><p>This is my notebook for experiments at their intersection: what I tried, what the measurements said, and what I changed next.</p><a class="text-link" href="https://github.com/Belval">Find my work on GitHub ↗</a></div></section>'''
    write('about/index.html',page('About',about,'/about/'))
    write('404.html',page('Page not found','<section class="about wrap"><p class="eyebrow">404 / OFF THE MAP</p><h1>A fresh notebook.</h1><p>This page is no longer here.</p><a class="text-link" href="/">Return to the field notes ↗</a></section>','/404.html'))
    ns='http://www.w3.org/2005/Atom';ET.register_namespace('',ns)
    feed=ET.Element('{'+ns+'}feed')
    for key,value in [('title',SITE['title']),('id',SITE['url']+'/'),('updated',max(p['date'] for p in posts).isoformat()+'T00:00:00Z')]:ET.SubElement(feed,'{'+ns+'}'+key).text=value
    ET.SubElement(feed,'{'+ns+'}link',href=SITE['url']+'/feed.xml',rel='self')
    ET.SubElement(feed,'{'+ns+'}link',href=SITE['url']+'/')
    author=ET.SubElement(feed,'{'+ns+'}author');ET.SubElement(author,'{'+ns+'}name').text=SITE['author']
    for post in posts:
        entry=ET.SubElement(feed,'{'+ns+'}entry')
        for key,value in [('title',post['title']),('id',SITE['url']+post['url']),('updated',post['date'].isoformat()+'T00:00:00Z'),('summary',post['excerpt'])]:ET.SubElement(entry,'{'+ns+'}'+key).text=value
        ET.SubElement(entry,'{'+ns+'}link',href=SITE['url']+post['url'])
    (OUT/'feed.xml').write_bytes(ET.tostring(feed,encoding='utf-8',xml_declaration=True))
    print(f'Built {len(posts)} post(s) into {OUT}')

if __name__=='__main__':build()
