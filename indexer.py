import os
import json
from nltk import word_tokenize
from nltk.stem.snowball import EnglishStemmer
import string

stemmer = EnglishStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
       	stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
   	# text = "".join([ch for ch in text if ch not in string.punctuation])
   	tokens = word_tokenize(text)
   	stems = stem_tokens(tokens, stemmer)
   	return tokens

json_file = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/bookkeeping.json"
json_data = open(json_file).read()

links_data = json.loads(json_data)



if __name__ == "__main__":
	indir = "/Users/harsha/IR-Project3/WEBPAGES_CLEAN/"
	for i in range(1): #75
		curr_dir = indir + str(i) + "/"
		# for root, dirs, filenames in os.walk(curr_dir):
		filenames = ['107']
		for f in filenames:
			fullpath = os.path.join(curr_dir, f)
			print(fullpath)
			file_p = open(fullpath, 'r')
			text_data = file_p.read()
			print(text_data)
			print ('##################################################')
			print(tokenize(text_data))
			tokenized_data = tokenize(text_data)
			tokenized_data_filtered = {}
			for token in tokenized_data:
				token  = token.lower()
				if token.isalnum():
					if token not in tokenized_data_filtered:
						tokenized_data_filtered[token] = 1
					else:
						tokenized_data_filtered[token] += 1


				

