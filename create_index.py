#import our inverted_indexer file
import inverted_indexer as Indexer
import pprint
import json
import pickle
from bisect import bisect_left

if __name__ == "__main__":

	# Create Inverted Index
	inverted_index = {}

	docs_base_dir = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/"
	path_url_map_filepath = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/bookkeeping.json"
	
	num_sub_dirs = 75
	# num_sub_dirs = 10
	inverted_index = Indexer.inverse_index(inverted_index, docs_base_dir, num_sub_dirs, path_url_map_filepath)



	pickle.dump(inverted_index, open('index.p', 'wb'))

	# logFile = open("/Users/harsha/IR-Project3/inverted_index", 'w')
	# pp = pprint.PrettyPrinter(indent=4, stream=logFile)
	# with open("/Users/harsha/IR-Project3/inverted_index", 'w') as fp:
	# 	json.dump(inverted_index, fp)

	# index = pickle.load(open('index.p', 'rb'))

	# query = input("Enter the query: ")
	# print(query)

	# json_data = open(path_url_map_filepath).read()
	# path_url_map = json.loads(json_data)

	# query_words = query.split()

	# N = 37500

	# query_results = []
	# results_tfidf = []
	# from math import inf

	# if len(query_words) == 1:
	# 	q = query_words[0]
	# 	doc_list = index[q]
	# 	for doc in doc_list:
	# 		doc_frequency = index['document_details_counts'][doc['loc']]
	# 		tf = len(doc['pos'])/doc_frequency
	# 		from math import log
	# 		idf = log(N/len(index[q]), 10)
	# 		tf_idf = tf * idf
	# 		results_tfidf.reverse()
	# 		query_results.reverse()
	# 		index_res = bisect_left(results_tfidf, tf_idf)
	# 		results_tfidf.insert(index_res, tf_idf)
	# 		query_results.insert(index_res, path_url_map[doc['loc']])
	# 		results_tfidf.reverse()
	# 		query_results.reverse()

	# 		if len(query_results) > 5:
	# 			query_results = query_results[:-1]
	# 			results_tfidf = results_tfidf[:-1]
	# print('Query results are as follows: \n')
	# result = 0
	# for url in query_results:
	# 	print('Result '+ str(result))
	# 	print(url)
	# 	result += 1 





	# pp.pprint(inverted_index)
