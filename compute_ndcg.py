import math


def compute_ndcg_score(google_results_map, search_engine_results_map, num_results_cap):

	bucket_1_cap = (num_results_cap/4) - 1
	bucket_2_cap = (num_results_cap/2) - 1
	bucket_3_cap = (num_results_cap) - 1

	ndgc_all_queries = []

	overall_ndgc = 0
	count = 0

	for query in search_engine_results_map:
		
		rel = []
		dcg = 0;
		dcg_i = 0;

		if query in google_results_map:
			count = count + 1
			list_results = google_results_map[query]

			# Compoute Relevance to Google's results
			for result_url in search_engine_results_map[query]:
				
				if result_url in list_results:

					position_google = list_results.index(result_url)

					if(position_google <= bucket_1_cap):
						rel.append(3)
					elif(position_google <= bucket_2_cap):
						rel.append(2)
					elif(position_google <= bucket_3_cap):
						rel.append(1)

				else:
					rel.append(0) 

			# Compute DCG
			for j in range(0,5):
				dcg = dcg + (rel[j] / math.log(j+2,2))

			# Compute DCG_Ideal
			rel.sort(reverse=True)

			for j in range(0,5):
				dcg_i = dcg_i + (rel[j] / math.log(j+2,2))

			# Compute NDCG
			if(dcg_i == 0):
				ndcg = 0
			else:
				ndcg = (dcg / dcg_i)

			ndgc_all_queries.append(ndcg)
			
			overall_ndgc = overall_ndgc + ndcg
			
			print("NDCG for query- " + query + ": " + str(ndcg))

	print("Number of total matches:" +  str(count))

	overall_ndgc = overall_ndgc / len(search_engine_results_map)

	return [overall_ndgc, ndgc_all_queries]