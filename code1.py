from rdflib import Graph
import sys
from pkgutil import simplegeneric
import json

g = Graph()
g.parse("C:\Users\Yashodhanj\Desktop\ed.nt", format= "nt")


	#print obj
	#print json.dumps(obj, sort_keys=True, indent=4)
	#jsonData = json.dumps({'s' : s, 'o' : t, 'p' : p}, sort_keys=True, indent=4, separators=(',', ': '))
	
@simplegeneric
def get_items(obj):
    while False: 
        yield None

@get_items.register(dict)
def _(obj):
    return obj.iteritems() # json object

@get_items.register(list)
def _(obj):
    return enumerate(obj) # json array

def strip_whitespace(json_data):
    for key, value in get_items(json_data):
        if hasattr(value, 'strip'): # json string
            json_data[key] = value.strip()
        else:
            strip_whitespace(value) # recursive call


for s,t,p in g:
	
	data = {'subject' : s,
			 'predicate' : t,
			 'object' : p}
	strip_whitespace(data)
	#obj = json.dumps(data, ensure_ascii=False, indent=4)
		#json.dump(json.dumps(data, ensure_ascii=False, indent=4), f)
	with open('testdata.json', 'a') as f:
		json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))
		
	
		

