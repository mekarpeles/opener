#-*- coding: utf-8 -*-

import os
from math import ceil
import json
import requests

from api.search import match, index

TAG_API = 'http://api.stackoverflow.com/1.1/tags'
PATH = os.path.join('/'.join(os.path.abspath(__file__).split('/')[:-2]),
                    'indices/tags/')

def sotags(startpage=1, pagesize=100, limit=None, outfile=None):
    """Returns a list of all stack overflow tags"""
    def parsetags(page):
        r = requests.get('%s?pagesize=%s&page=%s' %
                         (TAG_API, pagesize, page))
        page = r.json()
        return page

    data = parsetags(startpage)
    pages = limit if limit else int(ceil(float(data['total']) / pagesize))
    tags = dict([(tag['name'], tag['count']) for tag in data['tags']])

    # we've already parsed page 1, start at 2
    for page in xrange(startpage+1, pages+1):
        for tag in parsetags(page)['tags']:
            tags[tag['name']] = tag['count']

    if outfile and type(outfile) is str:
        with open(outfile, 'wb') as fout:
            json.dump(tags, fout)
    return tags

def soindex(dbname=PATH):
    tags = json.load(open('data/tags.json'))
    index(tags.keys(), dbname=dbname)
    
def er(query, dbname=PATH):                       
    return match(query, dbname=dbname)
