from rdflib import Graph
#import sys
#from pkgutil import simplegeneric
import json
import pymongo
from pymongo import MongoClient
import sys

g = Graph()    
client = MongoClient() # establish mongodb connection
db = client.test
g.parse("gt2rdf.rdf", format= "nt")  # parse the graph as given format; nt in this case

try:


	id_count = 1 # initialize count

	for s,t,p in g:
	
		result = db.pya.find_one({'subject': s}) # check if record with the same subject exists
	#print result
		if result:
			db.pya.update({'subject': s}, { '$push': {'relation':{'predicate': t, 'object': p}}}) # If exists, then add predicate and object in a relation array
		else:
				db.pya.insert_one({'_id': id_count, 'subject': s, 'relation': [{'predicate': t, 'object': p}]}) # else, create a new document
				id_count = id_count+1

except:
	print "exception rasied"