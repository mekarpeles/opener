#!/usr/bin/env python

"""
    search
    ~~~~~~

    Search interface for indexing and querying/matching
"""

import os, sys

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

def index(keys, dbname=os.getcwd()+"/idx"):
    """Simple indexing allows you to create an index from a list of
    terms/keys and search/match over them

    usage:
    >>> index(['foo', 'bar', 'baz'])
    """
    schema = Schema(attr=TEXT(stored=True), 
                    index=TEXT(stored=True))
    ix = create_in(dbname, schema)
    writer = ix.writer()
    for k in keys:
        writer.add_document(attr=unicode(k),
                            index=unicode(k))
    writer.commit()
    
def multidex(keys, values, pkey=None, dbname=os.getcwd()+"/idx"):
    """Index values under 1 or more keys

    usage:
    >>> multidex(['login', 'name'], [{'login': 'foo', 'name': 'bar'}, ...], pkey="login")
    """
    schema = Schema(attr=TEXT(stored=True), 
                    index=TEXT(stored=True))
    ix = create_in(dbname, schema)
    writer = ix.writer()
    pkey = pkey or keys[0]
    for i, v in enumerate(values):
        for k in keys:
            if k in v and v[k]:                
                writer.add_document(attr=unicode(v[k].lower()),
                                    index=unicode(v[pkey]))

    writer.commit()

def match(query, dbname=os.getcwd()+"/idx"):
    index = open_dir(dbname)
    searcher = index.searcher()
    query = unicode(query.lower())
    q = QueryParser("attr", index.schema).parse(query)
    results = searcher.search(q)
    return results
