import collections
from   decimal import Decimal
import json
from   six     import string_types

def strify_dict(d):
    strdict = {}
    for k,v in itemize(d):
        assert isinstance(k, string_types)
        if isinstance(v, (list, dict)):
            raise TypeError('Cannot convert list/dict to .properties value')
        elif isinstance(v, string_types):
            strdict[k] = v
        elif isinstance(v, Decimal):
            strdict[k] = str(v)
        else:
            strdict[k] = json.dumps(v)
    return strdict

def itemize(kvs, sort_keys=False):
    if isinstance(kvs, collections.Mapping):
        items = ((k, kvs[k]) for k in kvs)
    else:
        items = kvs
    if sort_keys:
        items = sorted(items)
    return items
