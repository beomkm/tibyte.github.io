import os
import errno

print('Do you want to create pages for tag? (y/n)')
is_tag = input()
if is_tag == 'y':
    print('tag : ', end='', flush=True)
    tag = input()
    tag_prefix = f'tag/{tag}/'
else:
    tag_prefix = ''
print('pages up to : ', end='', flush=True)
try:
    pages = int(input())
    if pages > 100:
        raise
except:
    print('Input is wrong or too big.')
    exit()


content_main = '''---
layout: default
permalink: {0}
---

{{% assign cpage = 1 %}}
{1}
{{% include postlist.html %}}
'''

content = '''---
layout: default
permalink: {0}page/{1} 
---

{{% assign cpage = {1} %}}
{2}
{{% include postlist.html %}}
'''

if is_tag == 'y':

    filename = f'_pages/tags/{tag}/page1.html'
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    filename = f'_pages/tags/{tag}.html'
    with open(filename, 'w') as f:
        f.write(content_main.format(tag_prefix, f'{{% assign filter = "{tag}" %}}'))

for i in range(1, pages+1):
    if is_tag == 'y':
        with open(f'_pages/tags/{tag}/page{i}.html', 'w') as f:
            f.write(content.format(tag_prefix, i, f'{{% assign filter = "{tag}" %}}'))
    else :
        with open(f'_pages/page{i}.html', 'w') as f:
            f.write(content.format(tag_prefix, i, ''))
    print(f'page{i} complete')

