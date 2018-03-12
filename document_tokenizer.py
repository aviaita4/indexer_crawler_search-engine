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

# Tokenize document: positions
def tokenize_document(fullpath):
	document_term_frequency = 0
	file_p = open(fullpath, 'r')
	text_data = file_p.read()
	tokenized_data = tokenize(text_data)
	tokenized_data_filtered = {}

	for i in range(len(tokenized_data)):
		token = tokenized_data[i]
		if token.isalpha():
			if not token.isupper():
				token = token.lower()
			document_term_frequency += 1 
			if token not in tokenized_data_filtered:
				tokenized_data_filtered[token] = [i]
			else:
				tokenized_data_filtered[token].append(i)

	return (tokenized_data_filtered, document_term_frequency)


				

