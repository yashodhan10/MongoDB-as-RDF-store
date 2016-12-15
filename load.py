from rdflib import Graph
#import sys
#from pkgutil import simplegeneric
import json
import pymongo
from pymongo import MongoClient
import sys

g = Graph()
client = MongoClient()
db = client.test
g.parse("C:\Users\Yashodhanj\Desktop\RDF\gt2rdf.rdf", format= "nt")

try:


	id_count = 1
#json_data = []
	for s,t,p in g:
	
		result = db.pya.find_one({'subject': s})
	#print result
		if result:
			db.pya.update({'subject': s}, { '$push': {'relation':{'predicate': t, 'object': p}}})
		else:
				db.pya.insert_one({'_id': id_count, 'subject': s, 'relation': [{'predicate': t, 'object': p}]})
				id_count = id_count+1

except:
	print "exception rasied"