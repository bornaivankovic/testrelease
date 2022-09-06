import feedparser

f=feedparser.parse('https://github.com/bornaivankovic/testrelease/releases.atom')
print(f)