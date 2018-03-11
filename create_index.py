#import our inverted_indexer file
import inverted_indexer as Indexer
import pprint

if __name__ == "__main__":

	# Create Inverted Index
	inverted_index = {}

	docs_base_dir = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/"
	path_url_map_filepath = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/bookkeeping.json"
	
	num_sub_dirs = 75
	# num_sub_dirs = 1
	inverted_index = Indexer.inverse_index(inverted_index, docs_base_dir, num_sub_dirs, path_url_map_filepath)


	logFile = open("/Users/avinashaita/Desktop/info-retrieval/Project3/inverted_index", 'w')
	pp = pprint.PrettyPrinter(indent=4, stream=logFile)
	pp.pprint(inverted_index)
