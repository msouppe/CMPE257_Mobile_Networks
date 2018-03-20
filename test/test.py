import yaml

f = open('simple.yaml', 'r')

for data in yaml.load_all(f):
    # data["randomSeed"]
    # data["numMotes"]
    # data["x_placement"]
    # data["y_placement"]
    # data["terrain"]
#	print (str(data["randomSeed"]) + " " + str(data["numMotes"]))
	print (data)
