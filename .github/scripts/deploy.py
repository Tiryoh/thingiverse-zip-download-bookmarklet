#!/usr/bin/env python3

import requests
import re

def minify(debug=False):
    url = 'https://www.toptal.com/developers/javascript-minifier/raw'
    data = {'input': open('thingiverse-zip-download.js', 'rb').read()}
    response = requests.post(url, data=data)
    if debug:
        print('javascript:{}'.format(response.text))
    return response.text

def main():
    with open('README.md','r') as f:
        f.readline() # skip the first title
        body = f.read()

    body = re.sub(BEFORE_CONTENT, CONTENT, body, flags=re.DOTALL)
    body = re.sub(BEFORE_BOOKMARKLET, BOOKMARKLET, body, flags=re.DOTALL)

    with open('index.md','w') as f:
        f.write(body)

BEFORE_CONTENT='Add the bookmarklet from the following URL.'
BEFORE_BOOKMARKLET='https://tiryoh.github.io/thingiverse-zip-download-bookmarklet'
CONTENT='Add the following link as a bookmarklet to bookmark tab.'
BOOKMARKLET="<a href='javascript:{}'>ThingiverseZipDownload</a>".format(minify())

main()