import re

pattern = re.compile("<(/)?a[^>]*>")
f=open('./Text_corpus/wiki_00', 'r' )
o=open('./temp','w')
content = f.read()
content=str(content)
content_new = re.sub(pattern,"", content)
o.write(content_new)
f.close()
o.close()