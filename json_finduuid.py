import json
my_dict={"hari":{"aliases":{},"mappings":{},"settings":{"index":{"index":"hari","creation_date":"1485316834483","number_of_shards":"5","number_of_replicas":"1","version":{"created":"1070299"},"uuid":"JiES6mbfQgWTYwtZjKBfBg"}},"warmers":{}}}
#print my_dict
print json.dumps(my_dict,indent=5)
