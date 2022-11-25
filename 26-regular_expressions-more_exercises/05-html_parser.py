import re
text = input()
pattern_title = r'<title>(.+)</title>'
pattern_content = r'<body>(.+)</body>'
matches_title = re.findall(pattern_title, text)
matches_content = re.findall(pattern_content, text)
tags = r'(<[^>]*>)'
tabs = r'(\\n)|(\\t)'
title = ''
content = ''
if matches_title and matches_content:
    title = matches_title[0]
    title = re.sub(tags, "", title)
    title = re.sub(tabs, "", title)
    while "  " in title:
        title = title.replace("  ", " ")

    content = matches_content[0]
    content = re.sub(tags, "", content)
    content = re.sub(tabs, "", content)
    while "  " in content:
        content = content.replace("  ", " ")

    print(f'Title: {title}')
    print(f'Content: {content}')

