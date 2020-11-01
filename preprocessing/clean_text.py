import re

pattern = re.compile("<(/)?a[^>]*>")
punctuation = re.compile(",")
f=open('./Text_corpus/wiki_00', 'r', encoding='utf8')
o=open('./temp','w', encoding='utf8')
content = f.read()
content=str(content)
content_new = re.sub(pattern, " ", content)
content_new = re.sub(punctuation, " ", content_new)
o.write(content_new)
f.close()
o.close()