import os
import json
#import our document_tokenizer file
import document_tokenizer as Tokenizer

#create reverse index of a directory of files
def inverse_index(inverted_index, docs_base_dir, num_sub_dirs, path_url_map_filepath):

	json_data = open(path_url_map_filepath).read()
	path_url_map = json.loads(json_data)

	print("Creating Inverted-Index...")

	# For all documents
	for i in range(num_sub_dirs):
		curr_dir = docs_base_dir + str(i) + "/"
		
		for root, dirs, filenames in os.walk(curr_dir):
		# filenames = ['106','107']
			for f in filenames:
				fullpath = os.path.join(curr_dir, f)
				tokenized_data_filtered = Tokenizer.tokenize_document(fullpath)
				doc = {}
				doc["local_path"] = str(i) + "/" + f
				#doc["url"] = path_url_map[doc["local_path"]]

				inverted_index = index_document(inverted_index, doc, tokenized_data_filtered)

		print(str(i+1) + "/" + str(num_sub_dirs) + " sub_directories done.")
	return inverted_index

#update reverse index by including a document
def index_document(inverted_index, doc, tokenized_data_filtered):

	tokens_position_map = tokenized_data_filtered
	#url = doc["url"]
	path = doc["local_path"]

	for key in tokens_position_map:

		token_name = key
		token_positions = tokens_position_map[key]

		if token_name not in inverted_index:

			inverted_index[token_name] = {}
			inverted_index[token_name]["f"] = len(token_positions)
			inverted_index[token_name]["d"] = []
			
		else:

			inverted_index[token_name]["f"] += len(token_positions)

		#inverted_index[token_name]["documents_list"].append([url, path, token_positions])
		inverted_index[token_name]["d"].append([path, token_positions])

	return inverted_index