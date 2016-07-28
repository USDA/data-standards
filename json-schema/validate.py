'''
python3 validate.py
'''

import json
import jsonschema

from jsonschema import validate

data = ""

with open("example.json") as data_file:
	data = json.load(data_file)

with open("AcreageSubmission.json") as schema_file:
	agJsonSchema = json.load(schema_file)
	try:
   		#TODO: lazy validation
		validate(data, agJsonSchema)
		print ("valid json")
	except jsonschema.ValidationError as e:
		print (e.message)
