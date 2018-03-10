#import our inverted_indexer file
import inverted_indexer as Indexer
import pprint

if __name__ == "__main__":

	# Create Inverted Index
	inverted_index = {}

	docs_base_dir = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/"
	#num_sub_dirs = 75
	num_sub_dirs = 1

	path_url_map_filepath = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/bookkeeping.json"

	inverted_index = Indexer.inverse_index(inverted_index, docs_base_dir, num_sub_dirs, path_url_map_filepath)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(inverted_index)
