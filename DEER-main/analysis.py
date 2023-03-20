import json
dataset = json.load(open('extract_wiki/dataset_0.50_undir2dir_0.74.json'))
for i, datapoint in enumerate(dataset):
	# dict_keys(['pair', 'sim', 'entity', 'target', 'source', 'triple'])
	print(datapoint['pairs']])
	if i > 5: break