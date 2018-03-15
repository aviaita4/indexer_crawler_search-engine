from googlesearch import search
import time
import pickle
from urllib.parse import urlparse, parse_qs, urljoin
import re


def is_valid(url):
    parsed = urlparse(url)
    if parsed.scheme not in set(["http", "https"]):
        return False
    try:
        return ".ics.uci.edu" in parsed.hostname \
            and "calendar.ics.uci.edu" not in parsed.hostname \
            and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4"\
            + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
            + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
            + "|thmx|mso|arff|rtf|jar|csv"\
            + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        return False


def google_search(query, append_query, num_results_cap):

	total_query = query + append_query
	#print("Query: " + total_query)
	
	search_results = []
	
	for url in search(total_query, tld="com", num= 50, stop=1, pause=2):
		if(len(search_results) < num_results_cap):
			if is_valid(url):
				url = url.replace("http://","")
				url = url.replace("https://","")
				search_results.append(url)
		else:
			break
		#print(j)

	#print("----------------------------------------------------------------------------------------")

	return search_results

def google_search_list(queries, num_results_cap):

	append_query = " site:ics.uci.edu"

	google_query_results_map = {}

	for query in queries:
		print("Googling query: " + query + " in " + append_query + "...")
		res = google_search(query, append_query, num_results_cap)		
		google_query_results_map[query] = res

	return google_query_results_map
