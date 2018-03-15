import pprint
import json
import pickle
from bisect import bisect_left
from document_tokenizer import stem_tokens, tokenize 

if __name__ == "__main__":
	docs_base_dir = "/Users/rahil/Desktop/221/Project3/WEBPAGES_CLEAN/"
	path_url_map_filepath = "/Users/rahil/Desktop/221/Project3/WEBPAGES_CLEAN/bookkeeping.json"
	index = pickle.load(open('index.p', 'rb'))

	while True:
		query = input("Enter the query: ")
		if query == 'exit':
			break
		query_search_engine(query, path_url_map_filepath, index, docs_base_dir, True)
	# print(query)

def query_search_engine_list(queryList):

	docs_base_dir = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/"
	path_url_map_filepath = "/Users/avinashaita/Desktop/info-retrieval/Project3/WEBPAGES_CLEAN/bookkeeping.json"
	index = pickle.load(open('index.p', 'rb'))

	search_engine_results_map = {}

	i = 0
	for query in queryList:
		query_results = query_search_engine(query, path_url_map_filepath, index, docs_base_dir, False)
		print( str(i) + "/" + str(len(queryList)) + " querying done" )
		search_engine_results_map[query] = query_results
		i = i+1

	return search_engine_results_map

def query_search_engine(query, path_url_map_filepath, index, docs_base_dir, print_flag):

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
	pos_results = []
	path_results = []

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

	prev_query_pos = []
	curr_query_pos = []

	prev_query_path = []
	curr_query_path = []


	prev_query_results = []
	curr_query_results = []

	curr_results_tfidf = []

	count = 0
	for term in sorted_terms:
		doc_list = index[term]
		
		curr_results_tfidf = []
		curr_query_results = []
		curr_query_pos = []
		curr_query_path = []


		for doc in doc_list:
			doc_frequency = index['document_details_counts'][doc['loc']]
			tf = len(doc['pos'])/doc_frequency
			from math import log
			idf = log(N/len(index[term]), 10)
			tf_idf = tf * idf
			
			curr_results_tfidf.reverse()
			curr_query_results.reverse()
			curr_query_pos.reverse()
			curr_query_path.reverse()

			index_res = bisect_left(curr_results_tfidf, tf_idf)
			curr_results_tfidf.insert(index_res, tf_idf)
			curr_query_results.insert(index_res, path_url_map[doc['loc']])

			curr_query_pos.insert(index_res, doc['pos'])
			curr_query_path.insert(index_res, doc['loc'])

			# print("Inserting thisss:  ", doc['pos'])

			curr_results_tfidf.reverse()
			curr_query_results.reverse()
			curr_query_pos.reverse()
			curr_query_path.reverse()

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
			pos_final = []
			path_final = []
			k = 0
			while k < len(indices):
				results_final.append(prev_query_results[indices[k]])
				pos_final.append(prev_query_pos[indices[k]])
				path_final.append(prev_query_path[indices[k]])

				k = k+1

			if len(results_final) < 5:
				to_be_inserted = 5 - len(results_final)
				remaining = 0
				pos = 0
				while remaining < to_be_inserted:
					results_final.append(prev_query_results[pos])
					pos_final.append(prev_query_pos[pos])
					path_final.append(prev_query_path[pos])
					pos=pos+1
					remaining=remaining+1
				query_results = results_final
				pos_results = pos_final
				path_results = path_final
				break;
			
			curr_query_results = results_final
			curr_query_pos = pos_final
			curr_query_path = path_final


		# prev_results_tfidf = curr_results_tfidf
		prev_query_results = curr_query_results
		query_results = prev_query_results

		prev_query_pos = curr_query_pos
		pos_results = prev_query_pos

		prev_query_path = curr_query_path
		path_results = prev_query_path

		# print("After count: ", count)
		# print("Length of qResults: ", len(prev_query_results));
		# print("Length of query_results: ", len(query_results));


	if len(query_results) > 5:
		query_results = query_results[:5]

	return query_results

	if print_flag == True:

		print('Query results are as follows: \n')
		result = 0
		print_pos = 0
		for url in query_results:
			print('Result '+ str(result))
			print(url)
			# print("Path: ", path_results[print_pos])
			# Printing the line
			# print(pos_results[print_pos])


			file_p = open(docs_base_dir + path_results[print_pos], 'r')
			text_data = file_p.read()
			tokenized_data = tokenize(text_data)

			line_num = 0
			restrictTokens = 0;
			for token_num in pos_results[print_pos]:
				print("Text Snippet: ", line_num)
				wordCount = 0
				resultStr = ""
				while wordCount < 15 and (token_num + wordCount) < len(tokenized_data):
					resultStr = resultStr + tokenized_data[token_num + wordCount] + " "
					wordCount += 1
				print("...", resultStr, "...")
				line_num += 1
				print("\n")
				restrictTokens += 1
				if restrictTokens >= 3:
					break

			print_pos += 1
			result += 1 


