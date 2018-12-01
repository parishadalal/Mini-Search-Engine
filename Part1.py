import re
import collections
import pickle

from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer

def sourceFile(source_file):
    beg_tag = re.compile(r'<DOC (\d)*>')
    end_tag = re.compile(r'</DOC>')
    data = []
    string = ""
    with open(source_file) as inputfile:
        tracer = inputfile.readlines()
        for current_tracer in tracer:
            if beg_tag.match(current_tracer):
                string = ""
            elif end_tag.match(current_tracer):
                data.append(string)
            else:
                string += current_tracer.strip()

    return data

#fileTokenizer will remove the stop words
def fileTokenizer(string):
    tokens = re.split(r'\s*[\',!.()="\-\s]*\s*', string)
    stopWords = ['the', 'is', 'at', 'of', 'on', 'and', 'a', '']
    washed_tokens = [word.lower() for word in tokens if word.lower() not in stopWords]
    #it will remove duplicate tokens
    removed = list(set(washed_tokens))
    return removed

#stemmer will help sort out simliar wods
def fileStemmer(string):
    porter_stemmer = PorterStemmer()
    return [porter_stemmer.stem(word) for word in string]

#
def fileLemmar(string):
    lemmar = WordNetLemmatizer()
    return [lemmar.lemmatize(word).encode('ascii') for word in string]

#this will check if there is an existing key or if there is not an existing key
def def_inverted_index(fileTokens, inverted_index, fileId):
    for word in fileTokens:
        if word in inverted_index:
            inverted_index[word][0] += 1
            inverted_index[word].append(fileId)
        else:
            parsing_list = [1, fileId]
            inverted_index[word] = parsing_list
    return

#  modules are integrated here
#  data list will contain content of each document as a "String"
#  collections.OrderedDict will sort the tokens alphabetically
#  tokens_file will use for comparison in part 2 for queries
#  inverted_index_file will print the inverted_index.txt
def run_inverted_index(file_name, inverted_index_file, tokens_file):
    
    
    data = sourceFile(file_name)

    fileId = 1
    inverted_index = {}
    for doc in data:
        token_list = fileStemmer(fileTokenizer(doc))
        def_inverted_index(token_list, inverted_index, fileId)
        fileId += 1
    
    inverted_index = collections.OrderedDict(sorted(inverted_index.items()))

    with open(tokens_file, 'as') as output1:
        pickle.dump(inverted_index, output1)
    
    with open(inverted_index_file, 'a') as output2:
        for line in inverted_index:
            print >> output2, '{:18},{:3},{:3}'.format(line, inverted_index[line][0], inverted_index[line][1:])

    return


if __name__ == '__main__':
    run_inverted_index('documents.txt', 'Part3a.txt', 'inverted_token_file')
