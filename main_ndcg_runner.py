import compute_ndcg as NDCG
import load_index as engine
import google_search as google_engine
import pickle

def query_search_engine(queries):
	
	search_engine_results_map = engine.query_search_engine_list(queries)

	pickle.dump(search_engine_results_map, open('engine_results', 'wb'))

def query_google(queries, num_results_cap):
	
	google_query_results_map = google_engine.google_search_list(queries, num_results_cap)

	pickle.dump(google_query_results_map, open('google_results_new', 'wb'))

if __name__ == "__main__":

	queries = []

	#queries.append("mondego")
	queries.append("machine learning")
	queries.append("software engineering")
	queries.append("security")
	queries.append("student affairs")
	queries.append("graduate courses")
	queries.append("Crista Lopes")
	queries.append("REST")
	queries.append("computer games")
	queries.append("information retrieval")


	num_results_cap = 50
	#query_search_engine(queries)
	query_google(queries, num_results_cap)


	google_results_path = "/Users/avinashaita/Desktop/info-retrieval/Project3/google_results_new"
	search_engine_results_path = "/Users/avinashaita/Desktop/info-retrieval/Project3/engine_results"

	google_results_map = pickle.load( open( google_results_path, "rb" ))
	search_engine_results_map = pickle.load( open( search_engine_results_path, "rb" ))

	print(google_results_map)
	print(search_engine_results_map)

	[overall_ndgc, ndgc_all_queries] = NDCG.compute_ndcg_score(google_results_map, search_engine_results_map, num_results_cap)

	print("NDCG@5 metric: " + str(overall_ndgc))

