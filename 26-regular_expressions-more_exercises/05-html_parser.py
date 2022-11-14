import re
text = input()
pattern_title = r'<title>([a-zA-Z\s]*)</title>[\w\W]*<body>([\w\W]*)</body>'
matches = re.findall(pattern_title, text)
title = matches[0][0]
content = matches[0][1]

tags = r'(<[^>]*>)'
tabs = r'(\\n)|(\\t)'

title = re.sub(tags, "", title)
title = re.sub(tabs, "", title)
content = re.sub(tags, "", content)
content = re.sub(tabs, "", content)

print(f'Title: {title}')
print(f'Content: {content}')