"""Check output links, local assets, feed, and retirement of the old articles."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]/'_site'
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.images=[];self.title=False;self.in_title=False
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        for key in ('href','src'):
            if key in values:self.links.append(values[key])
        if tag=='img':self.images.append(values)
        if tag=='title':self.in_title=True
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
    def handle_data(self,value):
        if self.in_title and value.strip():self.title=True

count=0
for file in ROOT.rglob('*.html'):
    parser=Links();parser.feed(file.read_text());assert parser.title,file
    for image in parser.images:assert image.get('alt'),f'Missing image alt: {file}'
    for url in parser.links:
        parsed=urlparse(url)
        if parsed.scheme or parsed.netloc or not parsed.path:continue
        target=(ROOT/unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else file.parent/unquote(parsed.path)
        assert target.exists(),f'Broken local link {url} in {file}'
    count+=1
ET.parse(ROOT/'feed.xml')
for old in ('google-nest-mini-teardown','diy-power-bank','wireguard-is-awesome'):
    assert not any(old in str(p) for p in ROOT.rglob('*')),old
print(f'PASS: {count} HTML pages, links/images/feed; retired posts absent')
