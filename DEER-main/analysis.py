import json
dataset = json.load(open('extract_wiki/dataset_0.50_undir2dir_0.74.json'))
for datapoint in dataset:
	print(datapoint.keys())