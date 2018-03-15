#import our inverted_indexer file
import inverted_indexer as Indexer
import pprint
import json
import pickle
from bisect import bisect_left

if __name__ == "__main__":

	# Create Inverted Index
	inverted_index = {}

	docs_base_dir = "/Users/rahil/Desktop/221/Project3/WEBPAGES_CLEAN/"
	path_url_map_filepath = "/Users/rahil/Desktop/221/Project3/WEBPAGES_CLEAN/bookkeeping.json"
	
	num_sub_dirs = 75
	# num_sub_dirs = 10
	inverted_index = Indexer.inverse_index(inverted_index, docs_base_dir, num_sub_dirs, path_url_map_filepath)
	
	pickle.dump(inverted_index, open('index.p', 'wb'))
