import pprint
import json
import pickle
from bisect import bisect_left


docs_base_dir = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/"
path_url_map_filepath = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/bookkeeping.json"


index = pickle.load(open('index.p', 'rb'))


while True:
	query = input("Enter the query: ")
	if query == 'exit':
		break
	# print(query)

	json_data = open(path_url_map_filepath).read()
	path_url_map = json.loads(json_data)
	query_words = query.split()
	temp = []

	for word in query_words:
		if word.isupper():
			temp.append(word)
		else:
			temp.append(word.lower())

	query_words = temp

	N = 37500

	query_results = []

	from math import inf

	# loop through each term
	# sort them based on idf scores = sorted_terms
	sorted_terms = []
	terms_idf = []
	for term in query_words:
		# print("Term is: ", term)
		from math import log
		if term in index:
			idf = log(N/len(index[term]), 10)
			sorted_terms.reverse()
			terms_idf.reverse()
			index_at = bisect_left(terms_idf, idf)
			terms_idf.insert(index_at, idf)
			sorted_terms.insert(index_at, term)
			sorted_terms.reverse()
			terms_idf.reverse()	
		
	# loop through sorted_terms
		# keep intersecting until you hit the desired number of results

	prev_query_results = []
	curr_query_results = []

	curr_results_tfidf = []

	count = 0
	terminate = False
	for term in sorted_terms:
		doc_list = index[term]
		
		curr_results_tfidf = []
		curr_query_results = []

		for doc in doc_list:
			doc_frequency = index['document_details_counts'][doc['loc']]
			tf = len(doc['pos'])/doc_frequency
			from math import log
			idf = log(N/len(index[term]), 10)
			tf_idf = tf * idf
			
			curr_results_tfidf.reverse()
			curr_query_results.reverse()
			
			index_res = bisect_left(curr_results_tfidf, tf_idf)
			curr_results_tfidf.insert(index_res, tf_idf)
			curr_query_results.insert(index_res, path_url_map[doc['loc']])
			
			curr_results_tfidf.reverse()
			curr_query_results.reverse()

		count = count+1
		# if len(query_results1) >= 5:
			# prev_results_tfidf = curr_results_tfidf
			# prev_query_results = curr_query_results
		# print("Gets here at count: ", count)
		# print("Length of currResults: ", len(curr_query_results));

		if count > 1:
			indices = []
			i = 0
			while i < len(prev_query_results):
				j = 0
				while j < len(curr_results_tfidf):
					if prev_query_results[i] == curr_query_results[j]:
						indices.append(i)
					j = j+1
				i = i+1

			# print("Indices count: ", len(indices))
			
			results_final = []
			k = 0
			while k < len(indices):
				results_final.append(prev_query_results[indices[k]])
				k = k+1

			if len(results_final) < 5:
				to_be_inserted = 5 - len(results_final)
				remaining = 0
				pos = 0
				while remaining < to_be_inserted:
					results_final.append(prev_query_results[pos])
					pos=pos+1
					remaining=remaining+1
				query_results = results_final
				break;
			
			curr_query_results = results_final


		# prev_results_tfidf = curr_results_tfidf
		prev_query_results = curr_query_results
		query_results = prev_query_results
		# print("After count: ", count)
		# print("Length of qResults: ", len(prev_query_results));
		# print("Length of query_results: ", len(query_results));


	if len(query_results) > 5:
		query_results = query_results[:5]


	# handle null inputs


	print('Query results are as follows: ')
	result = 0
	for url in query_results:
		print('Result '+ str(result))
		print(url)
		result += 1 


# pp.pprint(inverted_index)
